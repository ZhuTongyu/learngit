## -*- coding: utf-8 -*-
#"""
#Created on Sat Mar 17 22:57:26 2018
#
#@author: ZTY
#"""
## To support both python 2 and python 3
#from __future__ import division, print_function, unicode_literals
#
#import numpy as np
#import os
#
#np.random.seed(42)
#import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
#
## Where to save the figures
#PROJECT_ROOT_DIR = "."
#CHAPTER_ID = "end_to_end_project"
#IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
#
#def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
#    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
#    print("Saving figure", fig_id)
#    if tight_layout:
#        plt.tight_layout()
#    plt.savefig(path, format=fig_extension, dpi=resolution)
#    
#import os
#import tarfile
#from six.moves import urllib
#
#DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
#HOUSING_PATH = os.path.join("datasets", "housing")
#HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
#
#def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
#    if not os.path.isdir(housing_path):
#        os.makedirs(housing_path)
#    tgz_path = os.path.join(housing_path, "housing.tgz")
#    urllib.request.urlretrieve(housing_url, tgz_path)
#    housing_tgz = tarfile.open(tgz_path)
#    housing_tgz.extractall(path=housing_path)
#    housing_tgz.close()
#    
#    
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
HOUSING_PATH = "datasets/housing"

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)
housing = load_housing_data(HOUSING_PATH)
#print(housing.head())  # pandas dataframe functioin 
#print(housing.info())
#print(housing["ocean_proximity"].value_counts())
#print(housing.describe())

#housing.hist(bins=50,figsize=(20,15))
#plt.show()  # optional (if the code is ignored, it will plot)
    
np.random.seed(42)   # 当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)
housing = train_set.copy()
#print(len(train_set), "train +", len(test_set), "test")    
    
#housing.plot(kind="scatter",x="longitude",y="latitude")   
#housing.plot(kind="scatter",x="longitude",y="latitude",alpha=0.1)  
#housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
#    s=housing["population"]/100, label="population", figsize=(10,7),
#    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
#    sharex=False)
#plt.legend()
#save_fig("housing_prices_scatterplot")  
corr_matrix = housing.corr()  
#print(corr_matrix["median_house_value"].sort_values(ascending=False))
from pandas.tools.plotting import scatter_matrix

attributes = ["median_house_value","median_income","total_rooms",
              "housing_median_age"]
#scatter_matrix(housing[attributes],figsize=(12,8))

housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]

corr_matrix = housing.corr() 
#print(corr_matrix["median_house_value"].sort_values(ascending=False))

housing = train_set.drop("median_house_value",axis=1)  #delete target value attribute(remain 9 attribute)
housing_labels = train_set["median_house_value"].copy()

# 数据缺损处理
#housing.dropna(subset=["total_bedrooms"]) #删除那些缺数据的instance
#housing.drop("total_bedrooms",axis=1)# delete the attribute column
#median = housing["total_bedrooms"].median()
#housing["total_bedrooms"].fillna(median)

from sklearn.preprocessing import Imputer
imputer = Imputer(strategy="median")
housing_num = housing.drop("ocean_proximity",axis=1)
    
imputer.fit(housing_num)
#print(imputer.statistics_)
#print(housing_num.median().values)
X = imputer.transform(housing_num)
housing_tr = pd.DataFrame(X, columns=housing_num.columns)
















