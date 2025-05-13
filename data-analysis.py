# Basic statistics
print("\n Descriptive Statistics:")
print(df.describe())

# Grouping: average measurements per species
grouped = df.groupby('species').mean()
print("\n Mean values grouped by species:")
print(grouped)

