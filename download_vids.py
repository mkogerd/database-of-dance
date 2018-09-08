import fetch_vid
import pandas as pd
import numpy as np

df = pd.read_csv('moveList.csv')

#df["Title"] = "empty"

# Add Empty row for title
if 'Title' not in df.columns:
	df["Title"] = "empty"

# Iterate through rows to modify values
for i, row in df.iterrows():
	print(row['Title'])
	if(row['Title'] == "empty"):
		row['Title'] = fetch_vid.get_video(row['Video'], 'static/vid/')
		# Export to new .csv (every itteration in case program crashes)
		df.to_csv('moveList.csv', index=False)

	