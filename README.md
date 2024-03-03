# Big-Foot-
This is a shared repository containing data from Big Foot Field Researchers Organization (BFRO).

---
## Instalation of required libraries

To install write in the command line (while in the same folder as requirements.txt):

```shell
pip install -r requirements.txt
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

'Task_5-1.ipynb' is not needed for its execution but it explains how to merge the TXT dataset step by step (locally implemented code, don't executed, only for didactid purpose)

#### Requirements:

  &emsp; -The three alternative datasets must be located in the 'data' folder (already present in this git's repository.
  
  &emsp; -Task 4 must have been executed previously ('dataset1/reports_task4-e_last.tsv' must have been generated).
  
  &emsp; -Task 5 scripts ('Task5TXT.py', 'Task5PDF.py', 'Task5JPG.py', and 'Task5Launch.py) must be located in a level higher than the 'dataset1' and 'data' folder ('Big-Foot' folder for this repository)

#### Execution:
```shell
python Task5Launch.py    
```
To execute this task you only to execute 'Task5Launch.py', this program will be in charge of executing all the indivual scripts and merging them into an unique tsv. Execution must done from the same location as Task 5 scripts.

#### Output:
  &emsp; -'dataset1/reports_task5.tsv'
