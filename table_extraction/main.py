import pandas as pd

# Read and save/print tables from webpages
tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_South_Park_episodes')

# Prints length of the tables, should corespond to how many seasons per series
# utilizing southpark for testing purposes
print(len(tables))

# Save Each table starting at season 1 in it's own csv file
for idx, table in enumerate(tables[1:]):
    table.to_csv('./csv/season' + str(idx + 1) + '.csv' )

