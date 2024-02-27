import pandas as pd
from number_parser import parse, parse_number
import re
import random
import pyperclip


def replace(df, replace_from, replace_to, reg=False):
    dfc = df.copy()
    for rf, rt in zip(replace_from, replace_to):
        dfc = dfc.str.replace(rf, rt, regex=reg)
    return dfc


def extract_witnesses_count(text, psn, ppl):
    # for debug
    flag = random.random() < 0.01
    res = None

    # tokenize
    tokens = re.findall(r'\w+', text)
    s = tokens[0]
    # main count
    if bool(re.search(r'\b\d{1,2}\b', text)):
        if s.isdigit() and 1 <= len(s) <= 2:
            if len(tokens) == 1:
                flag = False
                res = int(s)
            elif tokens[1] in ['other', 'others'] or s == '0':
                res = int(s) + 1
            else:
                res = int(s)
        elif s in 'no none nobody nope not sorry'.split():
            res = 1
        else:
            res = 1 + len({t for t in tokens if t in psn})
            for i, word in enumerate(tokens):
                if re.match(r'\b\d{1,2}\b', word):
                    tokens_after_digit = tokens[i + 1:i + 2]
                    if ' '.join(tokens_after_digit) == 'of us':
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
    # output
    if flag:
        print(res, '<===>', text)
    return res


def wc(df, param='f'):
    if param == 'f':
        first_words = df.apply(lambda x: x.split()[0] if x.split() else '')
        first_words.value_counts().to_clipboard(index=True, header=False)
    elif param == 'a':
        all_words = pd.Series(' '.join(df).split())
        all_words.value_counts().to_clipboard(index=True, header=False)
    elif param == 's':
        df.sort_values().to_clipboard(index=False, header=False)


def percent(series, pattern):
    matches = series.str.contains(pattern).sum()
    total = len(series)
    percentage = (matches / total) * 100
    return percentage
