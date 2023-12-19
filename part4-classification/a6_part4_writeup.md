# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

With the StandardScaler commented out, the model has an accuracy of 61% or 0.6125. This model is not accurate because the data is not standardized, meaning that the input data is with high variance. Usually image processing would be done to set images to the same amount of pixels and other techniques, but the StandardScaler balances the input data on its own.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

The model got an accuracy rate of 0.8375, now that the data is balanced and can be compared to the same level. This model should be used for predicting if an SUV should be bought because the model receives a high accuracy.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

Looking through the predicted and actual results, the model seemed to be only predicting the purchased or y-values incorrectly infrequently. One pattern I see is that the model does not predict an inaccurate value consecutively, or in a row. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

The prediction I got was [0] which means no.

