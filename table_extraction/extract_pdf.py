import camelot

tables = camelot.read_pdf('/docs/automationcs.pdf', pages='1', flavor='lattice')
print(tables)


# to a csv file
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')  

# to a df
print(tables[0].df) 