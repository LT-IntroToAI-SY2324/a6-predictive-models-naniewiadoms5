# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

The R-Square coefficient for this model is 0.86. This means that the model has values close to the actual values in the line of best fit. 

2. Is your model accurate? Why or why not?

This model is relatively accurate because the R-Squared Coefficient is close to 1. When looking at the predicted vs actual values though, some values seem to way off from the actual value, while others are very close.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

The model predicts that a 10-year-old car with 89000 miles is worth 14074.85142599. The car that is 20 years old with 150000 miles is worth 10343.13239914. 

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Some of the predicted results are negative because the model may be not generalizing toward that specific data, like not having enough data for high values of mileage and age of the car because most people don't take the risk of keeping those kinds of cars. 