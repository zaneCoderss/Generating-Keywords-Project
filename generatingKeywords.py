from pprint import pprint
import pandas as pd


# List of words to pair with products
words = ["cheap", "discount", "sale", "promo", "buy", "price"]

# Print list of words
print(words)

products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        #keywords_list.append([product, product + ' ' + word])

# Inspect keyword list
pprint(keywords_list)

# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it
keywords_df.head()

# Rename the columns of the DataFrame
keywords_df.rename(columns={0: "Ad Group", 1: "Keyword"}, inplace=True)
keywords_df['Campaign'] = "SEM_Sofas"
keywords_df['Criterion Type'] = 'Exact'

keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase['Criterion Type'] = 'Phrase'

# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)

# Save the final keywords to a CSV file
keywords_df_final.to_csv('keywords.csv', index=False)
# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
