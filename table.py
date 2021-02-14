import os
import pandas as pd

# Read CSV into DataFrame
file_path = "Resources/cities.csv"
cities_df = pd.read_csv(file_path)

# Convert DF to HTML table
cities_df.to_html('just_table.html', classes='table', index=False)
