# Banking Application Logout Feedback Analysis

## Overview

This project provides a comprehensive Jupyter notebook for analyzing user feedback on logout experience across three banking enterprise applications:
- **Collections**
- **Payments**
- **Customer Service Center**

The analysis includes synthetic data generation, statistical analysis, sentiment analysis, text mining, and actionable insights with visualizations.

## Features

### 📊 Data Analysis
- **Synthetic Dataset**: 570+ realistic feedback records with ratings (1-5 stars) and contextual feedback
- **Statistical Analysis**: Distribution analysis, correlation tests, and performance comparisons
- **Sentiment Analysis**: TextBlob and VADER sentiment scoring with polarity categorization
- **Text Mining**: Keyword extraction, frequency analysis, and theme identification

### 📈 Visualizations
- Rating distribution histograms and box plots
- Sentiment distribution pie charts and stacked bar charts
- Word clouds (overall, by application, and by sentiment)
- Trend analysis with moving averages
- Cumulative satisfaction and issue tracking
- Heatmaps and scatter plots

### 💡 Insights & Recommendations
- Application performance rankings
- Critical issue identification
- Satisfaction driver analysis
- Priority matrix for actionable items
- Strategic recommendations with implementation timelines

### 📋 Export Capabilities
- Processed dataset with sentiment scores (CSV)
- Summary statistics table (CSV)
- Application-wise performance summary (CSV)

## Quick Start

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Installation

1. **Clone/Download the project:**
```bash
cd /path/to/application_feedback_analysis
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download NLTK data (one-time setup):**
```bash
python -m textblob.download_corpora
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

### Running the Notebook

```bash
jupyter notebook feedback_analysis.ipynb
```

This will open the notebook in your default browser. Run all cells sequentially (Kernel → Restart & Run All) to generate the complete analysis.

## Notebook Structure

### Cell 1: Setup and Imports
Loads all required libraries and configures visualization settings.

### Cell 2: Synthetic Dataset Generation
Generates 570 realistic feedback records with:
- 3 banking applications (equal distribution)
- 1-5 star ratings with realistic distribution
- Application and rating-specific feedback templates

### Cell 3: Data Overview
Displays dataset summary, missing values, and basic statistics.

### Cell 4: Rating Distribution Analysis
- Overall rating distribution
- Rating statistics by application
- Distribution comparisons

### Cell 5: Sentiment Analysis
- TextBlob and VADER sentiment scoring
- Sentiment categorization (Positive/Neutral/Negative)
- Sentiment statistics

### Cell 6: Sentiment Distribution & Visualization
- Sentiment pie charts and stacked bar charts
- Sentiment vs rating scatter plots
- Sentiment trends

### Cell 7: Text Analysis & Keywords
- Top 20 keywords across all feedback
- Application-specific keyword analysis
- Frequency histograms

### Cell 8: Word Clouds
- Overall feedback word cloud
- Sentiment-specific word clouds
- Application-specific word clouds

### Cell 9: Issue Identification & Summary
- Low-rated feedback analysis (1-2 stars)
- High-rated feedback analysis (4-5 stars)
- Issue and satisfaction driver visualization

### Cell 10: Executive Summary & KPIs
- Overall metrics (satisfaction rate, issue rate, sentiment)
- Application performance comparison
- Key findings and recommendations

### Cell 11: Data Export
- Export processed dataset with sentiment scores
- Export summary statistics
- Generate CSV files for further analysis

## Analysis Metrics

### Key Performance Indicators (KPIs)
- **Average Rating**: Overall satisfaction measured on 1-5 scale
- **Satisfaction Rate**: Percentage of 4-5 star ratings
- **Issue Rate**: Percentage of 1-2 star ratings
- **Sentiment Score**: Polarity score from -1 (negative) to +1 (positive)
- **Correlation**: Rating-sentiment alignment metric

### Application Comparison
For each application, the analysis provides:
- Average rating and distribution statistics
- Satisfaction and issue rates
- Sentiment scores
- Top keywords and themes
- Performance ranking

## Dataset Details

### Columns
- **application_name**: Collections, Payments, or Customer Service Center
- **rating**: Integer from 1 to 5 stars
- **feedback**: Text feedback describing the logout experience
- **sentiment_textblob**: TextBlob polarity score (-1 to +1)
- **sentiment_vader**: VADER compound score (-1 to +1)
- **sentiment_score**: Average of TextBlob and VADER scores
- **sentiment_category**: Categorized as Positive, Neutral, or Negative

### Rating Distribution (Synthetic)
- 5 stars: 30%
- 4 stars: 35%
- 3 stars: 20%
- 2 stars: 10%
- 1 star: 5%

## Export Files

After running the notebook, three CSV files are generated:

### 1. feedback_analysis_with_sentiment.csv
Complete dataset with sentiment analysis results
```
application_name,rating,feedback,sentiment_score,sentiment_category
Collections,5,"Excellent logout process...",0.85,Positive
...
```

### 2. summary_statistics.csv
Key metrics summary
```
Metric,Value
Total Records,570
Average Rating,3.78
Average Sentiment Score,0.452
Satisfaction Rate,64.2%
...
```

