import inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Displaying full size of a table
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.width', None)  # Disable line wrapping

# Read in the data
df = pd.read_csv(r'D:\Coursera visualisation final assignment\Portfolio\movies.csv')
# print(df)
df.fillna(0, inplace=True)  # Replace all NaN values in the entire DataFrame

# Looking for a missing data
for col in df.columns:
    percent_missing = np.mean(df[col].isnull().any())
    # print(f'{col} - {percent_missing}%')

# Data types for our columns
df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')
df['votes'] = df['votes'].astype('int64')
df['yearcorrect'] = df['released'].str.extract(r'(\d{4})')

df = df.sort_values(by='gross', inplace=False, ascending=False)

# Drop any duplicates
df['company'] = df['company'].astype(str).drop_duplicates().sort_values(ascending=False)
# print(df.head())

# Scutter plot with budget vs gross
plt.scatter(x=df['budget'], y=df['gross'])

plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')

# Plot budget vs gross using seaborn
sns.regplot(x='budget', y='gross', data=df, scatter_kws={"color": "green"}, line_kws={"color": "blue"})

#Correlation matrix

numeric_df = df.select_dtypes(include=[np.number])

# Calculate correlation(Pearson, Kendall, Spearman)
correlation_matrix = numeric_df.corr(method='pearson')  # High correlation between budget and gross
# print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True)

plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

# Creating ALL correlations

df_numerized = df

for col_name in df_numerized.columns:
    if df_numerized[col_name].dtype == 'object':
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
# print(df_numerized)

correlation_mat = df_numerized.corr(method='pearson')  # High correlation between budget and gross
corr_pairs = correlation_mat.unstack()
sorted_pairs = corr_pairs.sort_values()
high_corr = sorted_pairs[(sorted_pairs) > 0.5]
# print(correlation_matrix)
print(high_corr)

'''
    Votes and budget have the highest correlation to gross earnings
    Company has Low correlation 
'''

sns.heatmap(correlation_matrix, annot=True)

plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

plt.show()