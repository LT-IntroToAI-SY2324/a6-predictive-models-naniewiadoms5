import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("C:/Users/naniewiadoms@cps.edu/Documents/IntrotoAI/a6-predictive-models-naniewiadoms5/part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y

print("x values: ")
print(x)
print("y values: ")
print(y)

# Step 2: Standardize the data using StandardScaler, 

# scaler = StandardScaler()

# Step 3: Transform the data

# scaled_x = scaler.fit_transform(x)

# Step 4: Split the data into training and testing data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) #scaled_x insted of x for actual

# Step 5 & 6: Fit the data + create a LogsiticRegression object and fit the data

model = linear_model.LogisticRegression().fit(x_train, y_train)

# Step 7: Print the score to see the accuracy of the model

accuracy = model.score(x_test, y_test)
print("\n Accuracy of model:", accuracy)

y_pred = model.predict(x_test)

print("\n Actual ytest values:")
print(y_test)  

print("\n Predicted y values:")
print(y_pred)

# my_person = [[34, 56000, 1]]
# numpy_array = np.array(my_person)

# my_person_scaled = scaler.transform(my_person)
# my_prediction = model.predict(my_person_scaled)
# print(my_prediction)