from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, WebsiteSearchTool

def process_report(raw_text):
    """
    Processes the blood test report using CrewAI and returns recommendations and articles.

    Parameters:
    - raw_text: The extracted text from the blood test report.

    Returns:
    - recommendations: Health recommendations based on the analysis.
    - articles: List of relevant articles found during the search.
    """
    
    # Define the tools
    search_tool = SerperDevTool()
    web_search_tool = WebsiteSearchTool()

    # Create Agents
    blood_test_analyst = Agent(
        role='Blood Test Analyst',
        goal='Analyze the blood test report to identify critical health indicators, abnormal values, and trends, providing a clear summary of findings to inform the user about their health status.',
        backstory='A medical expert with a background in laboratory diagnostics and clinical pathology. This agent is trained to interpret complex medical data and can recognize significant deviations from normal ranges, helping users understand potential health issues based on their blood tests.',
        verbose=True,
        allow_delegation=False
    )

    article_researcher = Agent(
        role='Article Researcher',
        goal='Utilize advanced search techniques to find reputable and relevant health-related articles that align with the findings from the blood test report, ensuring that users receive accurate and helpful information.',
        backstory='An expert researcher skilled in health information retrieval and literature review. This agent has access to various databases and search engines, enabling it to sift through vast amounts of information and pinpoint articles that can aid in understanding health conditions and recommended treatments.',
        tools=[search_tool, web_search_tool],
        verbose=True,
        allow_delegation=False,
    )

    health_advisor = Agent(
        role='Health Advisor',
        goal='Synthesize information from the retrieved articles and blood test analysis to provide personalized health recommendations tailored to the user’s specific needs and conditions.',
        backstory='A seasoned health advisor with expertise in nutrition, lifestyle medicine, and preventative healthcare. This agent understands the importance of holistic health approaches and can offer actionable recommendations based on current health knowledge and the user’s unique profile.',
        verbose=True,
        allow_delegation=False,
    )

    # Define Tasks
    analyze_blood_test_task = Task(
        description=f'Analyze the blood test report extracted from the user\'s PDF, focusing on identifying critical health indicators and summarizing the findings in an easy-to-understand format. The analysis should highlight any abnormal values and their potential implications for the user\'s health.',
        expected_output='A clear and concise summary of the blood test results, including key indicators, abnormal values, and potential health implications that the user should be aware of.',
        agent=blood_test_analyst,
    )

    find_articles_task = Task(
        description='Conduct a thorough search for reputable health articles that provide insights related to the identified health indicators from the blood test analysis. The articles should cover potential causes, implications, and management strategies for any abnormal results found in the analysis.',
        expected_output='A curated list of relevant health articles with links, brief summaries, and key takeaways that relate to the user\'s health concerns as indicated by their blood test results.',
        agent=article_researcher,
        context=[analyze_blood_test_task]
    )

    provide_recommendations_task = Task(
        description='Utilize the insights gained from the analyzed blood test report and the retrieved articles to formulate personalized health recommendations. These recommendations should be actionable, addressing the user\'s specific health concerns while promoting overall wellness.',
        expected_output='Personalized health recommendations along with links to the relevant articles, designed to empower the user with knowledge and actionable steps they can take to improve their health.',
        agent=health_advisor,
        context=[find_articles_task]
    )

    # Create a Crew
    crew = Crew(
        agents=[blood_test_analyst, article_researcher, health_advisor],
        tasks=[analyze_blood_test_task, find_articles_task, provide_recommendations_task],
        verbose=2
    )

    # Execute Tasks
    crew.kickoff()

    
    recommendations = crew.get_results(provide_recommendations_task)
    articles = crew.get_results(find_articles_task)

    return recommendations, articles
