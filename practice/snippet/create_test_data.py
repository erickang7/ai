import numpy as np
import pandas as pd

###################################################
## snipets to create test set from pandas dataframe
###################################################

# split test data snippet
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

# create test data with hash when immutable identifier column exists
import hashlib
def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_hashid(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]

# creating an index column using row in pandas dataframe to deal with test set with hash
# for dataframe without an index column
dataframe: pd.DataFrame
dataframe_with_id = dataframe.reset_index() # creates "index" column using row id.

# using sklearn: pure randomization 
from sklearn.model_selection import train_test_split

# stratification 
# categorization technique
dataframe["stratified_column_name"] = np.ceil(dataframe["source_column_name"]/1.5) # 1.5 is a regularization coefficient
dataframe["stratified_column_name"].where(dataframe["stratified_column_name"]<5, 5.0, inplace=True)

from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(dataframe, dataframe["stratified_column_name"]):
    strat_train_set = dataframe.loc[train_index]
    strat_test_set = dataframe.loc[test_index]

# check stratified test set
strat_test_set["stratified_comun_name"].values_counts() / len (strat_test_set)

# clear the stratified attribute from the train and test sets after the cretion of test set.
for set_ in (strat_train_set, strat_test_set):
    set_.drop("stratified_column_name", axis=1, inplace=True)

### end of test set creation snippets