import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv")
#print(data)
"""
OUT:
        TV  Radio  Newspaper  Sales
0    230.1   37.8       69.2   22.1
1     44.5   39.3       45.1   10.4
2     17.2   45.9       69.3   12.0
3    151.5   41.3       58.5   16.5
4    180.8   10.8       58.4   17.9
..     ...    ...        ...    ...
195   38.2    3.7       13.8    7.6
196   94.2    4.9        8.1   14.0
197  177.0    9.3        6.4   14.8
198  283.6   42.0       66.2   25.5
199  232.1    8.6        8.7   18.4

[200 rows x 4 columns]
"""
#print(data.isnull().sum())
"""
OUT:
TV           0
Radio        0
Newspaper    0
Sales        0
dtype: int64
"""

figure = px.scatter(data_frame = data, x="Sales",
                    y="TV", size="TV", trendline="ols")
figure.show()

figure = px.scatter(data_frame = data, x="Sales",
                    y="Newspaper", size="Newspaper", trendline="ols")
figure.show()

figure = px.scatter(data_frame = data, x="Sales",
                    y="Radio", size="Radio", trendline="ols")
figure.show()

correlation = data.corr()
print(correlation["Sales"].sort_values(ascending=False))
"""
OUT:
Sales        1.000000
TV           0.901208
Radio        0.349631
Newspaper    0.157960
Name: Sales, dtype: float64
"""

#split the data into training and test sets
x = np.array(data.drop(["Sales"], 1))
y = np.array(data["Sales"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2,  random_state=42)

#train the model to predict future sales
model = LinearRegression()
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

#input values into the model according to the features we have used to train
#features = [[TV, Radio, Newspaper]]
features = np.array([[153.1, 307.8, 9.2]])
print(model.predict(features))

"""
OUT:
[44.17037546]
"""
