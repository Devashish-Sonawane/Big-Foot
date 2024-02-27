import pandas as pd
from number_parser import parse, parse_number
import re
import pyperclip
from collections import Counter

bigfoot_df = pd.read_csv('dataset1/reports_task4-a_last.tsv', sep='\t', encoding='utf8')
# tuple(map(float, bigfoot_df['Location'][0].strip('()').split(', ')))

parsed_witnesses = bigfoot_df['Other Witnesses'].fillna('1').apply(parse)








data = parsed_witnesses
data_lower = data.str.lower()
# data_words = data_lower.apply(lambda x: ' '.join(re.findall(r'\w+', x)))
data_words = data_lower.apply(lambda x: ' '.join(re.findall(r'\w+', re.split(r'[.!?]', x)[0])))
data_words.sort_values().to_clipboard(index=False, header=False)
all_words = ' '.join(data_words).split()
pd.Series(all_words).value_counts().to_clipboard(index=True, header=False)

first_words = data_words.apply(lambda x: x.split()[0] if x.split() else '')
first_words.value_counts().to_clipboard(index=True, header=False)

# ========
# replace
# ========
data_removed_phrases = (data_words.str.replace(r'^there was ', '', regex=True).str.replace(r'^there were ', '', regex=True).str.replace(r'^there are ', '', regex=True).str.replace(r'^there where ', '', regex=True)
                        .str.replace(r'^there ', '', regex=True)
                        .str.replace(r'^\w+ly ', '', regex=True)
                        .str.replace(r'^approx ', '', regex=True)
                        .str.replace(r'^about ', '', regex=True)
                        .str.replace(r'^a total of ', '', regex=True)
                        .str.replace(r'^at least ', '', regex=True)
                        .str.replace(r'^it was ', '', regex=True)
                        .str.replace(r'^yes there was ', '', regex=True).str.replace(r'^yes there were ', '', regex=True).str.replace(r'^yes there are ', '', regex=True).str.replace(r'^yes there where ', '', regex=True)
                        .str.replace(r'^over ', '', regex=True)
                        .str.replace(r'^unfortunately ', '', regex=True)
                        .str.replace(r' freind ', ' friend ', regex=True)
                        .str.replace(r' girl friend ', ' girlfriend ', regex=True)
                        .str.replace(r' boy friend ', ' girlfriend ', regex=True)
                        .str.replace(r' g f ', ' girlfriend ', regex=True)
                        .str.replace(r' girfriend ', ' girlfriend ', regex=True)
                        .str.replace(r' my self ', ' myself ', regex=True)
                        .str.replace(r' self ', ' myself ', regex=True)
                        .str.replace(r' fiancee\b', ' fiance ', regex=True)
                        .str.replace(r' financee\b', ' fiance ', regex=True)
                        .str.replace(r' mum\b', ' mom ', regex=True)
                        .str.replace(r'^yeah ', 'yes ', regex=True)
                        )
# data_removed_phrases.sort_values().to_clipboard(index=False, header=False)

# ========
# filter by just words
# ========
person = 'wife/friend/husband/son/brother/father/dad/mother/sister/girlfriend/daddy/mom/daughter/cousin/uncle/boyfriend/fiance/buddy/aunt/partner/boss/best'.split('/')
data_filtered_phrases = data_removed_phrases[~data_removed_phrases.isin(
    ['yes','me','myself','just me','just myself','only me','only myself','wife','myself only'] +
    [s for s in person] +
    ['my ' + s for s in person] +
    ['yes my ' + s for s in person] +
    ['just my ' + s for s in person] +
    ['only my ' + s for s in person] +
    ['myself and my ' + s for s in person] +
    ['me and my ' + s for s in person]
)]
# data_filtered_phrases.sort_values().to_clipboard(index=False, header=False)

