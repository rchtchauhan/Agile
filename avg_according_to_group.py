import pandas as pd

# read the two sheets into dataframes
sheet1 = pd.read_csv('input-sheet1.csv')
sheet2 = pd.read_csv('input-sheet2.csv')

# merge the two sheets on the User ID and uid columns
merged = pd.merge(sheet1, sheet2, left_on='User ID', right_on='uid')

# group the merged data by Team Name and calculate the average statements and reasons
team_stats = merged.groupby('Team Name')[['total_statements', 'total_reasons']].mean()
team_stats = team_stats.sort_values('total_statements', ascending=False)

# print the results
print(team_stats)
