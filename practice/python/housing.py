import os
import tarfile
import urllib
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt



downdload_root = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
housing_path = os.path.join("datasets", "housing","")
housing_url = downdload_root + housing_path + "housing.tgz"
print(housing_url)

def fetch_housing_data(housing_url=housing_url, housing_path=housing_path, housing_tgz="housing.tgz"):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    
    tgz_path = os.path.join(housing_path, housing_tgz)
    if not os.path.isfile (tgz_path):
        urllib.request.urlretrieve(housing_url, tgz_path)
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_path)
        housing_tgz.close()

def load_housing_data(housing_path = housing_path, housing_csv="housing.csv"):
    csv_path = os.path.join(housing_path, housing_csv)
    return pd.read_csv(csv_path)

fetch_housing_data(housing_url=housing_url, housing_path=housing_path)
housing_df = load_housing_data(housing_path)


print(housing_df.head())
print(housing_df.info())

print(housing_df["ocean_proximity"].value_counts())
print(housing_df.describe())

# housing_df.hist(bins = 50, figsize = (20,15))
# plt.show()