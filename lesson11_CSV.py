import csv

import pandas
import pandas as pd

l_connect = [
    {"user_name":"user",
     "password":"password123"},
    {"user_name":"user1",
     "password":"password321"},
    {"user_name":"admin",
     "password":"321Qwerty"}
]

df1 = pandas.DataFrame(l_connect)
df2 = pandas.DataFrame(l_connect,)
df1.to_csv('simple.csv')

with pandas.ExcelWriter('simple.xlsx') as writer:
    df1.to_excel(writer,sheet_name="main",)

print(df1)
print(type(df1))
