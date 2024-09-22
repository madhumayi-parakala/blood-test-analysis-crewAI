from PyPDF2 import PdfReader

def analyze_pdf(file):
    """
    Extracts text from the provided PDF file.

    Parameters:
    - file: A PDF file object.

    Returns:
    - raw_text: The extracted text from the PDF.
    """
    raw_text = ''
    try:
        reader = PdfReader(file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                raw_text += content + '\n'
    except Exception as e:
        raise ValueError(f"Error reading the PDF file: {str(e)}")

    return raw_text.strip()
