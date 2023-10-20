import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('nba.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Get basic statistics about the data
print(df.describe())

# Filter rows based on a condition
filtered_df = df[df['column_name'] > 50]

# Sort the DataFrame by a specific column
sorted_df = df.sort_values(by='column_name', ascending=False)

# Group data by a column and perform an aggregation
grouped_data = df.groupby('category_column')['value_column'].mean()

# Save the modified DataFrame back to a CSV file
filtered_df.to_csv('filtered_file.csv', index=False)

# Access specific columns or rows
column_data = df['column_name']
row_data = df.loc[0]  # Access the first row

# Iterate through rows
for index, row in df.iterrows():
    print(f'Row {index}: {row}')

# Create a new column based on existing columns
df['new_column'] = df['column_a'] + df['column_b']

# Drop a column from the DataFrame
df = df.drop('column_to_drop', axis=1)

# Replace missing values (NaN) with a specific value
df['column_name'].fillna(0, inplace=True)

# Save the DataFrame to a new CSV file
df.to_csv('new_file.csv', index=False)
