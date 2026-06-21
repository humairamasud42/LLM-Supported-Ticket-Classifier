# LLM Support Ticket Auto Tagging

Automatically classify customer support tickets into relevant categories using Large Language Models (LLMs). This project demonstrates the effectiveness of Zero-Shot and Few-Shot Prompt Engineering for automated ticket tagging and category prediction.

---

## Project Overview

Support teams receive thousands of customer queries daily. Manually categorizing these tickets is time-consuming and error-prone.

This project uses an LLM to automatically:

- Analyze support ticket text
- Predict relevant categories
- Generate Top-3 probable tags
- Compare Zero-Shot and Few-Shot classification performance

---

## Objectives

- Automate support ticket categorization using LLMs
- Compare Zero-Shot and Few-Shot prompting techniques
- Improve classification accuracy using prompt engineering
- Generate ranked Top-3 tag predictions for each ticket

---

## Technologies Used

- Python
- OpenAI GPT
- Pandas
- NumPy
- Scikit-Learn
- Prompt Engineering
- Few-Shot Learning
- Zero-Shot Learning

---

##  Project Structure

```text
LLM-Support-Ticket-Auto-Tagging/
│
├── data/
│   ├── tickets.csv
│   └── results.csv
│
├── src/
│   ├── zero_shot.py
│   ├── few_shot.py
│   └── evaluate.py
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## Dataset

The dataset contains customer support tickets and their actual categories.

Example:

| ticket_text | true_tag |
|------------|-----------|
| Unable to login to account | login_issue |
| Payment failed during checkout | billing_issue |
| Internet connection not working | network_issue |

---

##  Classification Categories

Example tags:

- login_issue
- account_issue
- billing_issue
- payment_issue
- network_issue
- technical_issue
- service_issue
- authentication_issue

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/LLM-Support-Ticket-Auto-Tagging.git

cd LLM-Support-Ticket-Auto-Tagging
```

---

##  Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```


##  Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Configure OpenAI API Key

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_api_key_here
```

---

# Running the Project

Run the complete pipeline:

```bash
python main.py
```

---

## Zero-Shot Classification

```bash
python src/zero_shot.py
```

---

## Few-Shot Classification

```bash
python src/few_shot.py
```

---

## Evaluation

```bash
python src/evaluate.py
```

---

#  Methodology

## Zero-Shot Learning

The model receives only the ticket and available categories.

Example:

```text
Ticket:
Unable to login to my account

Predict the most relevant tags.
```

---

## Few-Shot Learning

The model receives labeled examples before prediction.

Example:

```text
Ticket: My internet is not working
Tags: network_issue

Ticket: Unable to login
Tags: login_issue

Now classify:
Unable to access my account
```

Few-shot prompting generally improves accuracy by providing context and examples.

---



---

# Evaluation Metrics

The project compares:

- Zero-Shot Accuracy
- Few-Shot Accuracy
- Top-1 Prediction Accuracy
- Top-3 Prediction Accuracy

---

#  Results

| Method | Accuracy |
|----------|----------|
| Zero-Shot | Lower |
| Few-Shot | Higher |

Few-shot prompting improves ticket classification performance by providing contextual examples to the LLM.

---

# Skills Demonstrated

### Natural Language Processing (NLP)

- Text Classification
- Multi-Class Classification
- Multi-Label Prediction

### Prompt Engineering

- Zero-Shot Prompting
- Few-Shot Prompting

### Machine Learning Concepts

- Classification Evaluation
- Ranking Predictions
- Accuracy Analysis

### Software Development

- Python Development
- API Integration
- Dataset Processing

---

#  Project Coverage

- Prompt Engineering

- LLM-Based Text Classification

- Zero-Shot Learning

- Few-Shot Learning

- Top-3 Tag Prediction

- Performance Comparison

- Automated Ticket Categorization

---

# Future Improvements

- Fine-Tune Open Source LLMs
- Streamlit Dashboard
- FastAPI Deployment
- Vector Database Integration
- RAG-Based Ticket Understanding
- Real-Time Customer Support Assistant

---


---

## ⭐ If you found this project useful, consider giving it a star!
