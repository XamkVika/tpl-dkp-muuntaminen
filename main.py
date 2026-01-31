import pandas as pd

file_path = "data/countries_noisy.json"
# Read JSON file content to a dataframe
data = pd.read_json(file_path)

# Show the first 10 rows to understand the data
print("Original data sample:")
print(data.head(10))
print(f"\nTotal rows before cleaning: {len(data)}")

# -----------------------------------------------------------
# 1. String / Text Cleaning
# -----------------------------------------------------------
# TODO:
# Use pandas .str methods to clean 'name' and 'capital' columns:
# - Strip spaces
# - Convert to title case
# - Optionally remove unwanted characters (like @, digits, etc.)

# -----------------------------------------------------------
# 2. Handling Missing Data
# -----------------------------------------------------------
# TODO:
# Replace "N/A" entries with NaN using replace()
# Print how many missing values exist per column
# Remove rows where 'capital' is missing

# -----------------------------------------------------------
# 3. Removing Duplicates
# -----------------------------------------------------------
# TODO:
# Identify and remove duplicates based on 'name' (case-insensitive)

# -----------------------------------------------------------
# 4. Fixing Data Formats and Inconsistencies
# -----------------------------------------------------------
# TODO:
# Convert columns to proper types and sort alphabetically by 'name'

# -----------------------------------------------------------
# 5. Save cleaned version to a separate file
# -----------------------------------------------------------
# TODO:
# Save the cleaned DataFrame to a new file (data/cleaned_countries.csv)

# -----------------------------------------------------------
# Print final overview
# -----------------------------------------------------------
print("\nAfter cleaning operations:")
print(data.head(10))
print(f"\nTotal rows after cleaning: {len(data)}")
