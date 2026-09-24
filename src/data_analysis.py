"""Reusable functions and classes for exploratory cybersecurity data analysis."""

from pathlib import Path

import pandas as pd

try:
    from IPython.display import display
except ImportError:
    display = print


def enhance_dataframe_output(max_rows=20, max_columns=None, width=1400):
    """Configure pandas so wide cybersecurity records are easier to inspect."""
    pd.set_option("display.max_rows", max_rows)
    pd.set_option("display.max_columns", max_columns)
    pd.set_option("display.width", width)
    pd.set_option("display.max_colwidth", 60)
    print("DataFrame display settings updated successfully.")


class DataAnalyzer:
    """Load a CSV file and provide reusable methods for understanding it."""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path, low_memory=False)
        print("Dataset loaded successfully.")
        return self.df

    def _check_data_loaded(self):
        if self.df is None:
            raise ValueError("Run load_data() before using this method.")

    def display_sample(self, number_of_rows=5):
        self._check_data_loaded()
        display(self.df.head(number_of_rows))

    def display_shape(self):
        self._check_data_loaded()
        print("Number of rows:", self.df.shape[0])
        print("Number of columns:", self.df.shape[1])

    def display_columns(self):
        self._check_data_loaded()
        print("Column names:")
        for column in self.df.columns:
            print("-", column)

    def display_information(self):
        self._check_data_loaded()
        self.df.info()

    def display_missing_values(self):
        self._check_data_loaded()
        display(self.df.isna().sum().to_frame(name="Missing Values"))

    def display_duplicates(self):
        self._check_data_loaded()
        print("Number of duplicate rows:", self.df.duplicated().sum())

    def display_categorical_summary(self):
        self._check_data_loaded()
        for column in ["Attack_label", "Attack_type"]:
            if column in self.df.columns:
                print(f"\n{column}:")
                display(self.df[column].value_counts().to_frame(name="Count"))

    def full_summary(self):
        self.display_sample()
        self.display_shape()
        self.display_columns()
        self.display_information()
        self.display_missing_values()
        self.display_duplicates()
        self.display_categorical_summary()
