# 🧠 Autonomous AI Agent for Share-of-Voice (SoV) Analysis  
### A project built for Atomberg Internship Submission

This repository contains an **AI-powered autonomous agent** that analyzes Atomberg’s online visibility across digital platforms by measuring **Share of Voice (SoV)**, sentiment polarity, brand mentions, and engagement across multiple keywords.

The agent scrapes real-time data from **YouTube** and **Twitter/X (via Nitter)**, processes unstructured text, executes sentiment analysis, extracts brand mentions, and produces cross-keyword competitive insights.

---

## 🚀 Features

- 🔍 Scrapes **YouTube & Twitter/X** for any keyword (no API required)
- 🚦 Extracts **top-N search results** (N = 20, configurable)
- 🧼 NLP-based **text cleaning & normalization**
- 🏷 Automated **brand mention detection**
- 😊 **Sentiment analysis** using VADER
- 📊 Computes **Share-of-Voice (SoV)** using a weighted metric
- 🔁 Supports **multi-keyword comparison**
- 📂 Saves all outputs as structured CSV files
- 💡 Generates **marketing insights** & recommendations

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-AGENT-FOR-SHARE-OF-VOICE-SoV-ANALYSIS.git
cd AI-AGENT-FOR-SHARE-OF-VOICE-SoV-ANALYSIS
```
### 2️⃣ Create Virtual Environment
python -m venv venv

### 3️⃣ Activate Environment

Windows:

venv\Scripts\activate

### 4️⃣ Install Dependencies
pip install requests beautifulsoup4 pandas vaderSentiment
(Optional visualizations)
pip install matplotlib

### ▶️ Running the AI Agent
To run the project:
python run_all.py
You will be prompted:
Enter keyword(s) to analyze (comma-separated).
Default = smart fan
→
Examples:
smart fan
BLDC fan
smart fan, BLDC fan, energy efficient fan
The agent processes each keyword independently and compares the results.

📊 Share-of-Voice (SoV) Formula
SoV = 0.5 × normalized_mentions + 0.3 × normalized_engagement + 0.2 × normalized_sentiment

Weight Justification:
Mentions (50%) → primary indicator of brand visibility
Engagement (30%) → reflects audience interaction & depth of impact
Sentiment (20%) → captures quality of brand perception.

📁 Output Files
All processed data and results are saved in:
/data/
Includes:
youtube_results.csv
twitter_results.csv
cleaned_<keyword>.csv
sov_output.csv
final_sov_comparison.csv


---

### 📄 Deliverables in This Repository
✔ AI Agent (run_all.py)
✔ Web scrapers
✔ NLP sentiment & mention analysis
✔ Complete SoV metric engine
✔ Multi-keyword results
✔ Cleaned CSV datasets
✔ Final formatted PDF report
---

## 🏗 Project Structure
AI-AGENT-FOR-SHARE-OF-VOICE-SoV-ANALYSIS/
│
├── scrapers/
│   ├── youtube_scraper.py
│   ├── twitter_scraper.py
│
├── nlp/
│   ├── clean_and_mentions.py
│   ├── sentiment.py
│
├── analysis/
│   ├── compute_sov.py
│
├── data/
│   ├── (generated CSV files)
│
├── run_all.py
├── README.md
└── Final_Report.pdf


---
## 👤 Author  
**RAHUL KRISHNA J**
📧 **Email:** [rahulkrishnaj@zohomail.in](mailto:rahulkrishnaj@zohomail.in)
---

