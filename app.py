import streamlit as st
import numpy as np
import pandas as pd
import time


#import dataset reading functions from other modules
from datasets import *

"""
# Data Science 1 Project: Rule Mining
by Seida Basha, Stefan Chalupka, Lily Djami
"""


ds_selection = st.selectbox(
    'Select a dataset',
    ["Entree Dataset", "Accidents", "Retail"])

#dummy dataset for initialization
dataset = pd.DataFrame()

if ds_selection == "Entree Dataset":
  dataset = entree_dataset()
elif ds_selection == "Retail":
  dataset = retail_dataset() 

dataset

"""
Here are some examples for Streamlit
"""
algorithm = st.selectbox(
    'Choose an algorithm',
    ["A-Priori", "ECLAT", "FP-Growth"])


'You selected:', algorithm


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

    


