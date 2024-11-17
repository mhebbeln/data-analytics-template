# Identify outliers in a numeric column using the IQR method
Q1 = data['Price'].quantile(0.25)  # First quartile
Q3 = data['Price'].quantile(0.75)  # Third quartile
IQR = Q3 - Q1  # Interquartile range

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out rows with outliers
outliers = data[(data['Price'] < lower_bound) | (data['Price'] > upper_bound)]
print(f"Number of outliers: {len(outliers)}")

