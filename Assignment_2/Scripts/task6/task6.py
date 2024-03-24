# Import necessary libraries
import requests
import pandas as pd
import re


# Define a function to capture image captions

def image_capture(row):
    file_path = re.search(r'Dataset1/Images/[^/]+\.png', row['Image URL']).group(0)
    # URL of the image captioning service
    url = 'http://localhost:8764/inception/v3/caption/image'
    # Open the image file in binary read mode
    with open(file_path, "rb") as f:
        # Post the image file to the service and capture the response
        response = requests.post(url, data=f)
    # Extract the caption from the response JSON and return it
    print(row.name, ': ', response.json().get('captions')[0].get('sentence'))
    return response.json().get('captions')[0].get('sentence')


# Define a function to detect objects in an image

def object_detect(row):
    file_path = re.search(r'Dataset1/Images/[^/]+\.png', row['Image URL']).group(0)
    # URL of the object detection service
    url = 'http://localhost:8765/inception/v4/classify/image'
    # Open the image file in binary read mode
    with open(file_path, "rb") as f:
        # Post the image file to the service and capture the response
        response = requests.post(url, data=f)
    # Extract class names from the response, remove duplicates, and return as a comma-separated string
    print(row.name, ': ', response.json().get('classnames'))
    return ', '.join(list(map(lambda x: x.split(', ')[0], response.json().get('classnames'))))


# Read the dataset after task5 process
df = pd.read_csv('Dataset1/reports_v2_task5.tsv', sep='\t', encoding='utf8')

debug = False
if debug:
    df = df.iloc[0:3].copy()

# Apply the image capture function to each row and store the results in a new column
print('--------- Image Captioning ---------')
df['Image Caption'] = df.apply(image_capture, axis=1)

# Apply the object detection function to each row and store the results in another new column
print('--------- Object Detection ---------')
df['Detected Objects'] = df.apply(object_detect, axis=1)

# Save the dataframe with the new columns to a new TSV file
df.to_csv('Dataset1/reports_v2_task6.tsv', sep='\t', index=False)
