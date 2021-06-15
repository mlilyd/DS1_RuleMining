"""
# Data Science 1 Project: Rule Mining
by Seida Basha
"""
from datasets import *
from rules import save_results, load_results
from mlxtend.frequent_patterns import apriori, association_rules

# Building the model
frq_items = apriori(retail_dataset(), min_support = 0.02, use_colnames = True)
save_results(frq_items, 'Apriori//apr_retail_0.02.support')

frq_items_1 = apriori(entree_bin(), min_support = 0.1, use_colnames = True)
save_results(frq_items_1, 'Apriori//apr_entree_0.1.support')

# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric ="confidence", min_threshold = 0.4)
pd.set_option('display.max_colwidth', None)
apr=rules.round(2)
print(apr[ (rules['lift'] >= 3)])
