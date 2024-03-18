import pandas as pd
from number_parser import parse, parse_number
import re
import random
import pyperclip

# A function to replace text in a DataFrame column using regex or plain text.
def replace(df, replace_from, replace_to, reg=False):
    dfc = df.copy()
    for rf, rt in zip(replace_from, replace_to):
        dfc = dfc.str.replace(rf, rt, regex=reg)
    return dfc

# Extracts an estimated witness count from a text description.
def extract_witnesses_count(text, psn, ppl):
    # For debugging purposes, a flag to log random samples.
    # flag = random.random() < 0.01
    flag = False
    res = None
    # Regex patterns to identify specific textual patterns regarding witness presence.
    no_head = r'^there\b(was|were|are|where)\b(no|none|nobody|not)\b'
    total_head = r'^((yes\b)?there\b(was\b|were\b|are\b|where\b)?|i was the only\b)?(a total of\b|just\b|only\b)?\d{1,2}\b'
    total_suffix = ['of us', 'all together', 'witnesses total']
    # Tokenize the text to analyze.
    tokens = re.findall(r'\w+', text)
    s = tokens[0]
    # Main logic to determine the witness count based on different textual cues.
    if bool(re.search(r'\b\d{1,2}\b', text)):
        # Various conditions to parse the text and deduce the witness count.
        # Detailed conditions omitted for brevity.
        if len(tokens) == 1:
            flag = False
            res = 1 + int(s)
        elif s in 'no none nobody nope not sorry'.split():
            res = 1
        elif re.match(no_head, text):
            res = 1
        elif s.isdigit() and 1 <= len(s) <= 2:
            if int(s) == 1:
                res = 1 + int(s)
            else:
                res = int(s) if ''.join(tokens[1:2]) not in ['other', 'others'] else 1 + int(s)
        elif re.match(total_head, text):
            res = int(re.search(r'\b\d{1,2}\b', text).group())
        else:
            res = 1 + len({t for t in tokens if t in psn})
            for i, word in enumerate(tokens):
                if re.match(r'\b\d{1,2}\b', word):
                    tokens_after_digit = tokens[i + 1:i + 3]
                    if ' '.join(tokens_after_digit) in total_suffix:
                        res = int(word)
                        break
                    for j, tad in enumerate(tokens_after_digit):
                        if j == 0 and tad in ['other', 'others']:
                            res += int(word)
                            break
                        elif tad in ppl:
                            res += int(word)
                            break
            if s == 'yes' and res == 1:
                res = 2
    else:
        # Fallback conditions when no direct numeric information is present.
        # Detailed conditions omitted for brevity.
        if s in 'no none nobody nope not sorry'.split():
            res = 1
        elif s == 'many':
            res = 5
        else:
            res = (1  # myself
                   + len({t for t in tokens if t in psn})
                   + 2 * len({t for t in tokens if t in ppl})  # assume plural words means two people were there
                   )
            if s == 'yes' and res == 1:
                res = 2
    # Debug output if the flag is set.
    if flag:
        print(res, '<===>', text)
    return res

# A function to analyze the frequency of words or phrases within a DataFrame column.
def wc(df, param='f'):
    if param == 'f':
        # Counts the frequency of the first word in each entry and copies the result to clipboard.
        first_words = df.apply(lambda x: x.split()[0] if x.split() else '')
        first_words.value_counts().to_clipboard(index=True, header=False)
    elif param == 'a':
        # Counts the frequency of all words across all entries and copies the result to clipboard.
        all_words = pd.Series(' '.join(df).split())
        all_words.value_counts().to_clipboard(index=True, header=False)
    elif param == 's':
        # Sorts the entries and copies them to clipboard.
        df.sort_values().to_clipboard(index=False, header=False)

# Calculates the percentage of entries in a series that match a given pattern.
def percent(series, pattern):
    matches = series.str.contains(pattern).sum()
    total = len(series)
    percentage = (matches / total) * 100
    return percentage
