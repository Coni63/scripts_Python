import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from pandas.plotting import scatter_matrix

from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer, StandardScaler, Imputer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

housing = pd.read_csv("housing.csv")
print(housing.head(), "\n" )
print(housing.info(), "\n")
print(housing.describe(), "\n")
print(housing["ocean_proximity"].value_counts(), "\n")

######################################################
############ Explore datas ###########################
######################################################

# housing.hist(bins=50, column="median_house_value") #, column="total_rooms"
# plt.show()

# housing.plot(
#              kind="scatter",
#              x="longitude",
#              y="latitude",
#              alpha = 0.1,
#              s = housing["population"]/100,
#              label = "population",
#              c = housing["median_house_value"],
#              cmap=plt.get_cmap("jet"),
#              colorbar = True
#             )
# plt.show()

# corr_matrix = housing.corr()
# print(corr_matrix, "\n")

# attributes = ["median_house_value","median_income","total_rooms","housing_median_age"]
# pd.plotting.scatter_matrix(housing[attributes], figsize = (12,8))
# plt.show()

# housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
# housing["bedrooms_per_rooms"] = housing["total_bedrooms"]/housing["total_rooms"]
# housing["population_per_household"] = housing["population"]/housing["households"]
#
# corr_matrix = housing.corr()
# print(corr_matrix)
#
# attributes = ["bedrooms_per_rooms", "median_house_value"]
# pd.plotting.scatter_matrix(housing[attributes], figsize = (12,8))
# plt.show()

######################################################
############ Split datas ###########################
######################################################

# # random_state pour avoir le meme split toujours
#
# # On 'utilise pas train_test_split car income est continu et doit etre discretise
# # train_set, train_test = train_test_split(housing, test_size=0.2, random_state=42)
#
# housing["median_income_new"] = np.ceil(housing["median_income"] / 1.5)
# housing["median_income_new"].where(housing["median_income_new"] < 5, 5.0, inplace=True)
#
# split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
# for train_index, test_index in split.split(housing, housing["median_income_new"]):
#     train_set = housing.loc[train_index]
#     train_test = housing.loc[test_index]
#
# # just back to original
# for set_ in (train_set, train_test):
#     set_.drop("median_income_new", axis = 1, inplace = True)

housing, train_test = train_test_split(housing, test_size=0.2, random_state=42)

housing_label = housing["median_house_value"].copy()
housing = housing.drop("median_house_value", axis=1)

######################################################
############ Prepare datas ###########################
######################################################

# # replaced afterward by LabelBinarizer
# encoder_LE = LabelEncoder()
# encoder_OHE = OneHotEncoder()
# housing_cat_encoded = encoder_LE.fit_transform(housing["ocean_proximity"])
# housing_cat_1hot = encoder_OHE.fit_transform(housing_cat_encoded.reshape(-1, 1))
# print(housing_cat_1hot, "\n")


encoder = LabelBinarizer(sparse_output=True)
housing_cat_1hot = encoder.fit_transform(housing["ocean_proximity"])
print(housing_cat_1hot, "\n")

imputer = Imputer(strategy="median")
housing_num = housing.drop("ocean_proximity", axis=1)
# imputer.fit(housing_num)

rooms_ix, household_ix, population_ix, bedrooms_ix = 3, 6, 5, 4

class DataFrameSlector(BaseEstimator, TransformerMixin):
    def __init__(self, attr_name):
        self.attribute_names = attr_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


num_attr = list(housing_num)
print(num_attr)
cat_attr = ["ocean_proximity"]

