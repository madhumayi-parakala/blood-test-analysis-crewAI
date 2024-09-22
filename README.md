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
