# Industrial Cybersecurity Data Analysis

This Jupyter project analyzes the supplied Edge-IIoT-style network traffic dataset. It includes reusable functions and a class, descriptive statistics, variance, standard deviation, quartiles, a scatter plot, histogram, box-and-whisker plot, Venn diagram, and a numerical summary.

## Project structure

```text
Industrial_Cybersecurity_Data_Analysis/
├── data/
│   └── cybersecurity_dataset.csv
├── notebooks/
│   └── cybersecurity_data_analysis.ipynb
├── src/
│   ├── __init__.py
│   └── data_analysis.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

1. Copy the supplied CSV into `data/` and name it `cybersecurity_dataset.csv`.
2. Create and activate a virtual environment.
3. Install packages with `pip install -r requirements.txt`.
4. Open `notebooks/cybersecurity_data_analysis.ipynb`.
5. Run the notebook from top to bottom.

The original dataset is intentionally excluded from Git by `.gitignore` because it is large. The notebook treats the records as a sample of wider industrial Internet of Things network traffic.
