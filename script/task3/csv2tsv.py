import csv

input_csv = "data/reports.csv"
output_tsv = "dataset1/reports.tsv"

# open original csv
with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    # open tsv for writing
    with open(output_tsv, 'w', newline='', encoding='utf-8') as tsvfile:
        csvwriter = csv.writer(tsvfile, delimiter='\t')

        # Write rows read from CSV to TSV file
        for row in csvreader:
            csvwriter.writerow(row)
