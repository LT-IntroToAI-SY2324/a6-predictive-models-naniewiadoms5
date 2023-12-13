# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?

What made this model more effective and accurate is using training and testing data. This model got an  r^2 coefficient of 0.680965554336323, while the linear regression without the training and testing data in part 1 received 0.6257932855322312. 

2. What does the R squared coefficient tell you about the model?

The r^2 shows that the model is not relative to the data points being close or matching to the line of best fit. The overall correlation is not that well in terms of the r^2 value, only increasing a little from the last model's r^2 value.

3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.

I would say that my model is not too accurate. Some values are close to each other, increasing the r^2 value, but some others are not, and judging by the r^2 value, most likely a majority of the predicted values are not really close to the actual value. An example of pretty close value is the predicted value as 153.5, and the actual being 162 (only being 8.5 away) compared to another prediction the model made of 136.56 compared to the actual value which is 160 (about 24 point difference).