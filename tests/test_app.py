import unittest
from pdf_analysis import extract_text_from_pdf
from crewai_integration import process_report

class TestBloodTestAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample PDF path (update this path as needed for your local setup)
        self.pdf_path = '/path/to/sample_blood_test_report.pdf'
        self.raw_text = extract_text_from_pdf(self.pdf_path)

    def test_extract_text_from_pdf(self):
        """Test if text extraction from PDF is successful and not empty."""
        self.assertIsNotNone(self.raw_text)
        self.assertGreater(len(self.raw_text), 0, "Extracted text should not be empty.")

    def test_process_report(self):
        """Test if the report processing returns valid recommendations and articles."""
        recommendations, articles = process_report(self.raw_text)

        # Ensure recommendations and articles are returned
        self.assertIsNotNone(recommendations)
        self.assertIsNotNone(articles)

        # Check if recommendations and articles have content
        self.assertGreater(len(recommendations), 0, "Recommendations should not be empty.")
        self.assertGreater(len(articles), 0, "Articles list should not be empty.")

if __name__ == '__main__':
    unittest.main()
