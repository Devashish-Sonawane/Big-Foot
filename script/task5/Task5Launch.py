import pandas as pd
from Task5TXT import *
from Task5PDF import *
from Task5JPG import *

if __name__ == "__main__":
    tsv = pd.read_table('dataset1/reports_task4-e_last.tsv', encoding='utf8')
    tsv = pd.DataFrame(tsv)

    tsv = merge_txt(tsv)
    tsv = merge_pdf(tsv)
    tsv = merge_jpg(tsv)

    tsv.to_csv('dataset1/reports_task5.tsv', sep="\t", index=False) 
    