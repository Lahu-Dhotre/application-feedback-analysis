# Banking Application Logout Feedback Analysis

A Jupyter notebook project for analyzing synthetic user feedback on the logout experience across 100 banking applications. The analysis combines statistical summaries, sentiment scoring, text mining, and visualization to uncover satisfaction drivers, pain points, and application-level performance trends.

## Overview

This repository contains a notebook-based data analysis workflow that:

- Generates synthetic feedback data for 100 banking applications
- Simulates realistic 1–5 star ratings and free-text reviews
- Applies dual sentiment scoring using TextBlob and VADER
- Identifies frequent words and themes in negative/positive feedback
- Produces visualizations and summary metrics for business insights
- Exports analysis results to CSV files for downstream use

The project is intentionally designed as a notebook-first analysis workflow rather than a traditional application codebase.

## Project Goals

- Measure customer satisfaction around logout experience
- Compare performance across multiple banking applications
- Detect patterns in good and poor logout feedback
- Summarize insights in an executive-friendly format
- Create reusable analysis outputs from synthetic but realistic data

## Repository Structure

```text
.
├── feedback_analysis.ipynb          # Main analysis notebook
├── create_notebook.py              # Generates/regenerates the notebook
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
├── SETUP_GUIDE.txt                 # Quick setup instructions
├── CLAUDE.md                      # Repository guidance for Claude Code
├── feedback_analysis_with_sentiment.csv  # Generated full dataset export
├── summary_statistics.csv          # Summary metrics export
├── application_summary.csv         # Per-application summary export
└── .gitignore
```

## Dataset Characteristics

The generated dataset includes:

- 100 banking applications
- 5,400 records total (54 per application)
- 1–5 star ratings
- Realistic application-agnostic feedback templates tied to rating levels
- Reproducible results through a fixed random seed (`random.seed(42)`) 

Example rating pattern:

- 5-star: 30%
- 4-star: 35%
- 3-star: 20%
- 2-star: 10%
- 1-star: 5%

## Analysis Pipeline

The notebook follows this flow:

1. Synthetic data generation
2. Statistical overview
3. Sentiment analysis
4. Text mining and keyword analysis
5. Visualizations and comparisons
6. Insight generation and recommendations
7. CSV export

## Sentiment Analysis

The project uses a dual-method sentiment model for robustness:

- TextBlob polarity score (-1 to +1)
- VADER compound score (-1 to +1)
- Final sentiment score = average of both methods
- Sentiment categories:
  - Positive: score >= 0.3
  - Neutral: -0.3 < score < 0.3
  - Negative: score <= -0.3

This helps combine general NLP polarity with social-text sentiment detection.

## Features

### Data Generation

- Builds 100 unique banking application names from combinations of:
  - 10 bank types
  - 10 regions
  - 10 service names
- Produces realistic feedback for each rating level
- Ensures reproducible synthetic analysis results

### Statistical Analysis

- Rating distribution analysis
- Satisfaction and issue-rate tracking
- Correlation between rating and sentiment
- Per-application performance summaries

### Text Mining

- Keyword frequency analysis
- Word cloud generation
- Theme extraction from positive and negative feedback
- Review pattern analysis by sentiment category

### Visualization

- Rating histograms and summary charts
- Distribution and comparison plots
- Scatter plots for sentiment vs. rating
- Word clouds for overall and grouped views
- Top application performance visual comparisons

### Exportable Outputs

The notebook generates these CSV files:

- `feedback_analysis_with_sentiment.csv` — full feedback dataset with sentiment metrics
- `summary_statistics.csv` — high-level KPI summary
- `application_summary.csv` — per-application performance statistics

## Getting Started

### Prerequisites

- Python 3.9+
- pip
- Jupyter environment

### Installation

```bash
pip install -r requirements.txt
```

### Download NLP resources

```bash
python -m textblob.download_corpora
```

If missing NLTK resources are encountered during execution, you may also install them manually:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

### Run the notebook

```bash
jupyter notebook feedback_analysis.ipynb
```

Then in Jupyter:

- Select the notebook
- Choose `Kernel > Restart & Run All`

## Regenerating the Notebook

If the notebook has been corrupted or needs to be rebuilt:

```bash
python create_notebook.py
```

This recreates the notebook from the notebook-generation definitions in `create_notebook.py`.

## Typical Project Metrics

The current synthetic dataset produces results similar to:

- Average rating: ~3.81 / 5
- Satisfaction rate: ~66.7%
- Sentiment correlation: ~0.805
- 100 application summaries in export output

## Customization

The notebook is designed so you can adjust the synthetic analysis in a few places:

### Change dataset size or application count

Edit the generation logic in the notebook cell that creates applications and records.

### Adjust rating distribution

Modify the `rating_distribution` values in the synthetic generation cell.

### Change sentiment thresholds

Update the `categorize_sentiment()` logic in the relevant analysis cell.

### Expand feedback templates

Add or replace entries in the per-rating feedback lists used to generate realistic review text.

## Troubleshooting

### Module not found

If you see an error like `ModuleNotFoundError: No module named 'textblob'`:

```bash
pip install -r requirements.txt
```

### Missing NLTK data

If you see a message such as `LookupError: Resource punkt not found`:

```bash
python -m textblob.download_corpora
```

### Word cloud blank or missing output

Ensure the generated feedback text is non-empty and the relevant NLP resources are installed correctly.

### Notebook rendering issues

Make sure Jupyter is installed and the notebook is launched in the project directory:

```bash
pip install jupyter ipykernel
```

## Important Notes

- The project uses synthetic data, not real production feedback.
- The generated CSV outputs are expected to stay consistent with the notebook logic.
- Do not rename core output columns without updating downstream analysis logic.
- Preserve the fixed random seed when reproducibility is important.

## License

This project is provided for educational and analytical use. Please review any organization-specific licensing requirements before using it beyond local analysis.

## Contributing

This repository is primarily a notebook-driven analysis project. Contributions are welcome in the form of:

- improved notebook logic
- better visualizations
- additional feedback templates
- documentation improvements
- performance or clarity enhancements

## Support

For issues or questions:

1. Review the notebook cells and comments
2. Check the troubleshooting section above
3. Rebuild the notebook using `python create_notebook.py`
4. Verify all Python dependencies are correctly installed

---

Built for exploratory banking user-experience analysis and synthetic sentiment evaluation.
