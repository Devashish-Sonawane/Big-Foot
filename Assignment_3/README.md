# Big-Foot
This is a shared repository containing data from Big Foot Field Researchers Organization (BFRO).

---
## Installation of required libraries

To install write in the command line (while in the same folder as requirements.txt):

```shell
pip install -r requirements.txt
```
'pip' must be previously installed.

---

## Task 5

#### Requirements:

- Docker Desktop must have been installed and run previously (Please refer to https://docs.docker.com/desktop/install/mac-install/).
  Windows users need to install Linux distribution by using WSL as well (Please refer to https://learn.microsoft.com/ja-jp/windows/wsl/install).
  In addition, Windows users need to have docker enable integration with the Linux distribution (Please check Settings/Resources/WSL integration on your Docker Desktop).
  Windows users will execute Docker commands in your Linux distribution terminal. Mac users will execute Docker commands in your terminal.

#### GeoParser Server Start-up:
- Windows users need to use your Linux Distribution (not PowerShell/Command Prompt). Mac users need to use your Terminal.
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

#### Ingestion:
- Please move to the root directory of this project folder at first.
```shell
python Scripts/task5/ingest_BFdata.py
```

---

## Work division

Ariel Martinez: Task7

Kyosuke Chikamatsu: Task6

Devashish Sonawane: 

Willy Tang: 

Ekaterina Shtyrkova: 

Tomine Bergseth: Task5

---
