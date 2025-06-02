from PyPDF2 import PdfReader

def read_pdf(pdf_bytes):
    text = ""
    pdf = PdfReader(pdf_bytes)
    for page in pdf.pages:
        text += page.extract_text()
        for image_num , image_file_obj in enumerate(page.images):
            text += read_images(image_file_obj.data)
    return text


def read_images(image_bytes: bytes):
    text = ""
    # will add more functionality regarding this using some vision models for
    # more understanding
    return text


