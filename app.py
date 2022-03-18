import pandas as pd
from datetime import datetime
import os
import glob

# Set variables for later filenaming
agent_name = "uribe_ana_"
print(agent_name)

# Source: https://softhints.com/how-to-merge-multiple-csv-files-with-python/
# All files have the same number of columns and identical information inside

path = 'csv/files-to-combine/'

# Match CSV files by pattern
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
print(all_files)

# Combine all files in the list and export as CSV
df_merged = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv(f"csv/combined-files/{agent_name}merged.csv", index=False)