num_pipeline = Pipeline([
    ('selector', DataFrameSlector(num_attr)),
    ('imputer', Imputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('selector', DataFrameSlector(cat_attr)),
    ('label_binarizer', LabelBinarizer())
])

full_pipeline = FeatureUnion(transformer_list=[
    ("num_pipeline", num_pipeline),
    ("cat_pipeline", cat_pipeline)
])

housing_prepared = full_pipeline.fit_transform(housing)

print(housing_prepared.shape, "\n")

######################################################
############ Create Model  ###########################
######################################################

# lin_reg = LinearRegression()
# lin_reg.fit(housing_prepared, housing_label)
#
# some_data = housing.iloc[:5]
# some_labels = housing.iloc[:5]
# some_data_prepared = full_pipeline.transform(some_data)
# print("Prediction", lin_reg.predict(some_data_prepared))
# print("Labels ", list(some_labels))
# housing_prediction = lin_reg.predict(housing_prepared)
# lin_mse = mean_squared_error(housing_label, housing_prediction)
# lin_rmse = np.sqrt(lin_mse)
# print(lin_rmse)
#
# #resultat bof, on passe sur decision tree
# tree_reg = DecisionTreeRegressor()
# tree_reg.fit(housing_prepared, housing_label)
# print("Prediction", tree_reg.predict(some_data_prepared))
# print("Labels ", list(some_labels))
#
# housing_prediction = tree_reg.predict(housing_prepared)
# tree_mse = mean_squared_error(housing_label, housing_prediction)
# tree_rmse = np.sqrt(tree_mse)
# print(tree_rmse, "\n")
#
# #3eme test avec Random forest
# forest_reg = RandomForestRegressor()
# forest_reg.fit(housing_prepared, housing_label)
# print("Prediction", forest_reg.predict(some_data_prepared))
# print("Labels ", list(some_labels))
#
# housing_prediction = forest_reg.predict(housing_prepared)
# forest_mse = mean_squared_error(housing_label, housing_prediction)
# forest_rmse = np.sqrt(forest_mse)
# print(tree_rmse, "\n")
#
# # Cross validation avec Kfold cross validation
# scores = cross_val_score(lin_reg, housing_prepared, housing_label, scoring="neg_mean_squared_error", cv=10)
# lin_rmse_scores = np.sqrt(-scores)
# print("Scores", lin_rmse_scores)
# print("Mean", lin_rmse_scores.mean())
# print("Stdev", lin_rmse_scores.std(), "\n")
#
# scores = cross_val_score(tree_reg, housing_prepared, housing_label, scoring="neg_mean_squared_error", cv=10)
# tree_rmse_scores = np.sqrt(-scores)
# print("Scores", tree_rmse_scores)
# print("Mean", tree_rmse_scores.mean())
# print("Stdev", tree_rmse_scores.std(), "\n")
#
# scores = cross_val_score(forest_reg, housing_prepared, housing_label, scoring="neg_mean_squared_error", cv=10)
# forest_rmse_scores = np.sqrt(-scores)
# print("Scores", forest_rmse_scores)
# print("Mean", forest_rmse_scores.mean())
# print("Stdev", forest_rmse_scores.std(), "\n")


######################################################
############ Fine tuning   ###########################
######################################################

# param_grid = [
#     {'n_estimators': [30, 50, 70], 'max_features': [4,6,8]},
#     #{'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2,3,4]},
# ]
#


# forest_reg = RandomForestRegressor()
# grid_search = GridSearchCV(forest_reg, param_grid, cv = 5, scoring='neg_mean_squared_error')
# grid_search.fit(housing_prepared, housing_label)
#
# print(grid_search.best_params_)
#
# cvres = grid_search.cv_results_
# for mean_scores, params in zip(cvres["mean_test_score"], cvres["params"]):
#     print(np.sqrt(-mean_scores), params)

#on garde 'max_features': 8, 'n_estimators': 30

######################################################
############ Test Set   ###########################
######################################################

param_grid = [
    {'n_estimators': [30], 'max_features': [8]}
]

forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv = 5, scoring='neg_mean_squared_error')
grid_search.fit(housing_prepared, housing_label)

X_test = train_test.drop("median_house_value", axis = 1)
Y_test = train_test["median_house_value"].copy()

X_test_prepared = full_pipeline.transform(X_test)
final_prediction = grid_search.predict(X_test_prepared)

final_rmse = np.sqrt(mean_squared_error(Y_test, final_prediction))
print(final_rmse)