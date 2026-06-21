import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EXAMPLES = """
Ticket: My internet is not working
Tags: network_issue, technical_issue, service_issue
Ticket: I want refund for my order
Tags: billing_issue, refund_issue, payment_issue
Ticket: Can't login to account
Tags: login_issue, account_issue, authentication_issue
"""

def predict_tags(ticket):
    prompt = f"""
You are an expert support ticket classifier.
Here are examples:
{EXAMPLES}
Now classify this ticket:
Ticket: {ticket}
Return top 3 tags ranked by relevance.
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