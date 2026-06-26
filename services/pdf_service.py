import re
import pdfplumber

pdf_path = r"C:\Prashely\Projects\ProofOfPayment\samples\PaymentConfirmation July 25 Maporch.pdf"

def extract_text_from_pdf(pdf_path):
    text = " "
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # ignore empaty pages or pdfs with no text
                text += page_text + "\n"
    return text

def clean_text(text):
    keywords = [
        "date",
        "amount",
        "reference",
        "beneficiary",
        "recipient",
        "payer",
        "account",
        "paid",
        "bank name",
        "date"
        "bank name",
        "reference number",
        "account number",
    ]

    lines = text.splitlines() # Split the text into individual lines "String"
    cleaned_lines = []

    for line in lines:
        line_lower = line.lower().strip()  # Convert the line to lowercase and remove leading/trailing whitespace

        if not line_lower: # Skip empty lines
            continue

        for keyword in keywords:
            if keyword in line_lower:
                cleaned_lines.append(line.strip()) #Append the original line (with leading/trailing whitespace removed) to the cleaned_lines list
                break # Exit the loop once the keyword is found
        lines_text = "\n".join(cleaned_lines) # Join the cleaned lines back into a single string with newline characters
    return lines_text

#In the future come back and parse data as JSON or dictionary instead of a string. This will make it easier to extract specific fields and values from the text.
#This will make it less error-prone and more efficient when working with the extracted data.
#AI costs will be reduced as well since the model will have to process less text and will be able to focus on the relevant information.

print(extract_text_from_pdf(pdf_path))
print(clean_text(extract_text_from_pdf(pdf_path)))



