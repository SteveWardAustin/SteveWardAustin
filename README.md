# Common Mind Survey Analysis

Data analytics project for Common Mind - analyzing survey results from Typeform exports using Python, AI, and exploratory data analysis (EDA).

## Project Structure

```
├── data/
│   ├── raw/              # Typeform export files (CSV/Excel)
│   └── processed/        # Cleaned and transformed data
├── notebooks/            # Jupyter notebooks for EDA and analysis
├── src/
│   ├── analysis/         # Analysis modules
│   └── utils/            # Utility functions
├── requirements.txt      # Python dependencies
└── README.md
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Add your API keys (e.g., OpenAI) to .env
   ```

4. Place Typeform export files in `data/raw/`

## Usage

1. Run the EDA notebook:
   ```bash
   jupyter notebook notebooks/01_eda.ipynb
   ```

2. For AI-powered analysis, ensure your OpenAI API key is set in `.env`

## Data Privacy

Survey data contains sensitive respondent information. Raw data files are excluded from version control via `.gitignore`.
