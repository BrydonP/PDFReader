from PyPDF2 import PdfReader
import os, csv, json

# Output Location
output = 'Output/'

# Input Files
file_path = "/Files/Type1/"
fileList = os.listdir(os.getcwd() + file_path)

# Create Blank Dictionary
dataDict = {}
dataList = []
file_name = os.path.basename(file_path)

# Look at the first file and store its Fields
reader = PdfReader(os.getcwd() + file_path + fileList[0]) # Select File
csvDict = reader.get_fields().keys() # Stores all fields names in a Dict
form_fields = list(csvDict) # List of all Fields Names

for idx, file in enumerate(fileList):
    reader = PdfReader(os.getcwd() + file_path + fileList[idx]) # Iterate through files in list
    dataDict = reader.get_fields() # Stores the Raw data in Field Names : Data Pairs
    # Add Updated Data in Dict for each file
    for idx, data in enumerate(form_fields):
        dataDict[form_fields[idx]] = dataDict[form_fields[idx]].value.replace("\n","")

    dataList.append(dataDict)
    print("File Completed: " + dataDict[form_fields[1]])

# Create & Export CSV File
with open(output + 'data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=dataDict.keys())
    writer.writeheader()
    writer.writerows(dataList)

print("Process Completed")
###############################################################################

#REPO
# Add form data to List
#for idx, data in enumerate(form_fields):
#    dataList.append(dataDict[form_fields[idx]].value.replace("\n","")) 

#print(dataDict['OSS NAME'].value) # Prints JUST the value based on the Dict Key. 

###############################################################################