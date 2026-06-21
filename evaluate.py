import pandas as pd
def simple_match(true_tag, predicted_text):
    return true_tag.lower() in predicted_text.lower()
def evaluate(file_path):
    df = pd.read_csv(file_path)
    correct = 0
    for _, row in df.iterrows():
        if simple_match(row["true_tag"], str(row["prediction"])):
            correct += 1
    accuracy = correct / len(df)
    print(f"Accuracy: {accuracy:.2f}")
if __name__ == "__main__":
    evaluate("../data/results.csv")