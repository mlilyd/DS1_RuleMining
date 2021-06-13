from datasets import *
from mlxtend.frequent_patterns import apriori, association_rules

# Building the model
frq_items = apriori(retail_dataset(), min_support = 0.04, use_colnames = True)

# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric ="confidence", min_threshold = 0.4)
pd.set_option('display.max_colwidth', None)
apr=rules.round(2)
print(apr[ (rules['lift'] >= 3)])

#from rules import rules_from_support
#support=pickle.load(open("./ECLAT/retail_0.05.support", 'rb'))
#rules_from_support(support[1], 0.05, separator=" & ")