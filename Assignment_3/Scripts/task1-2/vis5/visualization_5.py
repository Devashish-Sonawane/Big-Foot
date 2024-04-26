import json
from collections import Counter
import re
from nltk.corpus import stopwords

# Load stopwords
stop_words = set(stopwords.words('english'))

# Load the JSON file
with open('BFRO.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Define the columns to extract
columns_to_extract = ["Observed", "Also Noticed", "Other Witnesses", 
                      "Other Stories", "Time And Conditions", 
                      "Environment", "Follow-Up Report"]

# Extract text from specified columns
words = []
for entry in data['BFRO']:
    for column in columns_to_extract:
        text = entry.get(column, '')
        if isinstance(text, str):
            # Convert to lowercase and split into words
            words.extend(re.findall(r'\b\w+\b', text.lower()))

# Remove stop words and digits
filtered_words = [word for word in words if word not in stop_words and not word.isdigit()]

# Count occurrences of each word
word_counts = Counter(filtered_words)

# Get the 500 most common words
top_500_words = word_counts.most_common(500)

# Write word counts to a new JSON file
with open('BFRO_vis_5.json', 'w', encoding='utf-8') as output_file:
    json.dump(top_500_words, output_file, ensure_ascii=False, indent=4)
