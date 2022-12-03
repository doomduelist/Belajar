import gspread
from oauth2client.service_account import ServiceAccountCredentials 
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

# client.open("koneksi").add_worksheet(title="worksheet contoh",rows=1000,cols=20)
worksheets = client.open("Koneksi").worksheet("data_kontak")
# client.open("koneksi").del_worksheet(worksheets)

list_data = worksheets.get_all_records()

dataframe = pd.DataFrame(list_data)

# data_baru = pd.DataFrame.from_records({'no.wa': ['6289608525682'],'nama': ['dimas'],'pesan': ['hai dimas'], 'status': ['4']})

# dataframe = pd.concat([dataframe,data_baru])

# dataframe.loc[dataframe['no.wa'] == 628587490345, ['nama']] = "Astia"

# set_with_dataframe(worksheets,dataframe)
# print(dataframe)

filterData = 2+dataframe[(dataframe['no.wa'] == 6289608525682) & (dataframe['status'] == 4)].index.item()
worksheets.delete_row(filterData)

print(filterData)