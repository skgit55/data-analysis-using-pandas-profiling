import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('csv_file_path')
print(df)

profile= ProfileReport(df)
profile.to_file(output_file='report.html')