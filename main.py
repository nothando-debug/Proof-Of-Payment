from services.ai_extraction_service import extract_payment_data
from services.pdf_service import extract_text_from_pdf, clean_text

text = extract_text_from_pdf(r"C:\Prashely\Projects\ProofOfPayment\samples\PaymentConfirmation July 25 Maporch.pdf")
cleaned_text = clean_text(text)

extracted_data = extract_payment_data(cleaned_text)
print(extracted_data)


