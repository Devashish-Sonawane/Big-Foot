# Import necessary libraries
import requests
import pandas as pd


# Define a function to capture image captions

def image_capture(file_path):
    # URL of the image captioning service
    url = 'http://localhost:8764/inception/v3/caption/image'
    # Open the image file in binary read mode
    with open(file_path, "rb") as f:
        # Post the image file to the service and capture the response
        response = requests.post(url, data=f)
    # Extract the caption from the response JSON and return it
    return response.json().get('captions')[0].get('sentence')


# Define a function to detect objects in an image

def object_detect(file_path):
    # URL of the object detection service
    url = 'http://localhost:8765/inception/v4/classify/image'
    # Open the image file in binary read mode
    with open(file_path, "rb") as f:
        # Post the image file to the service and capture the response
        response = requests.post(url, data=f)
    # Extract class names from the response, remove duplicates, and return as a comma-separated string
    return ', '.join(list(map(lambda x: x.split(', ')[0], response.json().get('classnames'))))


debug = True
if debug:
    df = pd.read_csv('Data/reports_v2.tsv', sep='\t', encoding='utf8')
    df = df.iloc[0:3].copy()
    df['Image URL'] = ['Dataset1/state_mammal/Picture1.png', 'Dataset1/state_mammal/Picture2.png', 'Dataset1/state_mammal/Picture3.png']
else:
    # Read the dataset after task5 process
    df = pd.read_csv('Dataset1/reports_v2_task5.tsv', sep='\t', encoding='utf8')

# Apply the image capture function to each row and store the results in a new column
df['Image Caption'] = df['Image URL'].apply(image_capture)

# Apply the object detection function to each row and store the results in another new column
df['Detected Objects'] = df['Image URL'].apply(object_detect)

# Save the dataframe with the new columns to a new TSV file
df.to_csv('Dataset1/reports_v2_task6.tsv', sep='\t', index=False)
