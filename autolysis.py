import os
import pandas as pd
import logging
import sys
from dotenv import load_dotenv
import requests
import plotly.express as px

# Load environment variables from .env file
load_dotenv()
API_TOKEN = os.getenv("AIPROXY_TOKEN")

# Validate API Token
if not API_TOKEN:
    sys.exit("Environment variable AIPROXY_TOKEN is not set. Please check your .env file.")

# AI Proxy setup
API_BASE = "https://aiproxy.sanand.workers.dev/openai/v1"

# Set up logging
logging.basicConfig(
    filename="autolysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Function: Load dataset dynamically
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path, encoding="latin1")
        logging.info("Dataset loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        sys.exit("Failed to load dataset. Check the file path or format.")

# Function: Preprocess data dynamically
def preprocess_data(data):
    try:
        # Separate numeric and non-numeric columns
        numeric_cols = data.select_dtypes(include=["number"])
        non_numeric_cols = data.select_dtypes(exclude=["number"])

        # Fill NaNs in numeric columns with the mean
        for col in numeric_cols.columns:
            data[col] = data[col].fillna(data[col].mean())

        # Fill NaNs in non-numeric columns with "Unknown"
        for col in non_numeric_cols.columns:
            data[col] = data[col].fillna("Unknown")

        logging.info("Data preprocessing completed.")
        return data
    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")
        sys.exit("Data preprocessing failed.")

# Function: Analyze data dynamically
def analyze_data(data):
    try:
        numeric_cols = data.select_dtypes(include=["number"])
        categorical_cols = data.select_dtypes(exclude=["number"])

        summary = numeric_cols.describe().to_string()
        missing = data.isnull().sum()
        correlation = numeric_cols.corr()

        categorical_summary = categorical_cols.describe(include="all").to_string() if not categorical_cols.empty else "No categorical data."

        logging.info("Data analysis completed.")
        return {
            "summary": summary,
            "missing": missing,
            "correlation": correlation,
            "categorical_summary": categorical_summary,
        }
    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        sys.exit("Data analysis failed.")

# Function: Generate dynamic narrative using AI Proxy
def generate_narrative(data_info, include_summary=True, include_missing=True, include_correlation=True, include_categorical=True):
    try:
        # Create prompt dynamically based on the user's preference
        prompt = "You are a data analyst. Here is the dataset summary:\n\n"

        if include_summary:
            prompt += f"Dataset Summary:\n{data_info['summary']}\n\n"

        if include_missing:
            prompt += f"Missing values:\n{data_info['missing']}\n\n"

        if include_correlation:
            prompt += f"Correlation analysis (if applicable):\n{data_info['correlation']}\n\n"

        if include_categorical:
            prompt += f"Categorical data summary:\n{data_info['categorical_summary']}\n\n"

        prompt += "Write a detailed analysis story with insights, implications, and recommendations."

        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "gpt-4o-mini",  # or another smaller model to optimize time
            "messages": [{"role": "user", "content": prompt}],
        }

        response = requests.post(f"{API_BASE}/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        narrative = response.json()["choices"][0]["message"]["content"]
        logging.info("Narrative generated successfully.")
        return narrative

    except Exception as e:
        logging.error(f"Error generating narrative: {e}")
        sys.exit("Failed to generate narrative.")

# Function: Create README.md dynamically in the main project directory
def create_readme(narrative, project_dir, dataset_name):
    try:
        # Save the README with a naming convention as "<dataset_name>_README.md" in the main project directory
        readme_filename = f"{dataset_name}_README.md"
        readme_path = os.path.join(project_dir, readme_filename)
        with open(readme_path, "w") as file:
            file.write(f"# Analysis Report for {dataset_name}\n\n")
            file.write(narrative)
        logging.info(f"{readme_filename} created successfully: {readme_path}")
    except Exception as e:
        logging.error(f"Error creating README.md: {e}")
        sys.exit("Failed to create README.md.")

# Main function
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python autolysis.py <dataset_path>")

    file_path = sys.argv[1]
    dataset_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract dataset name without extension
    project_dir = os.getcwd()  # Use the current working directory as the project directory

    data = load_dataset(file_path)
    processed_data = preprocess_data(data)
    analysis_results = analyze_data(processed_data)

    narrative = generate_narrative(
        analysis_results, 
        include_summary=True, 
        include_missing=True,
        include_correlation=True,
        include_categorical=True
    )

    create_readme(narrative, project_dir, dataset_name)

if __name__ == "__main__":
    main()