# ========
# filter by fist word
# ========
data_filtered_phrases2 = data_filtered_phrases[~data_filtered_phrases.str.contains(r'^[1-9] other', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^[1-9]\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^\d\d\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^(0|no|none|nobody)\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^(nope|not|sorry)\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^another\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^((i (am|was) )|myself )?alone\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^(yes )?((i (am|was) )|myself )?(just )?\w+ing\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^(i (am|was) )?by myself\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^i had \d\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^i was with \d\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^i was with \b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^we\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^(just|only)( the)? \d\b', regex=True)]

data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^yes \d\b', regex=True)]  # +1
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^total of \d\b', regex=True)]
# i/me/myself and | and i/me/myself
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^((just|yes|only) )?(i|me|myself) and( the)? \d\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^((just|yes|only) )?(i|me|myself) and\b', regex=True)]  # 2

data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^i (am|was) (the )?only\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases.str.contains(r'^(((just|yes|only) )?(my |a )?(' + '|'.join(person) + r') (and (me|myself|i)|was))\b', regex=True)]

# ========
# filter by fist word excluding 'and'
# ========
data_with_and_excluded = data_filtered_phrases2[~data_filtered_phrases2.str.contains(r'^.* and\b', regex=True)]
temp_excluded = data_filtered_phrases2[data_filtered_phrases2.str.contains(r'^.* and\b', regex=True)]
data_filtered_phrases2 = data_with_and_excluded[~data_with_and_excluded.str.contains(r'^(just|only) (me|myself)\b', regex=True)]
data_filtered_phrases2 = data_filtered_phrases2[~data_filtered_phrases2.str.contains(r'^((just|yes|only) )?(my |a )?(' + '|'.join(person) + r')\b', regex=True)]

data_filtered_phrases2.sort_values().to_clipboard(index=False, header=False)
data_filtered_phrases2 = pd.concat([data_filtered_phrases2, temp_excluded]).sort_index()
data_filtered_phrases2.sort_values().to_clipboard(index=False, header=False)


# ========
# fist word ranking
# ========
first_words = data_filtered_phrases2.apply(lambda x: x.split()[0] if x.split() else '')
first_words.value_counts().to_clipboard(index=True, header=False)

# ========
# after 'my'
# ========
words_after_my = data_filtered_phrases2.apply(lambda x: re.findall(r'\bmy (\w+)', x))
pd.Series([word for sublist in words_after_my for word in sublist]).value_counts().to_clipboard(index=True, header=False)





















pyperclip.copy('\n'.join(parsed_witnesses.tolist()))
filtered_df = parsed_witnesses[~parsed_witnesses.str.lower().str.contains(r'^[\d|no|none]', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'\d+ other', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'\d+ of us', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'just me and', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'just myself and', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'just me', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'just myself', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'alone', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'^myself and', regex=True)]
filtered_df = filtered_df[~filtered_df.str.lower().str.contains(r'^me and', regex=True)]
pyperclip.copy('\n'.join(filtered_df.tolist()))


count = parsed_witnesses.str.lower().apply(lambda x: re.findall(r'\w+', x)[0]).value_counts().sort_values(ascending=False)
count.to_clipboard()
parsed_witnesses.sort_values().to_clipboard(index=False)
def apply_regex(text):
    return re.sub(r'(\d+\s*ft)', '0', text)


replaced_witnesses = parsed_witnesses.str.replace('myself', '0').replace('me', '0')
replaced_witnesses = replaced_witnesses.apply(apply_regex)


i = 0
for row in replaced_witnesses.values:
    print(row)
    print(re.findall(r'\d+', parse(row)))
    i += 1
    if i == 10: break

# Dictionary to convert number words to digits
word_to_num = {
    "no": 0,
    "myself": 0,
    "me": 0,
    "no other witness": 0,
    "no other witnesses": 0,
}


text = parsed_witnesses[0]

def extract_witnesses_count(text):
    # Convert text to lowercase and tokenize
    text = text.lower()
    tokens = re.findall(r'\w+', text)

    if tokens[0].isdigit():
        return int(tokens[0])
    elif tokens[0] in ['no', 'none']:
        return 1

    # Initialize witnesses count
    count = 1
    multiple_flag = False

    for i, token in enumerate(tokens):
        # Check for direct numbers
        if token.isdigit():
            count += int(token)
        # Check for worded numbers and special phrases
        elif token in word_to_num:
            if word_to_num[token] == "multiple":
                multiple_flag = True
            else:
                count += word_to_num[token]
        # Check for patterns like "me and another person"
        elif token in ["me", "myself", "i"] and "and" in tokens[i:i + 3]:
            count += 1 + tokens[i + 3:i + 4].count("another")

    # Adjust for cases where "I" or equivalents are mentioned without quantifiers
    if "i" in tokens or "me" in tokens or "myself" in tokens:
        count = max(1, count)

    return count if not multiple_flag else "multiple"


witness_counts = [extract_witnesses_count(testimony) for testimony in testimonies]
witness_counts




sw = sw | set(person.split(', ')) | set(people.split(', '))
words_after_my = data_words_rr.str.extract(r'my (\w+)\s+(\w+)\s+(\w+)').stack().reset_index(drop=True)
words_after_my[~words_after_my.isin(sw)].value_counts().to_clipboard()
words_after_my = data_words_rr.str.extract(r'ex (\w+)').stack().reset_index(drop=True).value_counts().to_clipboard()
