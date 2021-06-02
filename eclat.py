"""
# Data Science 1 Project: Rule Mining
by Lily Djami
"""

from pyECLAT import ECLAT
from entree import read_entree_dataset

#reading entree dataset
dataset = read_entree_dataset()

#applying ECLAT algorithm on dataset
eclat_instance = ECLAT(data=dataset, verbose=True)
ECLAT_indexes, ECLAT_supports = eclat_instance.fit (min_support=0.5,
                                                            min_combination=1,
                                                            max_combination=2,
                                                            separator=', ',
                                                            verbose=True)

print(ECLAT_indexes)
print(ECLAT_supports)