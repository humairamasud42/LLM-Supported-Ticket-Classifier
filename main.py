from src.few_shot import predict_tags
import pandas as pd
df = pd.read_csv("data/tickets.csv")
results = []
for _, row in df.iterrows():
    prediction = predict_tags(row["ticket_text"])
    results.append({
        "ticket": row["ticket_text"],
        "true_tag": row["true_tag"],
        "prediction": prediction
    })
pd.DataFrame(results).to_csv("data/results.csv", index=False)
print("Done! Results saved.")