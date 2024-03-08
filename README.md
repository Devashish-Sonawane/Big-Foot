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

  &emsp; -Etllib must be installed
  
  &emsp; -Task 5 must have been executed previously (‘reports_task5.tsv’ must have been generated)

  &emsp; -aggregate-json folder must be created for the output

  &emsp; -The folder ‘conf’ must be created

  &emsp; -In the conf folder the user should put the following files:‘colheaders.txt’ containing column headers,‘encoding.txt’ containing encodings 

  the conf folder for the given data can be found: `scripts/task6/conf`
  
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

To execute this task there are 2 files required: `script/task6/split_files.sh` and `dataset/aggregate.json` (the output of part 1)


Before execution it is critically important to update the input file name in the line 7 of the 'split_files.sh' file. In addition, the user should manually create the folder named 'output' in the working directory (that's where all the chunks will go) and the folder `aggregate-json' and put the .json file which has to be divided into this folder.

After that the only step left is the execution of the command:

```shell
sh split_files.sh aggregate-json
```

#### Output:
  &emsp; -`dataset1/output` 
  Which is 4373 chunks (jsons) of the data, which will appear in the `output` folder (created manually before`, an those chunks will be used to create subsets for the part 3

### Part 3

For the part where it was asked to explore the generic features the visualizations were based on, the steps were the following:

1. The specific script `script/task6/columns.py` was used to replace the columns in the original json file -  `dataset1/aggregate.json` wil just "" value. It is important to specify- which columns specifically would need to be replaced.
   
   It one case of getting rid of text columns the columns such as "City","MAMMAL 1", "Follow-up: were replaced, in the other case of getting rid of columns with numerical values, the columns such as "Precipitation(in)", "ZipCode" and "Population (age 21 and older)" were replaced.

   For the convenience, there are 2 scripts- `script/task6/replace-text-columns.py` replaces text columns with "", `script/task6/replace-numeric-columns.py` replaces numeric columns with "".
   
   The only thing left to implement this step is to specify the initial json (in which the keys (columns) will be replaced by "" and the name of the file which will be created as a json file with replaced columns (for the purpose of saving the initial data the program creates a new file with replaced columns, it does not owerwrites existing file) in lines 38 an 39 of the `script/task6/replace-text-columns.py` and `script/task6/replace-numeric-columns.py`.

2. After getting 2 new jsons with replaced keys (columns), it is needed to divide them onto chunks by repeating Part 2 of Task 6 (the previous part).
   
3. After that out of each set of chunks the first 100 were manually taken for the part 4. (It is critically important to take the same-numbered chunks since part 4 should compare the results for those chunks for the 3 visualizations, an we need them to correspond to the same observations) 


#### Output:
  &emsp; 3 json files + 3 sets of 100 chunks, one-from the json with all keys(columns), another-from the json with text columns replaced by "", and the third one-from the json with numeric columns replaced by "" 

### Part 4

1. First step is to clone the git which would bring in files for the visualizations
   
```shell
git clone http://github.com/chrismattmann/tika-similarity
```
2. After that it is crucial to make sure that the files from the git are in the working derectory.

3. Requirements: import "subprocess" module to python, latest version of editdistance installed
   
   There are scripts : `script/task6/Jaccard.py`, `script/task6/Edit.py`, `script/task6/Cosine.py` which alost automate the visualization process, however, it is important to make sure that the paths to files from git (from the step 1) needed are all there. If all the paths and level transitions are handled correctly, the execution for the visualizations should be reduced to the following:

Jaccard:
`script/task6/Jaccard.py`

```shell
python -mhttp.server 8082
```
(this fires up a server on port 8082, so then visit http://localhost:8082/levelCluster-d3.html)

Edit Distance:


```shell
`script/task6/Edit.py`
```

```shell
python -mhttp.server 8082
```
(this fires up a server on port 8082, so then visit http://localhost:8082/levelCluster-d3.html)

Cosine:
```shell
`script/task6/Cosine.py`
```

```shell
python -mhttp.server 8082
```
(this fires up a server on port 8082, so then visit http://localhost:8082/levelCluster-d3.html)

#### Output:
  &emsp; Visualizations for the chunks of data (the ones from the json with all keys, the ones from the json with text keys replaced by "", the ones from the json with numerical keys replaced by "", based on the differences in which we can make conclusions on the features used by different measures (see final report)

Visualizations for the json chunks with all keys:

Jaccard
<img width="477" alt="Screenshot 2024-03-08 at 11 06 16 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/5aa26d93-91d7-4b7d-b65f-7ada404d8b86">

Edit 
<img width="570" alt="Screenshot 2024-03-08 at 4 26 58 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/94c8217a-ebe1-4717-8198-daa03d91ce56">

Cosine
<img width="487" alt="Screenshot 2024-03-08 at 5 31 13 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/168020c4-e304-4ae7-9718-140a523e9d1c">


Visualizations for the json chunks with text keys deleted:

Jaccard
<img width="497" alt="Screenshot 2024-03-08 at 5 11 45 AM-jaccard-withoutcolumns" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/3bdbea3d-a736-43b1-a154-a0d294187b72">

Edit
<img width="485" alt="Screenshot 2024-03-08 at 4 41 44 AM-edit-without-columns" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/a43cc847-82d6-4024-80f3-6511fb697188">

Cosine
<img width="511" alt="Screenshot 2024-03-08 at 5 58 02 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/5fb110a0-13a1-4a71-8189-8ff55fe79a35">

Visualizations for the json chunks with numerical keys deleted:

Jaccard
<img width="398" alt="Screenshot 2024-03-08 at 11 11 15 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/0a8cc195-20eb-4f69-b6b0-4605e4b10476">

Edit
<img width="470" alt="Screenshot 2024-03-08 at 11 11 59 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/c7de85a1-1415-4e31-acb2-c5880d9bff26">

Cosine
<img width="319" alt="Screenshot 2024-03-08 at 11 12 43 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/3cb1283a-667a-4d9d-b9d7-dae560e3c1b4">


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

So, basically, it is possible to build chord diagram using files such as jaccard.csv, edit.csv, cosine.csv (which contained columns `x_coordinate`, `y_coordinate`, `similarity score`) from the task 6 as an input.

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

#### Output:
  &emsp; Should produce similar visualization:
  
<img width="772" alt="Screenshot 2024-03-08 at 11 14 47 AM" src="https://github.com/Devashish-Sonawane/Big-Foot/assets/158105673/37d5e82d-12ba-445e-ba56-b7e486de237a">


---

## Work division

Ariel Martinez: Task 4e, PDF dataset (task 5), conversion of .ipynb to .py

Kyosuke Chikamatsu: Task3, Task4 a-e, Task7

Devashish Sonawane: TXT dataset - Alcohol Consumption (Task 5)

Willy Tang: PNG dataset (Task 5)

Ekaterina Shtyrkova: Task 6, Task 8

---
