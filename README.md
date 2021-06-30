# Data Science - Rule Mining
Research project on rule mining for the lecture Data Science


#### Tasks
1) Briefly describe the problem of rule mining in your own words; if you are a team, clearly mark which participant wrote which part of the text.

2) Describe the a priori algorithm in your own words. Describe another itemset mining algorithm (like ECLAT, FPGrowth).

3) From a public data repository, choose (at least) two data sets that you can apply itemset mining on and write a brief description of each of the datasets.
   e.g. 
    - https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research, 
    - http://archive.ics.uci.edu/ml/index.php,http://www.timeseriesclassification.com/dataset.php, 
    - http://kdd.ics.uci.edu/summary.data.application.html, 
    - http://fimi.uantwerpen.be/data/) <br/>
  
  
4) Choose public implementations (in Python) of A priori and the algorithm(s) chosen under 2), and apply them on the datasets chosen under 3) such that the support threshold     can be flexibly set as a parameter. Describe your implementation; if you are a team, clearly mark which participant wrote which part of the text.

5) Implement an evaluation module that compares the outcomes of the 2 (or n) chosen algorithms with respect to average support, confidence, lift and conviction of the obtained   rules (again, the support threshold can be flexibly set as a parameter). Describe your implementation; if you are a team, clearly mark which participant wrote which part of     the text.

6) Implement a simple web frontend (e.g. using streamlit or svelte) to select the data sets, visualize the data sets, set parameters (like support threshold) and display the     obtained rules (from 4)) as well as the comparison (from 5)) of the two (or n) algorithms. Describe the implementation and write a brief user manual with screenshots; if you   are a team, clearly mark which participant wrote which part of the text.

## Running the app

The web frontend can be run with the following command

```
streamlit run app.py
```


#### Needed Python Packeges:
- [mlxtend](https://github.com/rasbt/mlxtend) 
- [pyECLAT](https://github.com/jeffrichardchemistry/pyECLAT)
- [streamlit](https://streamlit.io)

  > pip install mlxtend pyECLAT streamlit <br/>

## Authors:
Lily Djami, 7478862        - [Mail](mailto://lily.djami@stud.uni-frankfurt.de)<br/>
-> Algorithm:  ECLAT<br/>
-> Dataset:    [entree](http://kdd.ics.uci.edu/databases/entree/entree.html)
  
Seida Basha, 7392317       - [Mail](mailto://s.basha@stud.uni-frankfurt.de)<br/>
-> Algorithm:  Apriori<br/> 
-> Dataset     [retail](http://archive.ics.uci.edu/ml/datasets/Online+Retail)

Stefan Chalupka, 6037666   - [Mail](mailto://s7021955@stud.uni-frankfurt.de) (Dropped the class)<br/>
 -> Algorithm:  FP-Growth<br/>
 -> Dataset:    [accidents](http://fimi.uantwerpen.be/data/accidents.dat)<br/>
 Warning! Dataset is not Complete in this Project...to big for github