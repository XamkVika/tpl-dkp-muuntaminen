import pandas as pd
from data_transform.transform import clean_dataframe


def main():
	file_path = "data/countries_noisy.json"

	# Read JSON file content to a dataframe
	data = pd.read_json(file_path)

	# Show the first 10 rows to understand the data
	print("Original data sample:")
	print(data.head(10))
	print(f"\nTotal rows before cleaning: {len(data)}")

	cleaned = clean_dataframe(data, save_path="data/cleaned_countries.csv")

	print("\nAfter cleaning operations:")
	print(cleaned.head(10))
	print(f"\nTotal rows after cleaning: {len(cleaned)}")


if __name__ == "__main__":
	main()
