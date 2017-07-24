import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("forestfires.csv")
print(csv.head(), "\n" )
print(csv.info(), "\n")
print(csv.describe(), "\n")

def mapper(month):
    month_to_num = {"jan":1, "feb":2, "mar":3, "apr":4, "may":5, "jun":6, "jul":7, "aug":8, "sep":9, "oct":10, "nov":11, "dec":12}
    return month_to_num[month]

print(csv["month"].value_counts())
csv["month"] = csv['month'].apply(mapper)
print(csv["month"].value_counts())
csv["month"].value_counts().plot(kind="bar", sort_columns=True)
plt.show()
