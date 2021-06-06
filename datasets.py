import os
import pandas as pd

"""
reading Retail dataset
by Seida Basha
"""
def retail_dataset():
    data = pd.read_excel('./Datasets/Online_Retail.xlsx')

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
    return basket_sets


"""
reading Entree dataset
by Lily Djami
"""
def prepare_entree_dataset():
    dir = "./Datasets/entree/data/"
    cols = [i for i in range(0, 2)]
    data = []
    for file in os.listdir(dir):
        if file.endswith(".txt") and file!="features.txt":
            #print(file)
            df = pd.read_csv(dir+file, sep='\t', names=cols, engine='python')
            #print(df)
            data.append(df)
    
    res = pd.concat(data)
    res = res.drop([0], axis=1)
    res.to_csv("Datasets/entree/entree.csv", sep=" ", index=False)
    
def entree_dataset():
    dir = "./Datasets/entree/"
    cols = [i for i in range(0, 30)]
    res = pd.read_csv(dir+"entree.csv", sep=" ", names=cols, engine='python')
    res.fillna("-", inplace=True)
    res.applymap(str)
    return res


"""
reading Accident dataset
by Stefan Chalupka
"""
def accident_dataset():
    itemSetList=[]
    file_path='./Datasets/accidents-shortened.dat'
    datei=open(file_path, 'r')
    for i in datei:
        line=datei.readline()
        liste=line.split(' ')
        if liste[-1]=='\n':
            liste.pop()
        itemSetList.append(liste)
    
    return itemSetList