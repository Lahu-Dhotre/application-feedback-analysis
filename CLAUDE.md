# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Banking Application Logout Feedback Analysis** - A Jupyter notebook-based analytical system for analyzing user feedback on logout experience across 100 banking applications.

The project is a **Jupyter notebook environment** focused on data analysis, not a traditional code repository. The primary deliverable is an interactive analysis notebook that generates synthetic data for 100 distinct banking applications, performs sentiment analysis, and produces visualizations and CSV exports.

## Key Concepts & Architecture

### Analysis Pipeline Flow

The notebook follows a sequential analysis pipeline:

```
Synthetic Data Generation → Statistical Analysis → Sentiment Analysis
  → Text Mining → Visualizations → Insights & Recommendations → CSV Export
```

- **Cell 1-3**: Setup, data generation, and overview
- **Cell 4-5**: Statistical and sentiment analysis
- **Cell 6-8**: Visualizations (distributions, word clouds, scatter plots)
- **Cell 9-11**: Issue/driver identification, executive summary, CSV export

### 100 Banking Applications

Analysis is stratified across 100 dynamically generated banking applications created from combinations of:
- **10 Bank Types**: Bank, Credit Union, Trust, Capital, Financial, Savings, Investment, Commerce, Exchange, Lending
- **10 Regions**: National, State, Regional, Global, Federal, International, Local, Central, Digital, Online
- **10 Services**: Services, Group, Corp, Solutions, Partners, Platform, Network, System, Hub, Gateway

Each application generates a unique name (e.g., "Bank Digital Services", "Credit Union Global Platform") with application-agnostic feedback templates tied to rating levels (1-5 stars).

### Synthetic Data Structure

The dataset is procedurally generated with realistic constraints:
- **5,400 records** (54 per application, evenly distributed across 100 apps)
- **Rating distribution**: 30% 5-star, 35% 4-star, 20% 3-star, 10% 2-star, 5% 1-star
- **Feedback**: Application-agnostic templates randomly selected for each rating level
- **Reproducible**: Uses `random.seed(42)` for consistent results
- **Current metrics**: Avg rating 3.81/5, Satisfaction 66.7%, Sentiment correlation 0.805

### Dual Sentiment Scoring

Sentiment analysis combines two methods for robustness:
- **TextBlob**: Polarity scoring (-1 to +1)
- **VADER**: Compound scoring specialized for social media/informal text
- **Final score**: Average of both methods
- **Categories**: Positive (≥0.3), Neutral (-0.3 to 0.3), Negative (≤-0.3)

## Common Development Tasks

### Run the Complete Analysis

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download NLTK/TextBlob data (one-time)
python -m textblob.download_corpora

# 3. Launch notebook and run all cells
jupyter notebook feedback_analysis.ipynb
# Then: Kernel → Restart & Run All
```

### Regenerate the Notebook

If `feedback_analysis.ipynb` is corrupted or needs regeneration:

```bash
python create_notebook.py
```

This recreates the entire notebook from the JSON cell definitions in `create_notebook.py`.

### Export Analysis Results

The notebook automatically exports three CSV files when Cell 11 runs:

```
feedback_analysis_with_sentiment.csv  # Full dataset with sentiment scores
summary_statistics.csv                # Key metrics (avg rating, satisfaction %)
application_summary.csv               # Per-application performance stats
```

These are generated in the notebook's working directory.

### Modify Dataset Parameters

Edit **Cell 2** in the notebook to customize:

- **Dataset size**: Change `total_records = 5700` to desired number (note: currently scales to 5400 due to app count)
- **Application count**: Modify loop limits in `while len(applications) < 100:` to generate different numbers of apps
- **Rating distribution**: Adjust `rating_distribution = {5: 0.30, ...}`
- **Feedback templates**: Expand/replace feedback text in `feedback_*_star` lists (currently application-agnostic)
- **Application name generation**: Customize `application_types`, `regions`, or `services` lists for different naming patterns

### Adjust Sentiment Thresholds

Edit **Cell 5** `categorize_sentiment()` function to change polarity boundaries:

```python
def categorize_sentiment(score):
    if score >= 0.5:      # Changed from 0.3
        return 'Positive'
    elif score <= -0.5:   # Changed from -0.3
        return 'Negative'
    else:
        return 'Neutral'
```

### Customize Visualizations

Edit individual cell code to modify:
- Chart colors (matplotlib color maps): `color='steelblue'`, `cmap='RdYlGn'`
- Figure sizes: `plt.figure(figsize=(14, 10))`
- Bin counts: `bins=30` in histograms
- Font sizes: `fontsize=12`

## Architecture Patterns

### Feedback Template Organization

Feedback is now organized by rating level only (application-agnostic):

```python
feedback_5_star = [
    'Excellent logout process! All features worked perfectly...',
    'Very smooth experience. Quick logout and data preserved...',
    ...
]
# Repeated for feedback_4_star, feedback_3_star, feedback_2_star, feedback_1_star

# Combined into:
feedback_templates = {5: feedback_5_star, 4: feedback_4_star, ...}

# Applied to all 100 dynamically generated applications
for app in applications:
    for rating in [5, 4, 3, 2, 1]:
        feedback = random.choice(feedback_templates[rating])
        # Add to records with app name
