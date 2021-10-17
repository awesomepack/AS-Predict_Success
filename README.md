# AS-Predict_Success
Predict whether an applicant will be successful if funded by Alphabet Soup.

## Table of Contents
* predict.ipynb: initial model cleaning , training , compiling
* AlphabetSoupCharity_Optimizer.ipynb: code for optimization attempts
* model.py: has preprocessing code wrapped up in a function to make optimizing iterations easier
* Read Me: contains the report

## Overview
    AlphabetSoup wants to lend money to organizations that will make an impact in the world. Money funded in failed ventures is money that could have been allocated to a potential success. Using historical data from its applicants and information on their success the intention of this analyis is to help application reviewers make the best decisions when disbursing funds

## Results
     Data Prepocessing:
        * The target feature in the csv data is in the "Is_Success" column which is a binary representation of whether or not a certain applicant was succesful in their venture. (target_feature.png)
        * The remaining features after accounting for the target column would be the initial inputs for our model. (input_features.png) 
        * Some features in the dataset are used purely for identification , in this case the EIN and Name features , which add no value to the model and should be removed. Once trained it would be possible to discover noisy features that only serve to confuse the model and decrease its performance.

    Compiling:
        * As I described in the predict.ipynb file which contains links to my sources , that generally single layered networks only have the capacity to model linear systems , unless the number of nodes is drastically increased. Later I discovered that two hidden layers are sufficient to model most problems. For this reason I decided to start of my model with two hidden layers and matched the number of hidden neurons with that of the features in the dataset 43.

        * In my very first attempt my model had a test accuracy of 72.6% which is roughly only three percent away from the target performance (initial_score.png)

        * In my second attempt I read that the smaller the output of your loss function meant that your model would be less sensitive to outliers. This formed the basis for testing a new loss function "Poisson" against the default "Binary-Crossentropy" function. This model performed worse but nearly identical to my first attempt at an accuracy of 72.5%.

        * My third attempt involved increasing the number of epochs as I thought that the model needed more time to converge 150 epochs. This also resulted in an accuracy of around 72.5%. I tried 50 epochs and found a slight reduction in accuracy but at improved time efficiency.

        * In my Final attempt I fiddled with the capacity of the model fearing that the loss was associated with underfitting. As such I doubled the number of hidden neurons in my hidden layer. The result again was 72.5% showing that the loss was not a result of underfitting. I then tried halving the number of neurons thinking that the model may be overfitting but the result was identical to that of doubling.

        * I did later find that ceiling analysis provides a systematic method of pinpointing where in your pipeline your model is underperforming so you can spend your time on parts of the pipeline that are more likely to yield model improvements instead of focusing one section of your pipeline like I did.

## Summary
    Overall the model made it close to the target performance. Because this is a binary classification problem logistic regression or an SVM could work. They might even be less computationally costly if we can prove that our classes are linearly seperable since logistic regression is a linear classifier. However if the classes are seperated my a complex shape then that is where neural networks excels




