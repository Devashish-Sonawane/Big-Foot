# Big-Foot
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

Contains code to convert the original data set, a csv file, to a tsv file

#### Requirements:

  &emsp; -need to place `reports.csv` in `data` directory

#### Execution:
```shell
cd script/task3; python csv2tsv.py
```

#### Output:

  &emsp; - `dataset1/reports.tsv`

---

## Task 4
Contains codes for each task in Task 4 and manually written data for converting irregular year expression to formatted year.

#### Requirements:

  &emsp; -Task 3 must have been executed previously (`dataset1/reports.tsv` must have been generated).

  &emsp; -`Query Builder for Public Use Statistics (1979 - Last Calendar Year).xlsx` must be located in the `data` folder (already present in this git's repository). This is the data about national park visitors counts.

  &emsp; -`irregular_year.json` must be located in the `script/task4` folder (already present in this git's repository.

  &emsp; -Set your google map API key into `task4-a.py:95`.

  &emsp; -`extract_witness_count.py` must be located in the `script/task4` folder (already present in this git's repository.

  &emsp; -`data/WeatherEvents_Jan2016-Dec2022.csv` must be located in the `data` folder (you need to download the data from https://www.kaggle.com/datasets/sobhanmoosavi/us-weather-events)
  


#### Execution:
```shell
python script/task4/task4-a.py
python script/task4/task4-b.py
python script/task4/task4-c.py
python script/task4/task4-d.py
python script/task4/task4-e.py
```

#### Output:
  &emsp; -`dataset1/reports_task4-a_1.tsv` (intermediate, some location information are added)

  &emsp; -`dataset1/national_park_task4.csv` (intermediate, national park location data)

  &emsp; -`dataset1/reports_task4-a_last.tsv` (intermediate, final output of task4-a.py)

  &emsp; -`dataset1/reports_task4-b_last.tsv` (intermediate, final output of task4-b.py)

  &emsp; -`dataset1/reports_task4-c_last.tsv` (intermediate, final output of task4-c.py)

  &emsp; -`dataset1/reports_task4-d_last.tsv` (intermediate, final output of task4-d.py)

  &emsp; -`dataset1/reports_task4-e_last.tsv` (final output of task4-e.py and task4)


---

## Task 5
Contains code to merge three datasets (census, alcohol, and state mammals), with bigfoot dataset.

'Task_5-1.ipynb' is not needed for its execution but it explains how to merge the '.txt' dataset step by step (locally implemented code, do not execute, only for didactic purpose)

#### Requirements:

  &emsp; -The three alternative datasets must be located in the 'data' folder (already present in this git's repository.
  
  &emsp; -Task 4 must have been executed previously ('dataset1/reports_task4-e_last.tsv' must have been generated).
  
  &emsp; -Task 5 scripts ('Task5TXT.py', 'Task5PDF.py', 'Task5JPG.py', and 'Task5Launch.py) must be located in a level higher than the 'dataset1' and &emsp;'data' folder ('Big-Foot' folder for this repository)

#### Execution:
```shell
python Task5Launch.py    
```
To execute this task you only to execute 'Task5Launch.py', this program will be in charge of executing all the indivual scripts and merging them into an unique tsv. Execution must done from the same location as Task 5 scripts.

#### Note:
The state mammal data was extracted manually from the image dataset consisting of 73 state mammal images. A state mammal is the official mammal of a U.S. state as designated by a state's legislature. The 'state' and 'state mammal' data was extracted from the side information of the image dataset. The 'Foot size' data was manually looked up photo by photo, by searching corresponding mammals' description.

#### Output:
  &emsp; -'dataset1/reports_task5.tsv'

---

## Task 6
### Part 1

Contains codes for converting tsv file to JSON file
Requirements:
  &emsp; Task 5 must have been executed previously (‘reports_task5.tsv’ must have been generated
#### Output:
  &emsp; -`dataset1/aggregate.json`

### Part 2

Contains code for splitting JSON file into chunks of 100
#### Output:
  &emsp; -4373 json chunks 

### Part 3

Contains code for displaying ...
#### Output:
  &emsp; -3 visualizations


---

## Task 7
Contains codes for converting a bunch of JSON files into one TSV file.

#### Requirements:

  &emsp; -Task 5 must have been executed previously (`dataset1/reports_task5.tsv` must have been generated).

  &emsp; -Task 6 must have been executed previously (`dataset1/json` directory must have a bunch of JSON files named like `chunkX.json`).

#### Execution:
```shell
python script/task7/json2tsv.py
```

#### Output:
  &emsp; -`dataset1/reports_task7.tsv`
