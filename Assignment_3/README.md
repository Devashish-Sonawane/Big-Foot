# DSCI 550 Spring 2024 Assignment 3 (Team 9)
This repository hosts the DSCI 550 Spring 2024 Assignment 3.

## Webpage

https://ambirlanga.github.io/DSCI550_BF_Web/

Note: Mac users might be unable to interact with visualization 2. After some testing, we found out that this is NOT true for ALL MacOs enviroments, so this might be due to an incompatibility with a browser extension.

---

## Installation of required libraries

To install write in the command line (while in the same folder as requirements.txt):

```shell
pip install -r requirements.txt
```
'pip' must be previously installed.

## Docker Installation

Task 3, 4 and 5 require Docker installation.
- Docker Desktop must have been installed and run previously (Please refer to https://docs.docker.com/desktop/install/mac-install/).
- Windows users need to install Linux distribution by using WSL as well (Please refer to https://learn.microsoft.com/ja-jp/windows/wsl/install).
- In addition, Windows users need to have docker enable integration with the Linux distribution (Please check Settings/Resources/WSL integration on your Docker Desktop).
- Windows users will execute Docker commands in your Linux distribution terminal. Mac users will execute Docker commands in your terminal.

## Task 1-2

### Website
All visualizations can be viewed on the website: https://ambirlanga.github.io/DSCI550_BF_Web/
Link to public git repository with website code: https://github.com/ambirlanga/ambirlanga.github.io/tree/main/DSCI550_BF_Web

Notes on website code folders:
- For the website, we followed the ufo template: https://github.com/USCDataScience/ufo.usc.edu/tree/master- The html folder has all of our html files for visualizations
- The css folder has css code I took from the template
- The json folder has our json data for the visualizations
- The js folder has js code I took from the template
- The images folder has our front page image, logo, and thumbnail images.
- The index file outside the folders follow the one in the template with updates for ours.

### Visualization 1: Line Chart 
- To view on website, open the following link: https://ambirlanga.github.io/DSCI550_BF_Web/html/visualization_1.html
- 
For generating the json for the line chart: 
- Open Jupyter Notebook and navigate to Big-Foot\Assignment_3\Scripts\task1-2\vis1\task1_visualization1.ipynb. 
- Click run all cells in task_1_visualization_1.ipynb to aggregate and get json objects for the first visualization
  (the line chart).

In order to view the visualization locally rather than on the website, in the command line, navigate to the directory: cd Big-Foot\Assignment_3
- Start a python server by typing this command: python -m http.server
- If it doesn't open automatically, navigate to http://localhost:8000 or the url provided in the 
  command line.
- From the browser, navigate to Scripts/task1-2/vis1 and click on visualization_1.html to open and view the visualization.
- Alternatively, view the visualization on our visualization website, where it can be found under the Visualization tab as the Line Chart.
- Note that the file for this visualization is slightly different in this directory versus the one that can be found 
  under the github website repository under the html folder with the same name as the file in the website has added code
  to connect it to the website and be consistent with our website format whereas the file in this directory can be viewed through localhost
  as well, so it does not have that code. The only difference for the visualization is that this one does not have the description
  whereas the one on the website does. Feel free to view the website file on github if you want to look at both versions.

#### Output:
Json data file for visualization 1 (Line Chart):
- Dataset1/BFRO_vis_1.json

### Visualization 2:
- Execute MapJson.py in (Big-Foot\Assignment_3\Scripts\task1-2\vis2) from the Assignment_3 folder to create a copy of the json used in this visualization. 
- visualization_2.html uses a embedded visualization stored in:

https://observablehq.com/d/c6f9d60f9efa8eb3 

#### Output:
- BFRO_vis_2.json

### Visualization 3:
- Execute BFRO_vis_3.py in (Big-Foot\Assignment_3\Scripts\task1-2\vis3) to create a copy of the json used in this visualization. 
- From the browser, navigate to Scripts/task1-2/vis3 and click on visualization_3.html to open and view the visualization.
- Alternatively, view the visualization on our visualization website.

#### Output:
- BFRO_vis_3.json

### Visualization 4:
- Execute Visualization_4.py in (..\Scripts\task1-2\vis4) to obtain the json file containing data used in the visualization. (Note: The program can take 10-15 minutes for producing the output)
- Open file titled 'Visualization_4.html' located in the same directory (..\Scripts\task1-2\vis4) to see the Circle Packing chart.
- Alternatively, the chart is available on our website.

#### Ouput:
- 'BFRO_vis_4.json' located in (..\Dataset1)

## Task 3

### Starting the Solr Container

To start the Apache Solr container, navigate to the appropriate script directory and use Docker Compose to launch the service:

```shell
cd Scripts/task3
docker-compose up -d
```

After successful startup, the Solr service will be available at:
- http://localhost:8983

### Setting up Solr Schema and Data Ingestion

1. **Upload Schema**:
   Set the schema for the Solr instance by executing the Python script:

   ```shell
   python set_schema.py
   ```

2. **Ingest JSON Data**:
   Ingest data into Solr using the provided shell script:

   ```shell
   ./ingest-json.sh
   ```

3. **Compress Solr Index**:
   Retrieve and compress the Solr index data:

   ```shell
   ./get_compressed_index.sh
   ```

### Sample Queries

Execute the following queries to interact with the Solr server:

- Retrieve 10 documents from the dataset:
  - http://localhost:8983/solr/bigfoot/select?q=*:*&wt=json&indent=true&rows=10

- Get statistical data for `BF_Witness_Count`:
  - http://localhost:8983/solr/bigfoot/select?q=*:*&rows=0&stats=true&stats.field=BF_Witness_Count

- Filter documents by year and return specific fields (e.g., from 2016):
  - http://localhost:8983/solr/bigfoot/select?q=*:*&fq=BF_Fixed_Year:2016&fl=BF_Id,BF_Class,BF_Headline

- Calculate average witness count by state:
  - [click here](http://localhost:8983/solr/bigfoot/select?q=*:*&rows=0&json.facet={categories:{type:terms,field:BF_State,facet:{average_wc:"avg(BF_Witness_Count)"}}})

---

## Task 4

### Creating the Image Index

To create a new image index, perform the following steps:

- **Start the Docker Containers**:
   Navigate to the script directory and start the required Docker services with the image directory set:

   ```shell
   cd Scripts/task4
   IMAGE_DIR=./Images/ docker-compose up -d
   ./smqtk_services.run_images.sh --docker-network task4_imagespace-network --images ./Images
   ./enable-imagespace.sh
   ```

### Overwriting the Existing Index

To overwrite the existing index with new images:

1. **Stop and Remove Existing Containers**:
   Stop the currently running containers and remove them to clear the previous state:

   ```shell
   cd Scripts/task4
   docker stop smqtk-postgres smqtk-services
   docker rm smqtk-postgres smqtk-services
   docker stop $(docker ps -q --filter "name=task4")
   docker rm $(docker ps -a -q --filter "name=task4")
   docker network rm task4_imagespace-network
   ```

2. **Recreate Containers with New Images**:
   Restart the Docker services with the new image directory specified:

   ```shell
   IMAGE_DIR=./Images/ docker-compose up -d
   ./smqtk_services.run_images.sh --docker-network task4_imagespace-network --images ./Images
   ./enable-imagespace.sh
   ```

### Managing Docker Containers

- **Stop Containers**:
  To simply stop the Docker containers:

  ```shell
  cd Scripts/task4
  docker stop smqtk-postgres smqtk-services
  docker stop $(docker ps -q --filter "name=task4")
  ```

- **Restart Containers**:
  To restart the Docker containers:

  ```shell
  cd Scripts/task4
  docker start smqtk-postgres smqtk-services
  docker stop $(docker ps -q --filter "name=task4")
  docker rm $(docker ps -a -q --filter "name=task4")
  IMAGE_DIR=./Images/ docker-compose up -d
  ```

### Retrieving Compressed Image Index

To retrieve the compressed image index:

```shell
cd Scripts/task4
./get_compressed_index.sh
```

### Access URLs

The services can be accessed via the following URLs:

- ImageSpace Interface: http://localhost:8989/
- Solr Interface for ImageSpace: http://localhost:8081/solr/

---

## Task 5

### GeoParser Server Start-up:
- Please move to the root directory of this project folder at first.
```shell
cd Scripts/task5/Docker
docker-compose up -d
cd ..
./create-core.sh
./add-fields.sh
```
- if you succeed in the start-up, you see:
  - http://localhost:8000/
  - http://localhost:8983/solr/

### Ingestion:
- Please move to the root directory of this project folder at first.
```shell
python Scripts/task5/ingest_BFdata.py
```

### Visualization:
1. Access to http://localhost:8000/
2. Click on Configure Index Tab
3. Set Domain Name to `bigfoot_index`.
4. Set Index Path to http://localhost:8983/solr/bigfoot/
5. Click on add index
6. Click on Database Icon Tab
7. Click on GeoParse button, and then wait (takes ~10 minutes)
8. Click on View button
---

## Work division

Ariel Martinez: Task 1 & 2: Visualization 2 (Map)

Kyosuke Chikamatsu: Task 3, 4, 5

Devashish Sonawane: Task 1 & 2: visualization 4 (Zoom Bubbles)

Willy Tang: Task 1 & 2: visualization 3 (Bubble Chart)

Ekaterina Shtyrkova: Task 2: visualization 5 (WordCloud)

Tomine Bergseth: Task 1 & 2: visualization 1 (Line Chart), create website

---
