# 📊 Page View Time Series Visualizer

This project is part of the **freeCodeCamp Data Analysis with Python** curriculum.  
It visualizes time series data from the **freeCodeCamp forum** to analyze daily page views between **2016-05-09 and 2019-12-03**.

You’ll find three types of visualizations:
- **Line plot** → trends of daily page views.
- **Bar plot** → average daily page views per month, grouped by year.
- **Box plots** → year-wise trend and month-wise seasonality.

---

## 🚀 Features
- Data cleaning (remove outliers using 2.5%–97.5% quantiles).
- Line chart of daily page views.
- Bar chart grouped by year and month.
- Year-wise and Month-wise box plots for trend and seasonality analysis.
- Fully tested with **unittest / pytest**.

---

## 🛠️ Technologies Used
- **Python 3**
- **Pandas** (data handling)
- **Matplotlib** (line & bar plots)
- **Seaborn** (box plots)
- **Pytest / Unittest** (testing)


---

## ⚙️ Setup Instructions

### 1. Clone the repository
    git clone https://github.com/<your-username>/pageview-visualizer.git
    cd pageview-visualizer
### 2. Create a virtual environment (recommended):
    python -m venv venv
    venv\Scripts\Activate.bat
### 3. Install dependencies:
    pip install -r requirements.txt
### 4. Run the project:
    python main.py
### 5. Run tests:
    pytest -q
