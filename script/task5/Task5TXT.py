import pandas as pd

def merge_txt(tsv):

    # Alcohol dataset location
    input = 'data/pcyr1970-2021.txt'

    # This is location of data in original file
    line_number = 130

    # Dictionary to change values in State Column
    fips_to_state = {
        "01": "Alabama", "02": "Alaska", "04": "Arizona", "05": "Arkansas",
        "06": "California", "08": "Colorado", "09": "Connecticut", "10": "Delaware",
        "1": "Alabama", "2": "Alaska", "4": "Arizona", "5": "Arkansas", "6": "California", "8": "Colorado", "9": "Connecticut",
        "11": "District of Columbia", "12": "Florida", "13": "Georgia", "15": "Hawaii",
        "16": "Idaho", "17": "Illinois", "18": "Indiana", "19": "Iowa", "20": "Kansas",
        "21": "Kentucky", "22": "Louisiana", "23": "Maine", "24": "Maryland", "25": "Massachusetts",
        "26": "Michigan", "27": "Minnesota", "28": "Mississippi", "29": "Missouri", "30": "Montana",
        "31": "Nebraska", "32": "Nevada", "33": "New Hampshire", "34": "New Jersey", "35": "New Mexico",
        "36": "New York", "37": "North Carolina", "38": "North Dakota", "39": "Ohio", "40": "Oklahoma",
        "41": "Oregon", "42": "Pennsylvania", "44": "Rhode Island", "45": "South Carolina",
        "46": "South Dakota", "47": "Tennessee", "48": "Texas", "49": "Utah", "50": "Vermont",
        "51": "Virginia", "53": "Washington", "54": "West Virginia", "55": "Wisconsin",
        "56": "Wyoming", "91": "Northeast Region", "92": "Midwest Region", "93": "South Region", "94": "West Region", "99": "United States"}

    # Dictionary to change values in Type of beverage Column
    type_of_beverage = { '1': 'Spirits', '2': 'Wine', '3': 'Beer', '4': 'All beverages'}

    # List with Column Names
    column_names = ['Fixed Year','State','Type of beverage','Gallons of beverage','Gallons of ethanol (absolute alcohol)',
                    'Population (age 14 and older)','Gallons of ethanol per capita age 14 and older',
                    'Decile for per capita consumption age 14 and older','Population (age 21 and older)',
                    'Gallons of ethanol per capita age 21 and older','Decile for per capita consumption age 21 and older',
                    'Type of data source','Time-varying alcohol by volume (ABV)','Gallons of ethanol derived from time-varying ABV']

   

    # Filehandles for input and output file
    table = []
    with open(input, 'r') as filehandle:

    # Processing data from line 130 and onwards
        for current_line_number, line in enumerate(filehandle, start = 1):
            if current_line_number >= line_number:

    # Detecting any invalid inputs which can cause errors in processing data
                if line in ['','\n','\t',' ']:
                    print(f"{current_line_number} is invalid")

    # Removing Spaces and writing N/A for blank values
                else:
                    col1 = line[0:4].strip().replace('.','None') or 'None'
                    col2_fips = line[5:7].strip().replace('.','') or ""
                    col2 = fips_to_state.get(col2_fips, col2_fips)
                    col3_id = line[8].strip().replace('.','') or ""
                    col3 = type_of_beverage.get(col3_id, col3_id)
                    col4 = line[10:20].strip().replace('.','None') or 'None'
                    col5 = line[21:30].strip().replace('.','None') or 'None'
                    col6 = line[31:41].strip().replace('.','None') or 'None'
                    col7 = line[42:48].strip().replace('.','None') or 'None'
                    col8 = line[49:51].strip().replace('.','None') or 'None'
                    col9 = line[52:62].strip().replace('.','None') or 'None'
                    col10 = line[63:68].strip().replace('.','None') or 'None'
                    col11 = line[69:71].strip().replace('.','None') or 'None'
                    col12 = line[72].strip().replace('.','None') or 'None'
                    col13 = line[74:77].strip().replace('.','None') or 'None'
                    col14 = line[78:87].strip().replace('.','None') or 'None'

                    if col1 == 'None':
                        col1 = None
                    else:
                        col1 = int(col1)
                    colL =  [col1,str(col2),str(col3),col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14]
                    for count, col in enumerate([col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14]):
                        if col == 'None':
                            colL[count+3]=None
                        else:
                            colL[count+3]=int(colL[count+3])


    # Writing data to table
                    table.append(colL)
                    

    # Load the table file into a DataFrame
    df = pd.DataFrame(table, columns = column_names) 

    # Filter rows based on the 'Type of beverage' column
    filtered_df = df[df['Type of beverage'] == 'All beverages']

    # Drop the specified columns 
    columns_to_drop = ['Gallons of beverage', 'Type of beverage', 'Type of data source', 'Time-varying alcohol by volume (ABV)']
    filtered_df = filtered_df.drop(columns=columns_to_drop)

    # Merge the two DataFrames on the specified columns
    merged_df = pd.merge(tsv, filtered_df, how='left', left_on=['Fixed Year', 'State'], right_on=['Fixed Year', 'State'])
    colInt = ['Gallons of ethanol (absolute alcohol)',
                        'Population (age 14 and older)','Gallons of ethanol per capita age 14 and older',
                        'Decile for per capita consumption age 14 and older','Population (age 21 and older)',
                        'Gallons of ethanol per capita age 21 and older','Decile for per capita consumption age 21 and older',
                        'Gallons of ethanol derived from time-varying ABV']
    
    # Make column type to integer
    for col in colInt:
        merged_df[col] =  merged_df[col].astype(pd.Int64Dtype())

    # Return merged dataset
    return merged_df

