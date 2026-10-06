#!/usr/bin/env python3
"""
Run the feedback analysis without visualization (headless mode)
"""

import pandas as pd
import numpy as np
import random
from collections import Counter
from datetime import datetime, timedelta
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import warnings
warnings.filterwarnings('ignore')

# Set seeds for reproducibility
random.seed(42)
np.random.seed(42)

# Download NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('vader_lexicon', quiet=True)

print('=' * 80)
print('BANKING APPLICATION LOGOUT FEEDBACK ANALYSIS')
print('=' * 80)

# ============================================================================
# CELL 1: SYNTHETIC DATASET GENERATION
# ============================================================================

feedback_5_star = {
    'Collections': [
        'Excellent logout process! Payment confirmation was instant and clear.',
        'Very smooth experience. Quick logout and immediate receipt download.',
        'Outstanding! Session ended securely without any hassle.'
    ],
    'Payments': [
        'Fantastic! Transaction status was instant and logout was smooth.',
        'Excellent security and quick logout process.',
        'Very impressed! Fast transaction processing and secure logout.'
    ],
    'Customer Service Center': [
        'Excellent support! Chat history saved perfectly before logout.',
        'Outstanding! Ticket status remained intact after logout.',
        'Perfect experience! All support tickets visible and logout smooth.'
    ]
}

feedback_4_star = {
    'Collections': [
        'Good logout experience. Payment confirmation took a moment to appear.',
        'Very good! Receipt download works well after logout.',
        'Satisfied! Logout process is quick and secure.'
    ],
    'Payments': [
        'Good! Transaction status visible but could update faster.',
        'Very good security features and reasonable logout speed.',
        'Satisfied with the transaction processing.'
    ],
    'Customer Service Center': [
        'Good! Chat history saved but took a moment to load.',
        'Satisfied! Ticket status preserved after logout.',
        'Very good support experience overall.'
    ]
}

feedback_3_star = {
    'Collections': [
        'Average logout experience. Sometimes slow, sometimes fast.',
        'Okay. Payment confirmation works but could be faster.',
        'Acceptable. Nothing special but no major issues.'
    ],
    'Payments': [
        'Average! Transaction updates could be faster.',
        'Okay experience. Security is good, speed could improve.',
        'Fair! Works most of the time but occasional hiccups.'
    ],
    'Customer Service Center': [
        'Average support experience. Response times could be better.',
        'Okay! Chat history works but loading is slow.',
        'Fair experience. Support quality is standard.'
    ]
}

feedback_2_star = {
    'Collections': [
        'Frustrated! Payment confirmation never appeared after logout.',
        'Poor experience. Receipt download is extremely slow.',
        'Disappointed! Session timed out before payment confirmation.'
    ],
    'Payments': [
        'Poor! Transaction status does not update after logout.',
        'Frustrated! Security verification takes too long.',
        'Bad experience. Transaction processing is slow.'
    ],
    'Customer Service Center': [
        'Poor! Chat history lost after logout.',
        'Frustrated! Ticket status not preserved after logout.',
        'Bad experience. Support staff unhelpful.'
    ]
}

feedback_1_star = {
    'Collections': [
        'Terrible! Lost payment confirmation after logout. Very concerning.',
        'Awful experience! Cannot retrieve receipt after session ends.',
        'Extremely frustrated! Payment status vanished after logout.'
    ],
    'Payments': [
        'Terrible! Transaction completely disappeared after logout.',
        'Awful! Security verification failed during logout.',
        'Worst experience! Cannot verify payment after logout.'
    ],
    'Customer Service Center': [
        'Terrible! Entire chat history deleted after logout.',
        'Awful! Cannot access ticket after logout.',
        'Worst support experience ever!'
    ]
}

feedback_templates = {5: feedback_5_star, 4: feedback_4_star, 3: feedback_3_star, 2: feedback_2_star, 1: feedback_1_star}
applications = ['Collections', 'Payments', 'Customer Service Center']

records = []
rating_distribution = {5: 0.30, 4: 0.35, 3: 0.20, 2: 0.10, 1: 0.05}
total_records = 570
records_per_app = total_records // 3

for app in applications:
    for rating in [5, 4, 3, 2, 1]:
        count = int(records_per_app * rating_distribution[rating])
        feedback_list = feedback_templates[rating][app]
        for _ in range(count):
            feedback = random.choice(feedback_list)
            records.append({'application_name': app, 'rating': rating, 'feedback': feedback})

df = pd.DataFrame(records)
df = df.sample(frac=1).reset_index(drop=True)

print('\n✓ Dataset generated successfully!')
print(f'Total records: {len(df)}')
print(f'Records per application: {len(df) // 3}')

# ============================================================================
# CELL 2: DATA OVERVIEW
# ============================================================================

