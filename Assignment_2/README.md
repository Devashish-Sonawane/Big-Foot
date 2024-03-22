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

## Task 5

---

## Task 6

#### Requirements:

- Task 5 must have been executed previously (`dataset1/XXXXX.tsv` and `dataset1/image/XXXX.jpg` must have been generated).

- Docker Desktop must have been installed and run previously (Please refer to https://docs.docker.com/desktop/install/mac-install/).
  Windows users need to install Linux distribution by using WSL as well (Please refer to https://learn.microsoft.com/ja-jp/windows/wsl/install).
  In addition, Windows users need to have docker enable integration with the Linux distribution (Please check Settings/Resources/WSL integration on your Docker Desktop).
  Windows users will execute Docker commands in your Linux distribution terminal. Mac users will execute Docker commands in your terminal.

#### Tika Image Captioning REST API Server Start-up:
- Windows users need to use your Linux Distribution (not PowerShell/Command Prompt). Mac users need to use your Terminal.
- Please move to the root directory of this project folder at first.
```shell
cd Scripts/task6/
docker-compose up -d
```
- if you succeed in the start-up, you see:
  - http://localhost:8764/
  - http://localhost:8765/

#### Execution:
- Please move to the root directory of this project folder at first.
```shell
python Scripts/task6/task6.py
```

#### Output:
- `Dataset1/reports_v2_task6.tsv`

---

## Task 7

---

## Task 8

---

## Work division

Ariel Martinez: 

Kyosuke Chikamatsu: 

Devashish Sonawane: 

Willy Tang: 

Ekaterina Shtyrkova: 

Tomine Bergseth: 

---
