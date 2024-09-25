import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from pdf_analysis import analyze_pdf  # Function to analyze PDF
from email_utils import send_email     # Function to send emails
from crewai_integration import process_report  # Function to integrate with CrewAI

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Endpoint to analyze blood test report
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    email = request.form.get('email')

    if not email:
        return jsonify({'error': 'No email provided'}), 400
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Process the PDF file
    try:
        pdf_text = analyze_pdf(file)  # Analyze the PDF and get text
        recommendations, articles = process_report(pdf_text)  # Process with CrewAI

        # Send email with results
        send_email(email, recommendations, articles)

        return jsonify({
            'recommendations': recommendations,
            'articles': articles
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('PORT', 5000)))
