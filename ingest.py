import sys
import pandas as pd
import subprocess

file_path = sys.argv[1]

df = pd.read_csv(file_path)

df.to_csv("data_raw.csv", index = False)

print ("Data is loaded and saved")

subprocess.run(["python","preprocess.py","data_raw.csv"])