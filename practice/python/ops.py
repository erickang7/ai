import os
import tarfile
import urllib
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = os.path.join("datasets", "sqlops_telemetry","")

def load_data(data_path = file_path, csv_file="dbo.carbonPerf.csv"):
    csv_path = os.path.join(data_path, csv_file)
    return pd.read_csv(csv_path)

ops_df = load_data(file_path)
valid_attributes = ["Platform", "AppVersion", "TotalMemory", "FreeMemory", "CPUCount", "CPUSpeed", "Ellapsed"]
ops_df = ops_df[valid_attributes]
print(ops_df.describe())

linux_df = ops_df[(ops_df["Platform"].str.lower() ==str('linux').lower())]
print(linux_df["Platform"].describe())
