"""
# Data Science 1 Project: Rule Mining
by Lily Djami
"""
import pickle
import pandas as pd
from mlxtend.frequent_patterns import association_rules

'''
loading and saving results using pickle
'''
def save_results(res, filename):
    with open(filename, 'wb') as f:
        pickle.dump(res, f)

def load_results(filename):
    return pickle.load(open(filename, 'rb'))

'''
create association rules using support from ECLAT
'''
def rules_from_support(support, min_support=0, separator=" & "):
    df = pd.DataFrame.from_dict(support, orient="index").reset_index()
    df = df.rename(columns={"index": "itemsets", 0: "support"})
    df['itemsets'] = [frozenset(i.split(separator)) for i in df['itemsets']]
    rules = association_rules(df, min_threshold=min_support)
    return rules

'''
convert antecedent and consequent in rule as string to enable join
'''
def frozenset_to_str(t):
    t = list(t)
    t.sort()
    return "(" + ", ".join([str(i) for i in t]) + ")"

def rule_str(rule_df):
    rule_list = [frozenset_to_str(rule_df['antecedents'][i]) + " -> " + frozenset_to_str(rule_df['consequents'][i])
                for i in range(rule_df.shape[0])]

    rule_df['rule'] = rule_list