# Blood Test Analysis with CrewAI

## Project Overview
This project is designed to analyze blood test reports, search for relevant health articles, and provide personalized health recommendations using the CrewAI framework. The system processes a user's blood test report, extracts important health indicators, finds related articles, and delivers actionable health advice via email.

## Approach and Methodology

1. **PDF Analysis**:
   - Uses the `PyPDF2` library to extract text from PDF blood test reports.
   - Focuses on specified pages containing relevant health data.

2. **Agent-Based Architecture**:
   - Implements three main agents:
     - **Blood Test Analyst**: Summarizes health indicators and abnormalities from the blood test report.
     - **Article Researcher**: Searches for reputable health articles related to the analysis results.
     - **Health Advisor**: Provides tailored health recommendations based on the analysis and articles found.

3. **CrewAI Integration**:
   - Utilizes the CrewAI framework for task execution and communication between agents.

4. **API Development**:
   - A secure POST API endpoint accepts PDF blood test reports and user email addresses, sending personalized recommendations and articles via email.

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- API keys for SERPER and OpenAI (to be added in the `.env` file)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/madhumayi-parakala/blood-test-analysis-ollama.git
   cd blood-test-analysis-ollama

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables**:
   Create a .env file and add your API keys:
   ```bash
   SERPER_API_KEY=your_serper_api_key
   OPENAI_API_KEY=your_openai_api_key

5. **Run the Application**:
   ```bash
   python app.py

## Testing
To run the tests, follow these steps:

1. Ensure you have the required dependencies installed:
   ```bash
   pip install -r requirements.txt

2. Navigate to the tests directory:
   '''bash
   cd tests

3. Run the test suite:
   '''bash
   python -m unittest test_app.py

## Usage

To analyze a blood test report, send a POST request to the `/analyze` endpoint with the following parameters:

- `pdf`: The blood test report in PDF format.
- `email`: The user's email address to receive recommendations.

### Example using `curl`
You can use the following `curl` command to send the request:

```bash
curl -X POST -F "pdf=@/path/to/blood_test_report.pdf" -F "email=user@example.com" http://localhost:5000/analyze






   