```

### Data Processing Chain

```python
1. Generate records list from feedback templates
2. Create DataFrame from records
3. Shuffle with .sample(frac=1)
4. Add sentiment scores (TextBlob + VADER)
5. Categorize sentiment (Positive/Neutral/Negative)
6. Export to CSV
```

### Visualization Pattern

Most visualizations follow:
```python
fig, axes = plt.subplots(rows, cols, figsize=...)
# Plot 1: axes[row, col].plot/bar/scatter/...
# Plot 2: axes[row, col].plot/bar/scatter/...
plt.tight_layout()
plt.show()
```

## Dependency Management

**Critical dependencies** (no suitable alternatives):
- **pandas**: Core data manipulation
- **matplotlib/seaborn**: Visualization backbone
- **textblob/vaderSentiment**: Dual sentiment analysis approach
- **nltk**: Text tokenization and stopword filtering
- **wordcloud**: Word frequency visualization

**Installation troubleshooting**:
- Missing NLTK data: `python -m textblob.download_corpora`
- Jupyter not found: `pip install jupyter ipykernel`
- Memory issues with large datasets: Reduce to <5000 records or increase RAM

## File Structure & Responsibilities

```
feedback_analysis.ipynb        # Primary deliverable - 11 cells of analysis
create_notebook.py             # Generates/regenerates notebook from JSON
requirements.txt               # Pin-based dependencies (pandas>=1.5.0, etc.)
README.md                      # User-facing documentation
SETUP_GUIDE.txt               # Quick start guide
CLAUDE.md                      # This file
```

**DO NOT modify**:
- `create_notebook.py` structure unless regenerating entire notebook
- Column names in generated CSVs (expected by downstream analysis)

## Performance Characteristics

- **Runtime**: ~120-150 seconds for 5,400 records (54 per app × 100 apps) on modern hardware
- **Memory**: ~600-800 MB for current 5,400 record dataset
- **Bottleneck**: Sentiment analysis (VADER is slower than TextBlob) and keyword extraction across large dataset
- **Scaling**: Scales linearly up to 10,000 records; beyond requires optimization or chunking of analysis
- **Note**: Visualizations are optimized to show top 5-10 apps rather than all 100 to avoid overcrowding

## Key Metrics & Interpretation

### Rating-Based KPIs
- **Satisfaction Rate**: % of 4-5 star ratings (target: >70%)
- **Issue Rate**: % of 1-2 star ratings (target: <15%)
- **Average Rating**: Overall 1-5 score (target: >3.8)

### Sentiment-Based KPIs
- **Sentiment Score**: -1 to +1 polarity (target: >0.4)
- **Positive %**: Feedback with score ≥0.3 (target: >70%)
- **Correlation**: Rating-sentiment alignment (expect >0.7)

### Application-Specific Comparison
All 100 applications are independently ranked and analyzed in CSV exports:
- **Individual app metrics**: Rating, satisfaction rate, sentiment score, record count
- **Top 10 apps visualization**: Displayed in Cell 18 for satisfaction comparison
- **Top 5 apps keywords**: Keyword analysis shown for representative apps to avoid overcrowding
- **Aggregate analysis**: Overall metrics across all 100 apps for executive summary
- **CSV details**: application_summary.csv contains full stats for all 100 applications

## Testing & Validation

**Manual validation steps**:
1. Run full notebook (Cell 1-11) without errors
2. Verify 5,400 records generated across 100 applications (~54 per app)
3. Check sentiment scores fall in [-1, +1] range
4. Validate CSV exports have expected columns (application_name, rating, feedback, sentiment_score, sentiment_category)
5. Confirm visualizations render without warnings (especially top 5/10 app comparisons)
6. Check keyword frequency counts sum correctly
7. Verify application_summary.csv contains exactly 100 rows (plus header)

**Expected outputs**:
- ✓ Sentiment correlation > 0.7 (currently ~0.805)
- ✓ Satisfaction rate 60-70% (currently 66.7%)
- ✓ All 100 applications present in application_summary.csv
- ✓ All KPI metrics match across CSV and console output
- ✓ Word clouds generate without "font not found" errors
- ✓ Average rating ~3.8 (currently 3.81)

## Modification Safety Checklist

When extending or modifying:

- [ ] Don't change column names in DataFrames (affects downstream aggregation)
- [ ] Preserve the `random.seed(42)` for reproducibility
- [ ] Test sentiment categorization with edge cases (score exactly 0.3, -0.3)
- [ ] When adding feedback templates, ensure they're in lists (application-agnostic) not dicts
- [ ] When modifying app name generation, ensure uniqueness check `if app_name not in name_set`
- [ ] Ensure new visualizations show top N apps (not all 100) to avoid overcrowding
- [ ] Check CSV exports have headers matching expectations
- [ ] Verify application_summary.csv row count matches number of applications generated

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'textblob'` | `pip install -r requirements.txt` |
| `LookupError: Resource punkt not found` | `python -m textblob.download_corpora` |
| Sentiment scores all 0 | Check VADER lexicon downloaded, verify text tokenization |
| Word clouds blank | Ensure feedback text is non-empty, check stopword filtering |
| Keyword analysis crashes | Cell 14 now shows top 5 apps instead of hardcoded 3, handles 100 apps |
| Memory issues with 5400 records | Reduce total_records or increase available RAM to 2GB+ |
| Visualizations don't appear in notebook | Ensure `%matplotlib inline` (handled in Cell 1 implicitly) |
| CSV not generated | Verify Cell 22 runs without errors, check working directory |
| application_summary.csv has fewer than 100 rows | Check that app name generation loop completes and creates unique names |

## Future Enhancement Considerations

Current scope is **static analysis** of synthetic data. Potential extensions:

- **Real data integration**: Replace synthetic generation with actual feedback CSV
- **Time-series analysis**: Add timestamp column for trend tracking
- **Topic modeling**: Use LDA instead of simple keyword extraction
- **Interactive dashboard**: Convert notebook to Streamlit/Dash app
- **Multi-language**: Add translation pipeline before sentiment analysis

Keep modifications **within the notebook cell structure** unless refactoring to different framework.
