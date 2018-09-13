import pandas as pd

records = [("Nafly", "125"), ("Naflan", "120")]
df = pd.DataFrame.from_records(records)
print(df)

df = pd.DataFrame.from_records(records, columns=["Name", "Deposit"])
print(df)