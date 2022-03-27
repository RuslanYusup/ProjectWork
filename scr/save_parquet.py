def write_parquet_file():
	df = pd.read_csv("name_file.csv")
	df.to_parquet("name_file.csv")
	