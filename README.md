# 📱 Mobile Sales Analysis with GenAI & Power BI

A comprehensive analysis of mobile phone sales data that combines traditional data cleaning and machine learning with modern Generative AI to produce automated business insights.

![Power BI Visualization](power%20BI%20visualization.jpeg)

## 📌 Project Overview

This project analyzes mobile phone sales data end-to-end — from raw data cleaning through to AI-generated business insights. It blends classic data science (Pandas, Scikit-Learn) with an interactive Power BI dashboard and Google Gemini AI to automatically summarize trends and recommend strategy.

## ✨ Key Features

- **Data Cleaning & ML** — Used Python (Pandas) to clean and prepare the raw sales dataset, and Scikit-Learn for a simple price prediction model based on ratings and discounts.
- **Data Visualization** — Built an interactive Power BI dashboard to compare brand performance and discount trends.
- **AI-Generated Insights** — Integrated the Google Gemini API (2.0 Flash) to automatically generate business summaries and strategic recommendations directly from the data.

## 🛠️ Tech Stack

| Category | Details |
|---|---|
| **Language** | Python 3.13 |
| **Libraries** | Pandas, Seaborn, Matplotlib, google-genai |
| **BI Tool** | Power BI Desktop |
| **AI Model** | Google Gemini 2.0 Flash |

## 📁 Project Files

| File | Description |
|---|---|
| `Sales.csv` | Raw mobile sales dataset |
| `Cleaned_Mobile_Sales.csv` | Cleaned dataset after preprocessing |
| `my.py` | Data cleaning and ML script |
| `ai_summary.py` | Generates AI-powered business insights via Gemini API |
| `power BI visualization.jpeg` | Power BI dashboard screenshot |
| `brand_report.png` | Brand performance report visualization |
| `output image.jpeg` | Sample output from the analysis |

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- A [Google Gemini API key](https://ai.google.dev/) (for AI-generated summaries)
- Power BI Desktop (optional, for viewing/editing the dashboard)

### Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/ashmieee/Mobile-Sales-AI-Analysis.git
   cd Mobile-Sales-AI-Analysis
   ```

2. Install dependencies:
   ```bash
   pip install pandas google-genai seaborn matplotlib scikit-learn
   ```

3. Run the data cleaning script:
   ```bash
   python my.py
   ```

4. Generate AI-powered insights (requires a Gemini API key):
   ```bash
   python ai_summary.py
   ```

5. View the visualizations in `power BI visualization.jpeg` and `brand_report.png`, or open the `.pbix` file in Power BI Desktop if included.

## 💡 Key Insights

The pipeline surfaces patterns in brand performance, pricing, and discount strategy, and pairs those with AI-generated natural-language summaries to make the findings easy to act on.

## 👩‍💻 Author

**Ashmita Gupta**
*Aspiring Data Analyst | Power BI | SQL | Data Visualization*

## 📄 License

No license has been specified for this project. All rights reserved by the author unless stated otherwise.
