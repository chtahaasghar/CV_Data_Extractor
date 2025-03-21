import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    pdf_document = fitz.open(stream=uploaded_file.getvalue(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in pdf_document])
    return text
