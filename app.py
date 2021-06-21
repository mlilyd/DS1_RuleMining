import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

#import dataset reading functions from other modules
from datasets import *
from rules import *

"""
# Data Science 1 Project: Rule Mining
by Seida Basha, Lily Djami
"""

ds_selection = st.selectbox(
    'Select a dataset',
    ["Retail", "Entree"])


retail_apriori = load_results("Apriori\\apr_retail_0.04.support")
entree_apriori = load_results("Apriori\\apr_entree_0.1.support")

retail_eclat = load_results("ECLAT\\retail_2_0.04.support")
entree_eclat = load_results("ECLAT\\entree_0.1.support")

retail_eclat_rules = rules_from_support(retail_eclat)
retail_apriori_rules = association_rules(retail_apriori, min_threshold = 0)

rule_str(retail_eclat_rules)
rule_str(retail_apriori_rules)
retail_eclat_rules = retail_eclat_rules.sort_values('rule')
retail_apriori_rules = retail_apriori_rules.sort_values('rule')

entree_eclat_rules = rules_from_support(entree_eclat[1])
entree_apriori_rules = association_rules(entree_apriori, min_threshold = 0)

rule_str(entree_eclat_rules)
rule_str(entree_apriori_rules)
entree_eclat_rules = entree_eclat_rules.sort_values('rule')
entree_apriori_rules = entree_apriori_rules.sort_values('rule')

if ds_selection == "Entree":
  dataset = entree_dataset()
  res_apriori=entree_apriori_rules
  res_eclat=entree_eclat_rules
elif ds_selection == "Retail":
  dataset = retail_dataset() 
  res_apriori=retail_apriori_rules
  res_eclat=retail_eclat_rules

dataset
rules_selection = st.selectbox(
    'Select an algorithm',
    ["Apriori", "ECLAT"])

if rules_selection=="Apriori":
  rules = res_apriori
else:
  rules = res_eclat

rules[['rule','support','confidence','lift','conviction']]

entree_joined = pd.merge(entree_eclat_rules, entree_apriori_rules, on="rule", suffixes=("_eclat", "_apriori"))
entree_joined = entree_joined.sort_values('rule')

retail_joined = pd.merge(retail_eclat_rules, retail_apriori_rules[retail_apriori_rules['support']>0.05], on="rule", suffixes=("_eclat", "_apriori"))
retail_joined = retail_joined.sort_values('rule')

st.subheader("Average Support")
avg_apr_entree= entree_apriori_rules['support'].mean()
avg_apr_retail=retail_apriori_rules['support'].mean()
avg_ecl_retail=retail_eclat_rules['support'].mean()
avg_ecl_entree=entree_eclat_rules['support'].mean()

mean = pd.DataFrame()
mean['label'] = ['Entree with Apriori','Retail with Apriori','Retail with ECLAT','Entree with ECLAT']
mean['mean'] = [avg_apr_entree, avg_apr_retail, avg_ecl_retail, avg_ecl_entree]
color_discrete_map={'Entree with apriori':'maroon','Retail with apriori':'red','Retail with ECLAT':'royalblue','Entree with ECLAT':'darkblue'}
fig = px.pie(mean, values='mean', names='label', color_discrete_sequence=['#B03A2E', '#2874A6', '#5DADE2', '#EC7063' ])
fig.update_traces(textinfo='value')
st.write(fig)


if ds_selection=='Entree':
  fig = px.line(entree_joined, y=['confidence_apriori', 'confidence_eclat'], labels={'index':'Rule Index', 'value':'Confidence'}, title="Confidence from {} Dataset".format(ds_selection), template='plotly_dark')
  st.write(fig)
else:
  fig = px.line(retail_joined, y=['confidence_apriori', 'confidence_eclat'], labels={'index':'Rule Index', 'value':'Confidence'},title="Confidence from {} Dataset".format(ds_selection), template='plotly_dark')
  st.write(fig)


if ds_selection=='Entree':
  fig = px.scatter(entree_joined, y=['lift_apriori', 'lift_eclat'], labels={'index':'Rule Index', 'value':'Lift'}, 
  title="Lift from {} Dataset".format(ds_selection), template='plotly_dark')
  
  st.write(fig)
else:
  fig = px.scatter(retail_joined, y=['lift_apriori', 'lift_eclat'], labels={'index':'Rule Index', 'value':'Lift'},title="Lift from {} Dataset".format(ds_selection), template='plotly_dark')
  st.write(fig)


if ds_selection=='Entree':
  fig = px.scatter(entree_joined, y=['conviction_apriori', 'conviction_eclat'], labels={'index':'Rule Index', 'value':'Conviction'},title="Conviction from {} Dataset".format(ds_selection), template='plotly_dark')
  st.write(fig)
else:
  fig = px.scatter(retail_joined, y=['conviction_apriori', 'conviction_eclat'], labels={'index':'Rule Index', 'value':'Conviction'}, title="Conviction from {} Dataset".format(ds_selection), template='plotly_dark')
  st.write(fig)
