import pandas as pd

# Read in the data from both sheets
sheet1 = pd.read_excel('data.xlsx', sheet_name='Sheet1')
sheet2 = pd.read_excel('data.xlsx', sheet_name='Sheet2')

# Merge the two sheets on the UID column
merged = pd.merge(sheet1, sheet2, on='UID')

# Group by name and UID and calculate the average number of statements and reasons
grouped = merged.groupby(['Name', 'UID'], as_index=False).agg({'Total Statements': 'mean', 'Total Reasons': 'mean'})

# Sort the data by number of statements (descending), then by number of reasons (descending), then by name (ascending)
sorted_data = grouped.sort_values(['Total Statements', 'Total Reasons', 'Name'], ascending=[False, False, True])

# Add a rank column
sorted_data['Rank'] = sorted_data.reset_index().index + 1

the final output
print(sorted_data)
