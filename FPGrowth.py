from fpgrowth_py.fpgrowth import fpgrowth
from fpgrowth_py.utils import *
import pprint as pprint
pp = pprint.PrettyPrinter(indent=4)

itemSetList = [['MONKEY'],
                ['DONKEY'],
                ['MAKE'],
                ['MUCKY'],
                ['COOKIE']]

#freqItemSet, rules = fpgrowth(itemSetList, minSup=0.5, minConf=0.5)
freqItemSet, rules = fpgrowth(itemSetList, 0.51, 0.5)
#pp.pprint(rules)
pp.pprint(freqItemSet)



