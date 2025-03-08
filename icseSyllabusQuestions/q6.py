import pandas as pd
import json

data = pd.read_csv("/home/akshatkushwaha/DevDrive/eskoolwork/icseSyllabusQuestions/data.csv")
print(pd.DataFrame(data))

print(data.info())
print(data.tail())
print(data.head())

# with open('/home/akshatkushwaha/DevDrive/eskoolwork/icseSyllabusQuestions/data.json', 'r') as f:
#     data = json.load(f)

# data = pd.json_normalize(data)
# print(pd.DataFrame(data))