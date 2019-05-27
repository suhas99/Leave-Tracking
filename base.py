import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint,yaml
import pandas as pd
from datetime import date
import string

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(cred)
sheet = client.open("Leavetrackingsheet").sheet1
pp = pprint.PrettyPrinter()
result = sheet.get_all_records()
temp = pd.DataFrame(result)

print(temp)

#pp.pprint(type(temp))
def clean(temp):
	temp=temp[temp.Day != 'Saturday']
	temp=temp[temp.Day!='Sunday']
	temp=temp[temp.Day!='Holiday']
	#days_aval_month=temp['Date'].count()
 	return temp
temp=clean(temp)

sd=temp["Start Date"][0]
ed=temp["End Date"][0]
sm,sd=str.split(sd,'/')
em,ed=str.split(ed,"/")

ran=int(ed)-int(sd)

print(temp, range)
