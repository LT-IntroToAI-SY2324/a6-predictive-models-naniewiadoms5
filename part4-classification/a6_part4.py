import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y

print(x)
print(y)

# Step 2: Standardize the data using StandardScaler, 

scaler = StandardScaler().fit(x)

# Step 3: Transform the data

x = scaler.transform(x)

# Step 4: Split the data into training and testing data

x_train, x_test, y_train, y_test = train_test_split(x, y)

# Step 5 & 6: Fit the data + create a LogsiticRegression object and fit the data

model = linear_model.LogisticRegression().fit(x_train, y_train)

# Step 7: Print the score to see the accuracy of the model

print("Accuracy:", model.score(x_test, y_test))
print("*************")
print("Testing Results:")
print("")
print(y_test)
for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 3)
    y_pred = int(model.predict(x))
    actual = y_test[index]


# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data

print(y_pred) 
print(actual)

# prediction
my_person = [[34, 56000, 1]]
numpy_array = np.array(my_person)

my_person_scaled = scaler.transform(my_person)
my_prediction = model.predict(my_person_scaled)
print(my_prediction)