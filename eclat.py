"""
# Data Science 1 Project: Rule Mining
by Lily Djami
"""

from pyECLAT import ECLAT
from datasets import entree_dataset, retail_horizontal, accident_df
from rules import save_results

if __name__=="__main__":

    retail_ds = retail_horizontal()
    entree_ds = entree_dataset()
    #accident_ds = accident_df()
 
    retail_eclat = ECLAT(data=retail_ds, verbose=True)
    save_results(retail_eclat, "ECLAT\\retail.eclat")
    
    entree_eclat = ECLAT(data=entree_ds, verbose=True)
    save_results(entree_eclat, "ECLAT\\entree.eclat")
    
    #accident_eclat = ECLAT(data=accident_ds, verbose=True)
    #save_results(accident_eclat, "ECLAT\\accident.eclat"))
    
    #'''
    print("Calculating support for dataset: Retail wtih ECLAT")
    retail_support = retail_eclat.fit_all(verbose=True)
    print("Finished calculaing support! Saving results to ECLAT\\retail_all.support")
    save_results(retail_support[1], "ECLAT\\retail_all.support")
    print("Saved!")
    
    print("Calculating support for dataset: Entree WITH ECLAT")
    entree_support = entree_eclat.fit_all(verbose=True)
    print("Finished calculaing support! Saving results to ECLAT\\entree_all.support")
    save_results(entree_support[1], "ECLAT\\entree_all.support")
    print("Saved!") 
    #'''
    
    '''
    print("Calculating support for dataset: Accident")
    accident_support = accident_eclat.fit_all(verbose=True)
    print("Finished calculaing support! Saving results to ECLAT\\accident_all.support")
    save_results(accident_support[1], "ECLAT\\accident_all.support")
    print("Saved!")
    '''