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

### How to run:
- Run task5.ipynb in Google Colab using the GPU option. The script can be found under Assignment_2/Scripts/task5.
- In order to run the script through Google Colab, the directory must be uploaded to Google Drive.

### Notes on implememtion:
- Image generation method: I used the diffusers StableDiffusionPipeline to generate the images.
- Text columns I joined: Observed, Observed.1, Environment, Time And Conditions, Season, and Witness Count.
  - The StableDiffusionPipeline only takes 77 tokens. For most rows, the above gives significantly more than 77 tokens;
  however, in cases where the preprocessed text resulted in less than 77 tokens, I also added
  Also Noticed, Headline, Time And Conditions, and Location Details to have text to generate the image.
  - As mentioned, the StableDiffusionPipeline only takes 77 tokens. In order to select 77 tokens
  appropriately I preprocess the text to remove punctuation, special characters, convert to lowercase,
  and convert easy numbers to text using the number parser and in cases where it does not convert it
  I take out multi-digit numbers as the StableDiffusionPipeline seems to separate each digit in
  a number and count it as a separate token which led to a larger mismatch between my token count using
  NLTK and the token count from the generator. There are still certain numbers from time objects left
  I believe and a slight mismatch in token count for some rows but this allowed me to select the
  most relevant tokens centering the description of BigFoot.
- The Image Text I use as the image cpation is added in a column called "Image Text".
- The local relative url for the image paths are added in a column "Image URL" to help keep track
of which image belongs to which row. The images are also labeled image_{index}.png to keep track.

### Output:
- Dataset1/reports_v2_task5.tsv
- Dataset1/Images

---

## Task 6

#### Requirements:

- Task 5 must have been executed previously (`reports_v2_task5.tsv` and `dataset1/Images/image_XXXX.png` must have been generated).

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

#### Requirements:

- Install: Lucene-geo-gazetteer, Tika, Geotopic-mime and the Ner-model. (https://cwiki.apache.org/confluence/display/TIKA/GeoTopicParser)
  
- Code MUST be run in Python 2.7 (parser won't work correctly otherwise)
  
- Do to complications during the parser instalation, code MUST be run in the same folder as the:
  ner-model folder, tika server jar, tika nlp jar, tika client jar, and geotopic mime folder

- Recomended the use of Linux (or Windows Subsystem for Linux) for execution


#### Execution:
- Please move to the root directory of this project folder at first. And be sure to follow the requirements.

- Terminal 1:
```shell
lucene-geo-gazetteer -server
```
- Terminal 2:
```shell
java -classpath ner-model:tika-server-standard-2.9.1.jar:tika-parser-nlp-package-2.9.1.jar org.apache.tika.server.core.TikaServerCli
```
- Terminal 3:
```shell
python2 test.py
```

#### Output:
- `Dataset1/reports_v2_task7.tsv`

---

## Task 8

---

## Work division

Ariel Martinez: Task7

Kyosuke Chikamatsu: Task6

Devashish Sonawane: 

Willy Tang: 

Ekaterina Shtyrkova: 

Tomine Bergseth: 

---