### 3. application_summary.csv
Per-application performance statistics

## Interpretation Guide

### Rating Scale
- **5 stars**: Excellent experience, highly satisfied
- **4 stars**: Good experience, satisfied
- **3 stars**: Average experience, neutral
- **2 stars**: Poor experience, dissatisfied
- **1 star**: Terrible experience, very dissatisfied

### Sentiment Categories
- **Positive**: Feedback with sentiment score ≥ 0.3 (praising features, quick responses, security)
- **Neutral**: Feedback with sentiment score between -0.3 and 0.3 (mixed or factual)
- **Negative**: Feedback with sentiment score ≤ -0.3 (complaints, issues, concerns)

### Correlation Interpretation
- Correlation > 0.7: Strong positive alignment between sentiment and rating
- Correlation 0.3-0.7: Moderate alignment
- Correlation < 0.3: Weak alignment (may indicate mismatches)

## Recommendations Framework

### Performance Levels
- **🟢 Good (Rating ≥ 3.8)**: Maintain quality, monitor improvements
- **🟡 Fair (Rating 3.2-3.8)**: Address issues within 2-4 weeks
- **🔴 Critical (Rating < 3.2)**: Implement immediate action plan

### Priority Actions
1. **Immediate**: Fix critical issues blocking user satisfaction
2. **Short-term**: Address moderate issues within 2-4 weeks
3. **Medium-term**: Implement enhancements within 1-3 months
4. **Long-term**: Maintain and evolve best practices

## Customization Guide

### Modify Dataset Size
In Cell 2, change `total_records`:
```python
total_records = 1000  # Change from 570 to desired number
```

### Adjust Rating Distribution
In Cell 2, modify `rating_distribution`:
```python
rating_distribution = {5: 0.25, 4: 0.40, 3: 0.20, 2: 0.10, 1: 0.05}
```

### Add Custom Feedback
Expand the feedback templates in Cell 2 with application-specific messages.

### Change Sentiment Threshold
In Cell 5, adjust sentiment categorization:
```python
def categorize_sentiment(score):
    if score >= 0.5:  # Increased from 0.3
        return 'Positive'
    elif score <= -0.5:
        return 'Negative'
    else:
        return 'Neutral'
```

## Troubleshooting

### ModuleNotFoundError
**Error**: `No module named 'textblob'`
**Solution**: Run `pip install -r requirements.txt` and retry.

### NLTK Data Missing
**Error**: `LookupError: Resource punkt not found`
**Solution**: Run `python -m textblob.download_corpora`

### Notebook Not Opening
**Error**: `Command not found: jupyter`
**Solution**: Run `pip install jupyter` and retry.

### Memory Issues with Large Datasets
If using >5000 records, reduce visualization sample size or increase system RAM.

## File Structure
```
application_feedback_analysis/
├── feedback_analysis.ipynb                 # Main notebook
├── requirements.txt                        # Python dependencies
├── README.md                              # This file
├── create_notebook.py                     # Script to generate notebook
├── feedback_analysis_with_sentiment.csv   # Generated export
├── summary_statistics.csv                 # Generated export
└── application_summary.csv                # Generated export
```

## Performance Metrics

Typical execution time:
- **Data generation**: 2-3 seconds
- **Sentiment analysis**: 5-10 seconds
- **Text analysis**: 3-5 seconds
- **Visualizations**: 10-15 seconds
- **Total runtime**: 20-35 seconds for 570 records

Memory usage: ~150-200 MB

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | ≥1.5.0 | Data manipulation |
| numpy | ≥1.23.0 | Numerical computing |
| matplotlib | ≥3.6.0 | Plotting and visualization |
| seaborn | ≥0.12.0 | Statistical visualization |
| plotly | ≥5.11.0 | Interactive plots |
| textblob | ≥0.17.0 | NLP and sentiment analysis |
| vaderSentiment | ≥3.3.2 | Alternative sentiment analysis |
| nltk | ≥3.8.0 | Natural language processing |
| wordcloud | ≥1.9.0 | Word cloud generation |
| scipy | ≥1.10.0 | Statistical functions |
| jupyter | ≥1.0.0 | Notebook environment |

## Use Cases

1. **User Experience Assessment**: Understand customer satisfaction with logout process
2. **Application Comparison**: Benchmark performance across different banking applications
3. **Issue Identification**: Discover and prioritize technical or UX problems
4. **Trend Analysis**: Monitor satisfaction trends over time
5. **Feature Validation**: Validate new features based on user feedback
6. **Team Alignment**: Share insights across product and engineering teams

## Future Enhancements

- Real-time feedback dashboard
- Time-series trend analysis
- Sentiment evolution tracking
- Multi-language support
- Advanced NLP (topic modeling, named entity recognition)
- A/B testing framework integration
- Automated email reports

## License

This project is provided as-is for analysis purposes.

## Support

For questions or issues:
1. Check the Troubleshooting section
2. Review the Customization Guide
3. Consult the inline comments in the notebook

## Version History

- **v1.0** (Jan 2026): Initial release with synthetic data generation, sentiment analysis, and insights

---

**Generated with Claude Code** | *Banking Application Feedback Analysis System*
