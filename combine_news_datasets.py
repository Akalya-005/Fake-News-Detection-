import pandas as pd

# Load both datasets
true_df = pd.read_csv("True.csv")
fake_df = pd.read_csv("Fake.csv")

# Add label columns
true_df['label'] = 'REAL'
fake_df['label'] = 'FAKE'

# Combine both into one dataset
combined_df = pd.concat([true_df, fake_df], ignore_index=True)

# Shuffle the rows
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to a new file
combined_df.to_csv("news_dataset.csv", index=False)

print("✅ news_dataset.csv created successfully!")
