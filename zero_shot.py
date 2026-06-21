import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TAGS = [
    "login_issue",
    "billing_issue",
    "network_issue",
    "technical_issue",
    "account_issue"
]
def predict_tags(ticket):
    prompt = f"""
You are a support ticket classifier.
Classify the ticket into relevant categories.
Available tags:
{TAGS}
Return TOP 3 most relevant tags with probability-like ranking.
Ticket:
{ticket}
Format:
1. tag1
2. tag2
3. tag3
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    df = pd.read_csv("../data/tickets.csv")
    for i, row in df.iterrows():
        print("\nTicket:", row["ticket_text"])
        print(predict_tags(row["ticket_text"]))
