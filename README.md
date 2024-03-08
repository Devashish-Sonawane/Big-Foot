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
python script/task3/csv2tsv.py
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
Contains code to merge three datasets (population census, alcohol consumption, and state mammals), with bigfoot dataset.

'Task_5-1.ipynb' is not needed for its execution but it explains how to merge the '.txt' dataset step by step (locally implemented code, do not execute, only for didactic purpose)

#### Requirements:

  &emsp; -The three alternative datasets must be located in the 'data' folder (already present in this git's repository).
  
  &emsp; -Task 4 must have been executed previously ('dataset1/reports_task4-e_last.tsv' must have been generated).
  
  &emsp; -Task 5 scripts ('Task5TXT.py', 'Task5PDF.py', 'Task5PNG.py', and 'Task5Launch.py) must be located in a level higher than the 'dataset1' and &emsp;'data' folder ('Big-Foot' folder for this repository)

#### Execution:
```shell
python script/task5/Task5Launch.py    
```
To execute this task you only to execute 'Task5Launch.py', this program will be in charge of executing all the indivual scripts and merging them into an unique tsv. Execution must done from the same location as Task 5 scripts.

#### Note:
The state mammal data was extracted manually from the image dataset consisting of 73 state mammal images. A state mammal is the official mammal of a U.S. state as designated by a state's legislature. The 'state' and 'state mammal' data was extracted from the side information of the image dataset. The 'Foot size' data was manually looked up photo by photo, by searching corresponding mammals' description. All the PNG images are stored in the folder 'state_mammal' in 'data' folder.

#### Output:
  &emsp; -'dataset1/reports_task5.tsv'

---

## Task 6
### Part 1
Contains codes for converting tsv file to JSON file
#### Requirements:

  &emsp; -Task 5 must have been executed previously (‘reports_task5.tsv’ must have been generated)

  &emsp; -aggregate-json folder must be created for the output

  &emsp; -The folder ‘conf’ must be created

  &emsp; -In the conf folder the user should put the following files:‘colheaders.txt’ containing column headers,‘encoding.txt’ containing encodings 


  
#### Execution:

In order not to duplicate column names when creating json it is important to copy the headers from the first row of tsv file to the 'colheaders.txt' file (which is used in the next step) and, after that, delete the first row.

Tsv file ('reports_task5.tsv') was renamed to '5467 task5.tsv' (where 5467 is a number of rows after deletion of the first one) for the convinience.

```shell
tsvtojson -t 5467\ task5.tsv -j aggregate-json/aggregate.json -c conf/colheaders.txt -o BFRO -e conf/encoding.txt -s 0.8 -v
```

#### Output:
  &emsp; -`dataset1/aggregate.json`

### Part 2

Contains code for splitting JSON file into chunks of 100 lines

#### Execution:

To execute this task there are 2 files required: 'split_files.sh' and 'aggregate.json'

Before execution it is critically important to update the input file name in the line 7 of the 'split_files.sh' file. In addition, the user should manually create the folder named 'output' in the working directory (that's where all the chunks will go)

#### Output:
  &emsp; -`dataset1/output`
  Which is 4373 chunks (jsons) of the data, which will be used to create subsets for the part 3

### Part 3

Contains code for displaying ...
#### Output:
  &emsp; -3 visualizations


---

## Task 7
Contains codes for converting a bunch of JSON files into one TSV file.

#### Requirements:

  &emsp; -Task 5 must have been executed previously (`dataset1/reports_task5.tsv` must have been generated).

  &emsp; -Task 6 must have been executed previously (`dataset1/output` directory must have a bunch of JSON files named like `chunkX.json`).

#### Execution:
```shell
python script/task7/json2tsv.py
```

#### Output:
  &emsp; -`dataset1/reports_task7.tsv`

---

## Extra credit task

Creating html file `chord.html` 

When creating the file in it was used d3.js code which builds the chord diagram based on the data of the file containing the information in the csv file with the columns : `x_coordinate`, `y_coordinate`, `similarity score`

So, basically, it is possible to build chord diagram using files such as jaccard.csv, edit.csv, cosine.csv (which contained columns `x_coordinate`, `y_coordinate`, `similarity score`) from the task 6.

For transforming the file (which was in the previous step) was used the following Python code:

```shell
python script/extra-credit/clusterization.py
```
Note: it is important to incude the csv filename (e.g. jaccard.csv) in the 6th line of the clusterization.py script.

Html file is transferred from extra-credit to the working directory for creating the template for the vusualization 

```shell
cp script/extra-credit/chord.html .

Note: it is important to incude the csv filename (e.g. jaccard.csv) in the 43th line of the chord.html script.

```
For visualization the python server is launched:

```shell
python -mhttp.server 8082
```
(this fires up a server on port 8082, so then visit http://localhost:8082/chord.html)

The visualization should be similar to the following one in structure (this one specifically was based on the jaccard.csv file from the task 6, which was a result of calculation of Jaccard similarity measure using Tika Similarity

!!!! PICTURE


---

## Work division

Ariel Martinez: Task 4e, PDF dataset (task 5), conversion of .ipynb to .py

Kyosuke Chikamatsu: Task3, Task4 a-e, Task7

Devashish Sonawane: TXT dataset - Alcohol Consumption (Task 5)

Willy Tang: PNG dataset (Task 5)

Ekaterina Shtyrkova: Task 6, Task 8

---
