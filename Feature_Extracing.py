import pandas as pd

# STEP 1: Load your data
df = pd.read_csv("./combined_data.csv")

# Clean whitespace column names
df.columns = df.columns.str.strip()

# STEP 2: Convert Unix timestamp to datetime
# df['ctime'] = pd.to_datetime(df['ctime'], unit='s')

# STEP 3: Keep necessary columns only
df = df[['ctime', 'BatSOH', 'BatTemp', 'BatCycleCount', 'BatVolt', 'ThrottlePercent', 'BatCurrent', 'MotorTemp']]
df = df.dropna()
df = df.sort_values('ctime')

print(df.head())