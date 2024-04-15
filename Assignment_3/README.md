# DSCI 550 Spring 2024 Assignment 3 (Team 9)
This repository hosts the DSCI 550 Spring 2024 Assignment 3, ....

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

## Task 2

### Visualization 1:
- Navigate to Big-Foot\Assignment_3\Scripts\task1\task1_Bergseth.ipynb to run task_1_Bergseth.ipynb
  to create aggregated  dataset and associated json objects for this visualization.
- In the command line, navigate to the directory: cd Big-Foot\Assignment_3
- Start a python server by typing this command: python -m http.server
- If it doesn't open automatically, navigate to http://localhost:8000 or the url provided in the 
  command line.
- From the browser, navigate to Scripts/task2 and click on visualization_1.html to open and view the visualization.
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

Ariel Martinez: 

Kyosuke Chikamatsu: Task3, 4, 5

Devashish Sonawane: 

Willy Tang: 

Ekaterina Shtyrkova: 

Tomine Bergseth: Task5

---
