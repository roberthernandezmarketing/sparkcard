# Verify if the CSV file is well formatted

import pandas as pd

# Cargar el CSV

path = "C:/Users/rober/OneDrive/Desktop/Coding_for_living/Rob-DVLP2024/sparkcard/app/services/"
file = (f"{path}cards.csv")
       
df = pd.read_csv(file, sep=",")  

for col in df.columns:
    print(f"{col}: ", end="")  
    print(df[col][0])       

print (f"\nTotal registros: {len(df)}")
