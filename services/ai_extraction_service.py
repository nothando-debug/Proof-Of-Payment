from openai import OpenAI
import os

client = OpenAI(api_key="")


def extract_payment_data(text: str):
    """
    Takes cleaned text from PDF service
    Returns structured JSON (dict)
    """

    prompt = f"""
You are a proof of payment data extraction system.

Extract the following fields from the text:
- beneficiary
- payer
- amount
- date
- reference
- account number

Return ONLY valid JSON.
No explanation.

TEXT:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You extract structured payment data from text."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content