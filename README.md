# Media Sentiment & Narrative Divergence

## Project Overview

This project explores how selected news reports and an official statement frame Ghana's Operation Cyber Hunt, also referred to as Operation Blackout. It compares Ghana-led and FBI/international framing and applies a simple keyword-based method to classify sentiment.

This is an exploratory research project. The current analysis uses five source summaries rather than a large collection of full-text articles or public comments.

## Objectives

- Examine differences in narrative framing across selected sources.
- Apply a basic keyword-based sentiment classification method.
- Compare how sources describe Ghanaian leadership and international involvement.
- Present preliminary findings in a chart and written summary.
- Document the limitations of automated text analysis.

## Research Questions

1. How do the selected sources frame leadership of the operation?
2. What sentiment labels does the current keyword-based method assign to the collected summaries?
3. What differences appear between sources emphasizing Ghanaian leadership and those emphasizing FBI or international involvement?

## Data Sources

The current dataset contains five entries:

- Cyber Security Authority (CSA) official-statement summary.
- 3News Ghana article summary.
- Two Citi Newsroom article summaries.
- MyJoyOnline article summary, credited to Graphic Online.

The dataset is small, and some sources report the same official position. The findings should not be interpreted as representative of all Ghanaian or international media.

## Tools and Technologies

- Python
- pandas
- matplotlib
- CSV files
- Git and GitHub (for version control and project sharing)

## Methodology

1. Prepare a dataset from the collected text summaries.
2. Count selected positive and negative keywords to assign preliminary sentiment labels.
3. Count selected framing keywords to classify each entry as Ghana-led framing, FBI/international framing, or cooperation/mixed framing.
4. Save the results to CSV and create a narrative-framing chart.

The classifications are based on simple keyword matching. They do not fully capture context, sarcasm, quotations, or the difference between an article's own position and the position it reports.

## Preliminary Results

Sentiment label	        Number of sources
Neutral                           3
Negative	                      2
Positive	                      0
Total	                          5

Keep the narrative framing results as:
Framing category	                Number of sources
Ghana-led framing	                          4
FBI/international framing	                  1
Cooperation or mixed framing	              0
Total	                                      5

These are preliminary results from a small dataset of five source summaries, not full articles. The sentiment and framing labels are based on keyword counts and should not be interpreted as definitive measures of media sentiment or bias. Some sources also report similar perspectives, so they do not represent five independent viewpoints.


## Project Structure

```text
media-sentiment-divergence/
├── Data/
│   ├── raw/
│   │   ├── articles/
│   │   ├── csa_statement.txt
│   │   └── source_log.csv
│   └── processed/
│       ├── articles_dataset.csv
│       ├── sentiment_results.csv
│       └── narrative_framing_chart.png
├── docs/
│   └── results_summary.md
├── src/
│   ├── prepare_data.py
│   └── analyze_sentiment.py
├── notebooks/
├── dashboard/
└── README.md
```

## Limitations and Ethics

- The dataset currently contains only five summaries.
- Summaries are not equivalent to analyzing complete original articles.
- Some sources overlap in the position they report.
- Keyword-based sentiment labels can misclassify text.
- Framing classifications depend on the keywords selected in the script.
- Claims made by sources should be distinguished from independently verified facts.
- Source attribution and publication dates should be preserved, and source material should be used responsibly.

## Future Improvements

- Collect and verify additional original articles and official statements.
- Record source URLs, dates, authors, and source categories consistently.
- Improve and validate sentiment and framing classification.
- Analyze recurring themes and keywords by source group.
- Consider an interactive dashboard after the dataset and analysis have been strengthened.

## Current Project Status

The initial dataset preparation, keyword-based analysis, chart generation, and preliminary results summary are complete. Validation, documentation review, and GitHub publication remain part of the project workflow.
