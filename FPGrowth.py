from fpgrowth_py.fpgrowth import fpgrowth
from fpgrowth_py.utils import *
import pprint as pprint
pp = pprint.PrettyPrinter(indent=4)

itemSetList=[]
#itemSetList = [['MONKEY'],['DONKEY'],['MAKE'],['MUCKY'],['COOKIE']]


#Hilfsfunktionen
def sortLength(item):
    return len(item)



    
####Read Dataset Accident for Algo####
def read_accident():
    file_path='C:/Users/Stefan Chalupka/Desktop/DataScience/sample.txt'
    datei=open(file_path, 'r')
    for i in datei:
        line=datei.readline()
        liste=line.split(' ')
        if liste[-1]=='\n':
            liste.pop()
        itemSetList.append(liste)
    
####Read Dataset Retail for Algo####
def read_retail():
    file_path='C:/Users/Stefan Chalupka/Desktop/DataScience/retail.dat'
    datei=open(file_path, 'r')
    for i in datei:
        line=datei.readline()
        liste=line.split(' ')
        if liste[-1]=='\n':
            liste.pop()
        itemSetList.append(liste)

####Read Dataset Entree for Algo####
#def read_entree():
#    file_path='C:/Users/Stefan Chalupka/Desktop/DataScience/retail.dat'
#    datei=open(file_path, 'r')
#    for i in datei:
#        line=datei.readline()
#        liste=line.split(' ')
#        if liste[-1]=='\n':
#            liste.pop()
#        itemSetList.append(liste)



####Print result of Algorithm####
def print_result(dataset, freqItemSet, rules):
    if dataset == 'accident':
        freqItemSet.sort(reverse = True, key = sortLength)
        for i in freqItemSet:
            if len(i) > 4:
                print(sorted(i))
        #pp.pprint(freqItemSet)

        #freqItemSet, rules = fpgrowth(itemSetList, minSup=0.5, minConf=0.5)
        #pp.pprint(rules)

    elif dataset == 'retail':
        pp.pprint(freqItemSet)

        #freqItemSet, rules = fpgrowth(itemSetList, minSup=0.5, minConf=0.5)
        #pp.pprint(rules)
        
    elif dataset == 'entree':
        pp.pprint(freqItemSet)

        #freqItemSet, rules = fpgrowth(itemSetList, minSup=0.5, minConf=0.5)
        #pp.pprint(rules)

    else:
        print("Please Use correct Dataset:\nMain('accident')\nMain('retail')\nMain('entree')")

#Start Program with Dataset
def Main(dataset, minSup=0.5, minConf=0.5):
    if dataset == 'accident':
        read_accident()
    elif dataset == 'retail':
        read_retail()
    elif dataset == 'entree':
        read_entree()
    else:
        print("Please Use correct Dataset:\nMain('accident')\nMain('retail')\nMain('entree')")



    ####Start Algo####
    freqItemSet, rules = fpgrowth(itemSetList, minSup, minConf)
    print_result(dataset, freqItemSet, rules )
    
#Main('accident', 0.7, 0.7)
Main('retail', 0.3, 0.3)
