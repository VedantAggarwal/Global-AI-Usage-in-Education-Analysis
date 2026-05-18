# Global AI Usage in Education Analysis

## Project Overview
Artificial Intelligence (AI) has become an increasingly important component of modern education systems. From assisting students in learning tasks to supporting teachers and institutions in educational processes, AI tools are now widely integrated into academic environments. As AI adoption continues to grow, understanding accessibility, usage patterns, and structural factors influencing adoption becomes increasingly relevant.

This project analyzes global AI usage in education using data collected from 10 countries between January 2015 and April 2026. The analysis focuses on AI adoption trends, country-level comparisons, infrastructural influence, and educational development indicators associated with AI usage.

---

## Objectives
- Analyze AI usage trends in education over time
- Compare AI adoption patterns across countries
- Study the relationship between internet penetration and AI usage
- Study the relationship between education index and AI adoption

---

## Dataset
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/abidhussai512/global-ai-in-education-dataset-20152026)
- **Time Span:** January 2015 to April 2026
- **Countries Included:**  
  United States, United Kingdom, China, India, Germany, Brazil, Pakistan, Nigeria, Canada, Australia

### Major Features
- `country`
- `year`
- `internet_penetration_pct`
- `education_index`
- `urban_ai_usage_pct`
- `rural_ai_usage_pct`
- `student_ai_usage_pct`
- `teacher_ai_usage_pct`
- `schools_ai_adoption_pct`
- `gender_gap_ai_usage_pct`

---

## Project Workflow
1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Aggregation
4. Visualization
5. Insight Generation

---

## Repository Structure

```bash
GLOBAL-AI-USAGE-IN-EDUCATION/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── interim/
│       └── insights
│       └── plotting
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   └── 03_visualizations_and_insights.ipynb
│
├── reports/
│   ├── figures/
│   ├── final_report.md
│   └── presentation.pdf
│
├── src/
│   ├── cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   └── data_io.py
│
├── config/
│   └── config.yaml
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Key Insights
- Urban AI usage consistently exceeds rural AI usage across countries and years.
- Student AI usage grows faster than teacher AI usage over time.
- Countries with higher internet penetration generally exhibit stronger AI adoption.
- Stronger education systems show higher institutional AI adoption and more consistent AI usage patterns.
- Gender gap in AI usage remains relatively stable across years.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## How to Run

### 1. Clone the repository
```bash
git clone <repository-link>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run notebooks
Open the notebooks in Jupyter Notebook or VS Code and execute them sequentially:

1. `01_data_cleaning.ipynb`
2. `02_exploratory_data_analysis.ipynb`
3. `03_visualizations_and_insights.ipynb`

---

## Future Improvements
- Build an interactive dashboard
- Perform predictive analysis on AI adoption trends
- Apply clustering techniques for country segmentation
- Expand analysis using more countries and larger datasets
- Incorporate policy-level and demographic-level analysis
