import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets-python-eec00310b52c.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('plan_retan')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)
sheet_instance2 = sheet.get_worksheet(1)

# get all the records of the data
records_data = sheet_instance.get_all_records()
records_data2 = sheet_instance2.get_all_records()

# convert the json to dataframe
df = pd.DataFrame.from_dict(records_data)
df2 = pd.DataFrame.from_dict(records_data2)


#print from df based condition 
#print(df[df['Grade']== 'B'])



