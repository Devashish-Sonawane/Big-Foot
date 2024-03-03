# Big-Foot-
This is a shared repository containing data from Big Foot Field Researchers Organization (BFRO).

---
##Instalation of required libraries

To install use (while in the same folder as requirements.txt):

```shell
'pip install -r requirements.txt'
```

'pip' must be previously installed.
---

## Task 3

```shell
cd script/task3; python csv2tsv.py
```

---

## Task 5
Contains code to merge three datasets (census, alcohol, and animal sightings), with bigfoot dataset.

Requirements:
  -The three alternative datasets must be located in the 'data' folder (already present in this git's repository.
  -Task 4 must have been executed previously ('dataset1/reports_task4-e_last.tsv' must have been generated).
  -Task 5 scripts ('Task5TXT.py', 'Task5PDF.py', 'Task5JPG.py', and 'Task5Launch.py) must be located in a level higher than the 'dataset1' and 'data' folder ('Big-Foot' folder for this repository)
  
To execute this task you only to execute 'Task5Launch.py', this program will be in charge of executing all the indivual scripts and merging them into an unique tsv. Execution must done from the same location as Task 5 scripts.

Execution:
```shell
python Task5Launch.py    
```

Output:
  -'dataset1/reports_task5.tsv'
