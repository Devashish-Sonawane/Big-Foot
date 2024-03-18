# Import necessary libraries
import pandas as pd
from number_parser import parse, parse_number
import re
# from importlib import reload

# Import a custom module for extracting witness count
import script.task4.extract_witness_count as ewc

# Load Bigfoot sighting reports data from a TSV file
bigfoot_df = pd.read_csv('dataset1/reports_task4-a_last.tsv', sep='\t', encoding='utf8')

# Parse numeric values from the 'Other Witnesses' column, filling missing values with '0'
parsed_witnesses = bigfoot_df['Other Witnesses'].fillna('0').apply(parse)

# Preprocess to extract words from the first sentence, converting to lowercase and extracting alphanumeric words
data_words = parsed_witnesses.str.lower().apply(lambda x: ' '.join(re.findall(r'\w+', re.split(r'[.!?]', x)[0])))

# for debug
# reload(ewc)
# ewc.wc(data_words_rr, 's')
# ewc.wc(data_words, 'a')
# ewc.wc(data_words, 'f')

# Correct variations in notation for clarity and consistency
replace_str = ('freind:friend|freinds:friends|boy friend:boyfriend|girl friend:girlfriend|g f:girlfriend|girfriend:girlfriend|'
               'my self:myself|self:myself|fiancee:fiance|financee:fiance|mum:mom|yeah:yes|husban:husband|huband:husband|'
               'wifes:wives|daugher:daughter|roomate:roommate|girlfreind:girlfriend|neighors:neighbors|twin:twins|'
               'bf:boyfriend|sis:sister|siste:sister|(\\d{1,2})\\s\\d{1,2}:\\1')
# Prepare lists for replacement
tmp, replace_list_to = zip(*[pair.split(':') for pair in replace_str.split('|')])
replace_list_from = ['\\b' + w + '\\b' for w in tmp]
# Apply replacement rules
data_words_r = ewc.replace(data_words, replace_list_from, replace_list_to, True)

# Strip unnecessary words from the text
replace_list_to_null = [r'\b(\w+ly\s)', r'\b(approx\s)', r'\b(about\s)', r'\b(at least\s)', r'\b(over\s)',
                        r'^(it was\s)']
data_words_rr = ewc.replace(data_words_r, replace_list_to_null, [''] * len(replace_list_to_null), True)

# Define words that represent a single person and groups of people
person = ('wife, friend, brother, son, husband, father, sister, girlfriend, mother, mom, dad, daughter, partner, buddy, '
          'boyfriend, uncle, fiance, aunt, nephew, coworker, roommate, grandmother, grandma, niece, stepfather, grandson, '
          'neighbor, boss, girlfriend, sister, grandpa, cousin, exhusband, girl, driver, grandfather, chief, fisherman, '
          'pastor, guy, child, adult, lady')
people = ('friends, parents, children, brothers, kids, sons, roommates, uncles, fathers, neighbors, coworkers, classmates, '
          'girlfriends, buddies, sisters, mothers, cousins, twins, daughters, grandmothers, wives, people, adults')
# person_too_general = 'witness, member, person'  # good not to use
# people_too_general = 'witnesses, members, family'  # good not to use

# Count the number of witnesses based on the processed text
data_count = data_words_rr.apply(ewc.extract_witnesses_count, psn=person.split(', '), ppl=people.split(', '))
# Add the witness count to the dataframe
bigfoot_df['Witness Count'] = data_count
# Save the updated dataframe to a new TSV file
bigfoot_df.to_csv('dataset1/reports_task4-b_last.tsv', sep='\t', index=False)
