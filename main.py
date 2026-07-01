from pathlib import Path
from services.ai_extraction_service import extract_payment_data
from services.pdf_service import extract_text_from_pdf, clean_text

BASE_DIR = Path(__file__).resolve().parent

pdf_path =  BASE_DIR / "samples" / "PaymentConfirmation July 25 Maporch.pdf"

text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(text)

print("CLEANED TEXT")
extracted_data = extract_payment_data(cleaned_text)
print(extracted_data)


