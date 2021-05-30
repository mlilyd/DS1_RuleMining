from fpgrowth_py.fpgrowth import fpgrowth
from fpgrowth_py.utils import *
import pprint as pprint
pp = pprint.PrettyPrinter(indent=4)

itemSetList=[]
#itemSetList = [['MONKEY'],['DONKEY'],['MAKE'],['MUCKY'],['COOKIE']]

def sortLength(item):
    return len(item)


####Read Dataset for Algo####
def read_accident():
    file_path='C:/Users/Stefan Chalupka/Desktop/DataScience/sample.txt'
    datei=open(file_path, 'r')

    for i in datei:
        line=datei.readline()
        liste=line.split(' ')
        if liste[-1]=='\n':
            liste.pop()
        itemSetList.append(liste)



#freqItemSet, rules = fpgrowth(itemSetList, minSup=0.5, minConf=0.5)
#pp.pprint(rules)


####Start Algo####
read_accident()
freqItemSet, rules = fpgrowth(itemSetList, 0.7, 0.7)


####Print Result####
freqItemSet.sort(reverse = True, key = sortLength)
for i in freqItemSet:
    if len(i) > 4:
        print(sorted(i))
#pp.pprint(freqItemSet)



