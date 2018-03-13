import os
import tarfile
import urllib
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split

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

train_set, test_set = train_test_split(housing_df, test_size=0.2, random_state=42)
print(len(train_set), "train +", len(test_set), "test_set")

housing_df["income_cat"] = np.ceil(housing_df["median_income"]/1.5)
housing_df["income_cat"].where(housing_df["income_cat"]<5, 5.0, inplace=True)

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing_df, housing_df["income_cat"]):
    strat_train_set = housing_df.loc[train_index]
    strat_test_set = housing_df.loc[test_index]

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

strat_train_set.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
    s=strat_train_set["population"]/100, label="population",
    c=strat_train_set["median_house_value"], cmap=plt.get_cmap("jet"), colorbar=True)
# plt.show()

corr_matric = strat_train_set.corr()
print(corr_matric["median_house_value"].sort_values(ascending=False))

from pandas.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing_df[attributes])

housing_df.plot(kind="scatter", x="median_house_value", y="median_income", alpha=0.1, figsize=(20,15))


# combination of attributes

housing_df["rooms_per_household"] = housing_df["total_rooms"] / housing_df["households"]
housing_df["bedrooms_per_room"] = housing_df["total_bedrooms"] / housing_df["total_rooms"]
housing_df["population_per_household"] = housing_df["population"] / housing_df["households"]
corr_matrix = housing_df.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))


#plt.show()