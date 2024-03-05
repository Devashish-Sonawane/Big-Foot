import pandas as pd
from Task5TXT import *
from Task5PDF import *
from Task5PNG import *

if __name__ == "__main__":

    # Load the Bigfoot tsv (task 4 processed) into a pandas DataFrame
    tsv = pd.read_table('dataset1/reports_task4-e_last.tsv', encoding='utf8')
    tsv = pd.DataFrame(tsv)

    # Execute each Task 5 script sequentially, merging each dataset one after the other
    tsv = merge_txt(tsv)
    tsv = merge_pdf(tsv)
    tsv = merge_png(tsv)

    # Creates a tsv with the new merged data
    tsv.to_csv('dataset1/reports_task5.tsv', sep="\t", index=False) 
    
