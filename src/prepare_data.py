from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Folder containing our original collected data
RAW_DIR = PROJECT_DIR / "data" / "raw"

# Folder where cleaned data will be saved
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

records = []

# Read the CSA official statement
csa_file = RAW_DIR / "csa_statement.txt"

if csa_file.exists():
    text = csa_file.read_text(encoding="utf-8").strip()

    if text:
        records.append({
            "source": "Cyber Security Authority",
            "source_type": "Official Statement",
            "text": text
        })

# Read text files inside the articles folder
articles_dir = RAW_DIR / "articles"

if articles_dir.exists():
    for file_path in articles_dir.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8").strip()

        if text:
            records.append({
                "source": file_path.stem,
                "source_type": "News Article",
                "text": text
            })

# Create a dataset
df = pd.DataFrame(
    records,
    columns=["source", "source_type", "text"]
)

# Remove duplicate and empty text entries
if not df.empty:
    df = df.drop_duplicates(subset=["text"])
    df = df[df["text"].str.strip().ne("")]

# Save the prepared dataset
output_file = PROCESSED_DIR / "articles_dataset.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Sources prepared: {len(df)}")
print(f"Dataset saved to: {output_file}")

if df.empty:
    print("No text files were found. Check your raw data folder.")
else:
    print(df[["source", "source_type"]].to_string(index=False))