print('\n' + '=' * 80)
print('DATASET OVERVIEW')
print('=' * 80)
print(f'Dataset Shape: {df.shape}')
print(f'\nFirst 5 records:')
print(df.head())
print(f'\nData Types:')
print(df.dtypes)
print(f'\nMissing Values:')
print(df.isnull().sum())
print(f'\nBasic Statistics - Rating:')
print(df['rating'].describe())
print(f'\nApplication Distribution:')
print(df['application_name'].value_counts())
print(f'\nRating Distribution:')
print(df['rating'].value_counts().sort_index(ascending=False))

# ============================================================================
# CELL 3: SENTIMENT ANALYSIS
# ============================================================================

sia = SentimentIntensityAnalyzer()
print('\n\nCalculating sentiment scores...')

df['sentiment_textblob'] = df['feedback'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['sentiment_vader'] = df['feedback'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment_score'] = (df['sentiment_textblob'] + df['sentiment_vader']) / 2

def categorize_sentiment(score):
    if score >= 0.3:
        return 'Positive'
    elif score <= -0.3:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment_category'] = df['sentiment_score'].apply(categorize_sentiment)

print('✓ Sentiment scores calculated successfully!')
print(f'\nSentiment Score Statistics:')
print(df['sentiment_score'].describe().round(3))
print(f'\nSentiment Category Distribution:')
print(df['sentiment_category'].value_counts())

# ============================================================================
# CELL 4: SENTIMENT BY APPLICATION
# ============================================================================

print('\n' + '=' * 80)
print('SENTIMENT BY APPLICATION:')
print('=' * 80)
print(pd.crosstab(df['application_name'], df['sentiment_category']))

# ============================================================================
# CELL 5: TEXT ANALYSIS & KEYWORDS
# ============================================================================

stop_words = set(stopwords.words('english'))

def extract_keywords(text):
    words = word_tokenize(text.lower())
    keywords = [word for word in words if word.isalpha() and word not in stop_words and len(word) > 3]
    return keywords

print('\n\nExtracting keywords...')
all_keywords = []
for feedback in df['feedback']:
    all_keywords.extend(extract_keywords(feedback))

keyword_freq = Counter(all_keywords)
top_keywords = dict(keyword_freq.most_common(20))

print('\n' + '=' * 80)
print('TOP 20 KEYWORDS ACROSS ALL FEEDBACK')
print('=' * 80)
for keyword, count in top_keywords.items():
    print(f'{keyword:20} : {count:3d} occurrences')

# Top keywords by application
print('\n' + '=' * 80)
print('TOP 10 KEYWORDS BY APPLICATION')
print('=' * 80)
for app in applications:
    app_keywords = []
    for feedback in df[df['application_name'] == app]['feedback']:
        app_keywords.extend(extract_keywords(feedback))

    app_keyword_freq = Counter(app_keywords)
    top_app_keywords = dict(app_keyword_freq.most_common(10))

    print(f'\n{app}:')
    for keyword, count in top_app_keywords.items():
        print(f'  {keyword:20} : {count:3d}')

# ============================================================================
# CELL 6: ISSUE IDENTIFICATION & SATISFACTION DRIVERS
# ============================================================================

print('\n' + '=' * 80)
print('ISSUE IDENTIFICATION & SATISFACTION DRIVERS')
print('=' * 80)

low_rated = df[df['rating'] <= 2][['application_name', 'rating', 'feedback']]
print(f'Low-Rated Feedback (1-2 stars) - Count: {len(low_rated)}')

for app in applications:
    app_issues = low_rated[low_rated['application_name'] == app]
    print(f'{app}: {len(app_issues)} issues')

high_rated = df[df['rating'] >= 4][['application_name', 'rating', 'feedback']]
print(f'\nHigh-Rated Feedback (4-5 stars) - Count: {len(high_rated)}')

for app in applications:
    app_drivers = high_rated[high_rated['application_name'] == app]
    print(f'{app}: {len(app_drivers)} satisfied users')

print('\n' + '=' * 80)
print('SATISFACTION BY APPLICATION')
print('=' * 80)

for app in applications:
    app_data = df[df['application_name'] == app]

    issue_count = len(app_data[app_data['rating'] <= 2])
    neutral_count = len(app_data[(app_data['rating'] == 3)])
    satisfied_count = len(app_data[app_data['rating'] >= 4])

    print(f'\n{app}:')
    print(f'  Issues (1-2 stars): {issue_count}')
    print(f'  Neutral (3 stars): {neutral_count}')
    print(f'  Satisfied (4-5 stars): {satisfied_count}')

# ============================================================================
# CELL 7: EXECUTIVE SUMMARY & KPIs
# ============================================================================

print('\n' + '=' * 80)
print('EXECUTIVE SUMMARY - BANKING APPLICATION LOGOUT FEEDBACK ANALYSIS')
print('=' * 80)

overall_satisfaction = len(df[df['rating'] >= 4]) / len(df) * 100
overall_issues = len(df[df['rating'] <= 2]) / len(df) * 100
overall_avg_rating = df['rating'].mean()
overall_avg_sentiment = df['sentiment_score'].mean()
correlation = df['rating'].corr(df['sentiment_score'])

print(f'Total Records Analyzed: {len(df)}')
print(f'Overall Average Rating: {overall_avg_rating:.2f} / 5.00')
print(f'Overall Average Sentiment: {overall_avg_sentiment:.3f}')
print(f'Customer Satisfaction Rate (4-5 stars): {overall_satisfaction:.1f}%')
print(f'Issue Rate (1-2 stars): {overall_issues:.1f}%')
print(f'Positive Sentiment: {(len(df[df["sentiment_category"] == "Positive"]) / len(df) * 100):.1f}%')
print(f'Negative Sentiment: {(len(df[df["sentiment_category"] == "Negative"]) / len(df) * 100):.1f}%')
print(f'Rating-Sentiment Correlation: {correlation:.3f}')

print(f'\nAPPLICATION PERFORMANCE:')
print('=' * 80)

for app in sorted(applications, key=lambda x: df[df['application_name']==x]['rating'].mean(), reverse=True):
    app_data = df[df['application_name'] == app]
    rating = app_data['rating'].mean()
    satisfaction = len(app_data[app_data['rating'] >= 4]) / len(app_data) * 100
    sentiment = app_data['sentiment_score'].mean()
    print(f'{app:30} | Rating: {rating:.2f}/5 | Satisfaction: {satisfaction:.1f}% | Sentiment: {sentiment:.3f}')

print(f'\nKEY FINDINGS:')
print('=' * 80)
print(f'1. Overall customer satisfaction is at {overall_satisfaction:.1f}%')
print(f'2. {overall_issues:.1f}% of users reported issues (1-2 stars)')
print(f'3. Sentiment analysis shows {(len(df[df["sentiment_category"] == "Positive"]) / len(df) * 100):.1f}% positive feedback')
print(f'4. Rating-sentiment correlation is {correlation:.3f} (strong alignment)')

print(f'\nRECOMMENDATIONS:')
print('=' * 80)
if overall_avg_rating >= 3.8:
    print('✓ Good performance. Maintain quality and monitor for improvements.')
elif overall_avg_rating >= 3.2:
    print('⚠ Fair performance. Address identified issues within 2-4 weeks.')
else:
    print('✗ Critical issues. Implement immediate action plan.')

print(f'\nReport Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
print('=' * 80)

# ============================================================================
# CELL 8: DATA EXPORT
# ============================================================================

print('\n\nExporting results...')

df_export = df[['application_name', 'rating', 'feedback', 'sentiment_score', 'sentiment_category']].copy()
df_export.to_csv('feedback_analysis_with_sentiment.csv', index=False)
print('✓ Processed dataset exported to feedback_analysis_with_sentiment.csv')

summary_stats = {
    'Metric': ['Total Records', 'Average Rating', 'Average Sentiment', 'Satisfaction Rate', 'Issue Rate'],
    'Value': [len(df), f'{df["rating"].mean():.2f}', f'{df["sentiment_score"].mean():.3f}',
              f'{(len(df[df["rating"] >= 4]) / len(df) * 100):.1f}%', f'{overall_issues:.1f}%']
}

summary_df = pd.DataFrame(summary_stats)
summary_df.to_csv('summary_statistics.csv', index=False)
print('✓ Summary statistics exported to summary_statistics.csv')

# Application summary
app_summary_stats = []
for app in applications:
    app_data = df[df['application_name'] == app]
    app_summary_stats.append({
        'Application': app,
        'Total Records': len(app_data),
        'Average Rating': f'{app_data["rating"].mean():.2f}',
        'Satisfaction Rate': f'{(len(app_data[app_data["rating"] >= 4]) / len(app_data) * 100):.1f}%',
        'Average Sentiment': f'{app_data["sentiment_score"].mean():.3f}',
        'Positive Sentiment %': f'{(len(app_data[app_data["sentiment_category"] == "Positive"]) / len(app_data) * 100):.1f}%'
    })

app_summary_df = pd.DataFrame(app_summary_stats)
app_summary_df.to_csv('application_summary.csv', index=False)
print('✓ Application summary exported to application_summary.csv')

print(f'\n✓ All exports completed successfully!')
print('\n' + '=' * 80)
print('ANALYSIS COMPLETE!')
print('=' * 80)
