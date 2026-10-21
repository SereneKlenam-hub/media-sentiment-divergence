# Media Sentiment & Narrative Divergence

## Preliminary Results Summary

### 1. Project Objective

This project explores how selected sources frame Ghana's Operation Blackout, also known as Operation Cyber Hunt. It focuses on differences in accounts of Ghanaian leadership and the involvement of international partners, including the FBI.

### 2. Dataset

The initial dataset contains five prepared source summaries:

- Cyber Security Authority (official statement summary)
- 3News Ghana
- Citi Newsroom — FBI accounts
- Citi Newsroom — CSA response
- MyJoyOnline

The prepared dataset is saved in `Data/processed/articles_dataset.csv`.

**Limitation:** The dataset contains summaries rather than complete original articles. Several entries describe the same CSA position, so they should not be treated as five independent perspectives.

### 3. Preliminary Sentiment Results

After revising the keyword lists, the current script assigned these labels:

- Neutral: 3 sources
- Negative: 2 sources
- Positive: 0 sources

These labels are produced by comparing counts of selected positive and negative keywords. They are not validated measurements of the author's overall sentiment. The method does not reliably account for context, quotations, negation, or the difference between describing a crime and expressing a negative opinion.

The results changed after the keyword list was revised. This demonstrates that the classifications depend on the selected keywords and should be interpreted cautiously.

### 4. Preliminary Narrative Framing Results

The current keyword-based framing script classified:

- Ghana-led framing: 4 sources
- FBI/international framing: 1 source
- Cooperation or mixed framing: 0 sources

The CSA statement summary and three news summaries emphasizing the CSA's response were classified as Ghana-led framing. The Citi Newsroom summary about FBI Director Kash Patel's public account was classified as FBI/international framing.

These labels reflect the phrases recognized by the current script. They do not establish each publisher's overall position or represent the distribution of viewpoints across Ghanaian and international media.

### 5. Visualization and Output Files

The framing chart is saved at:

`Data/processed/narrative_framing_chart.png`

The analysis results are saved at:

`Data/processed/sentiment_results.csv`

The prepared dataset is saved at:

`Data/processed/articles_dataset.csv`

The chart displays the number of source summaries assigned to each narrative-framing category.

### 6. Preliminary Interpretation

The current collection contains a contrast between summaries emphasizing Ghanaian authorities' leadership and a summary placing the operation within the FBI's broader international campaign against scam centres.

Because the dataset is small, contains summaries, and includes overlapping coverage of the CSA's position, the results are best treated as a demonstration of an exploratory analysis workflow. They are not sufficient to establish broader patterns in media sentiment or narrative dominance.

### 7. Methodological Limitations

- The dataset contains only five source summaries.
- The sources are not independent in the positions they describe.
- Sentiment labels rely on manually selected keywords.
- Narrative framing depends on a limited set of exact phrases.
- The analysis does not yet validate classifications through systematic manual coding.
- Results may change when the source texts or keyword lists change.

### 8. Next Steps

1. Verify source URLs, publication dates, authors, and source types.
2. Collect additional original articles and official statements where available.
3. Refine framing categories and compare automated labels with manual review.
4. Evaluate sentiment in context rather than relying only on keyword counts.
5. Re-run the scripts and verify that the report, CSV files, and chart agree before presenting the findings.
