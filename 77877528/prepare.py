import pandas as pd

print("Load CSV.")
df = pd.read_csv("/app/ranger_trainig_data.csv")
print(f"CSV file has {df.shape[0]} rows.")
