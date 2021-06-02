import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
data = pd.read_excel('Online_Retail.xlsx')

# Stripping extra spaces in the description
data['Description'] = data['Description'].str.strip()
  
# Dropping the rows without any invoice number
data.dropna(axis = 0, subset =['InvoiceNo'], inplace = True)
data['InvoiceNo'] = data['InvoiceNo'].astype('str')
  
# Dropping all transactions which were done on credit
data = data[~data['InvoiceNo'].str.contains('C')]

# Transactions done in France
basket = (data[data['Country'] =="Germany"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

# Building the model
frq_items = apriori(basket_sets, min_support = 0.04, use_colnames = True)

# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric ="confidence", min_threshold = 0.4)
apr=rules.drop(columns=['leverage', 'antecedent support','conviction','consequent support'])
pd.set_option('display.max_colwidth', None)
apr.round(2)
print(apr[ (rules['lift'] >= 3)])
