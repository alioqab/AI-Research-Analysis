# AI Research Analysis Dashboard

An interactive Streamlit dashboard that explores recent Artificial Intelligence research published on arXiv between **September 2025 and April 2026**.

The project combines **Exploratory Data Analysis (EDA)** and **Natural Language Processing (NLP)** to uncover research trends, dominant technologies, and common topics discussed across thousands of AI papers.

---

## Live Dashboard

🔗 Streamlit: https://your-app.streamlit.app

## Repository

🔗 GitHub: https://github.com/yourusername/AI.ResearchAnalysis

---

## Project Overview

This dashboard analyzes **7,701 AI research papers** from arXiv to answer questions such as:

- Which AI research fields publish the most papers?
- How concentrated is AI research across different categories?
- What topics are researchers discussing?
- Which technologies appear most frequently?
- How prevalent are Large Language Models (LLMs) across major AI fields?

---

## Dataset

- **Source:** arXiv
- **Time Period:** September 2025 – April 2026
- **Number of Papers:** 7,701
- **Number of Categories:** 107

The dataset was cleaned and processed using Python before being visualized in Streamlit.

---

## Dashboard Sections

### AI Research Overview
Provides a high-level summary of the dataset, including:

- Dataset statistics
- Top AI research categories
- Research concentration across categories

---

### Research Content Analysis

Analyzes the textual content of papers from the three largest research fields:

- Computer Vision
- Machine Learning
- Computational Linguistics

This section highlights the dominant research topics within each field using trigram analysis.

---

### Technology Trends

Identifies the most frequently discussed AI technologies and concepts extracted from the research papers.

Examples include:

- Large Language Models (LLMs)
- Vision Language Models (VLMs)
- Retrieval-Augmented Generation (RAG)
- Fine-tuning
- Diffusion Models

---

### Research Vocabulary

Explores the overall language used throughout the dataset using:

- Unigrams
- Bigrams
- Trigrams

These visualizations reveal the most common words and phrases appearing across AI research papers.

---

### Large Language Models in AI Research

Investigates the prevalence of Large Language Models within the three largest AI research fields by measuring the percentage of papers mentioning LLMs.

---

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- NLTK
- Scikit-learn

---

## Project Structure

```
AI.ResearchAnalysis/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│
├── data/
│
├── tables/
│
├── styles/
│
└── .streamlit/
```

---

## Running the Project

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application

```bash
streamlit run app.py
```

---

## Key Findings

- The top 10 AI categories account for over **87%** of all papers.
- Large Language Models are among the most frequently discussed technologies throughout the dataset.
- Nearly two-thirds of Computational Linguistics papers mention LLMs.
- Machine Learning and Computer Vision also demonstrate significant adoption of LLM-related research.

---

## Author

Ali Al-Malki

Bachelor of Computer Science

Data Analytics | Python | SQL | Power BI