
from pathlib import Path
import pandas as pd

# Locate the project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "data" / "processed" / "articles_dataset.csv"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

# Load the prepared dataset
df = pd.read_csv(INPUT_FILE)

# Check that the required column exists
if "text" not in df.columns:
    raise ValueError("The dataset must contain a 'text' column.")

# Define simple keyword-based sentiment indicators
positive_words = [
    "success", "successful", "protect",
    "cooperation", "progress"
]

negative_words = [
    "dispute", "reject", "challenged"
]

def count_words(text, word_list):
    text = str(text).lower()
    return sum(text.count(word) for word in word_list)

# Calculate keyword counts for each source
df["positive_keyword_count"] = df["text"].apply(
    lambda text: count_words(text, positive_words)
)

df["negative_keyword_count"] = df["text"].apply(
    lambda text: count_words(text, negative_words)
)

# Assign a preliminary label based on keyword counts
def label_sentiment(row):
    positive = row["positive_keyword_count"]
    negative = row["negative_keyword_count"]

    if positive > negative:
        return "Positive"
    elif negative > positive:
        return "Negative"
    return "Neutral"

df["sentiment_label"] = df.apply(label_sentiment, axis=1)

# Save the results
output_file = OUTPUT_DIR / "sentiment_results.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("Sentiment analysis completed!")
print(f"Sources analyzed: {len(df)}")
print(f"Results saved to: {output_file}")
print("\nSentiment labels:")
print(df[["source", "sentiment_label"]].to_string(index=False))

# Narrative framing analysis

def identify_framing(text):
    text = str(text).lower()

    ghana_keywords = [
        "ghanaian authorities",
        "ghana-led",
        "ghana's leadership",
        "planned, coordinated and executed",
        "ghana's sovereignty"
    ]

    fbi_keywords = [
        "fbi's wider campaign",
        "fbi campaign",
        "global scam-centre crackdown",
        "international campaign"
    ]

    ghana_count = sum(text.count(word) for word in ghana_keywords)
    fbi_count = sum(text.count(word) for word in fbi_keywords)

    if ghana_count > fbi_count:
        return "Ghana-led framing"
    elif fbi_count > ghana_count:
        return "FBI/international framing"
    else:
        return "Cooperation or mixed framing"


df["narrative_framing"] = df["text"].apply(identify_framing)

# Save the updated results
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("\nNarrative framing results:")
print(df[["source", "narrative_framing"]].to_string(index=False))
print(f"\nUpdated results saved to: {output_file}")

import matplotlib.pyplot as plt

# Count sources in each narrative framing category
framing_counts = df["narrative_framing"].value_counts()

# Create a bar chart
framing_counts.plot(kind="bar")

plt.title("Narrative Framing of Operation Blackout")
plt.xlabel("Narrative Framing")
plt.ylabel("Number of Sources")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()

# Save the chart
chart_file = OUTPUT_DIR / "narrative_framing_chart.png"
plt.savefig(chart_file, dpi=300)
plt.show()

print(f"\nChart saved to: {chart_file}")
