# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this lenear regression model?

The r^2 value is the coefficient of determination; the model got 0.0.6257932855322312. It is calculated based on a line of best fit, measuring the distance between each point to that line. It will show how well the model the data points got predicted by the model based on the linear relationship.

2. According to your model, what is the predicted systolic blood pressure for a person iwho is 43 years old?

When a person is 43 years old the predicted systolic blood pressure would be, 137.46185286 mmHg. 

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?

Based on the scatter plot printed by matplotlib and the r^2 value, I see that the points are only a little correlated to the line of best fit, despite there being a relationship between aging and blood pressure. Some points are far outliers, while most are close, making the r^2 value not too bad.