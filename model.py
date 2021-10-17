'''
Contains the functions for my predict applicant success model.

'''
import pandas as pd

# Preprocessing function
def PreProcess(filepath , dropCols , thresholds ):




    '''(str) --> (Pandas Dataframe)
    PreProcess returns a list of the target series and input DataFrame
     filepath (str): specifies path to csv file
     dropCol (list of str): specifies columns to drop
     thresholds (list of int)
       '''

    # Read in the csv as dataframe
    DF = pd.read_csv(filepath)

    # Drop the columns specified in dropCol
    DF.drop(dropCols , axis= 1, inplace= True)
       
   # Determine the number of unique values in each column
    uValue_Counts = DF.nunique()

   # Filter out columns with unique count greater than 10
    greater_than_10 = uValue_Counts[uValue_Counts > 10]

    # filter out columns that are not objects
    categorical_cols = [col for col in greater_than_10.index if DF[col].dtypes == 'object']

    # bin each col in categorical_cols according to their threshold
    for i in range(0 , len(thresholds)):

      type_counts = DF[categorical_cols[i]].value_counts()

      less_than_thresh = type_counts[DF[categorical_cols[i]].value_counts() < thresholds[i]].index

      DF[categorical_cols[i]] = DF[categorical_cols[i]].replace(less_than_thresh , 'other')

    # convert categorical values to numeric
    numeric_DF = pd.get_dummies(DF)

    # Splitting target and inputs
    y = numeric_DF.pop('IS_SUCCESSFUL') # Pop off "Is_Succesful" our target column
    X = numeric_DF # the remaining features after the pop off
    
    return [y,X]


# Preprocessing function
def PreProcess_notnumeric(filepath , dropCols , thresholds ):




    '''(str) --> (Pandas Dataframe)
    PreProcess returns a list of the target series and input DataFrame with categorical values still intact
     filepath (str): specifies path to csv file
     dropCol (list of str): specifies columns to drop
     thresholds (list of int)
       '''

    # Read in the csv as dataframe
    DF = pd.read_csv(filepath)

    # Drop the columns specified in dropCol
    DF.drop(dropCols , axis= 1, inplace= True)
       
   # Determine the number of unique values in each column
    uValue_Counts = DF.nunique()

   # Filter out columns with unique count greater than 10
    greater_than_10 = uValue_Counts[uValue_Counts > 10]

    # filter out columns that are not objects
    categorical_cols = [col for col in greater_than_10.index if DF[col].dtypes == 'object']

    # bin each col in categorical_cols according to their threshold
    for i in range(0 , len(thresholds)):

      type_counts = DF[categorical_cols[i]].value_counts()

      less_than_thresh = type_counts[DF[categorical_cols[i]].value_counts() < thresholds[i]].index

      DF[categorical_cols[i]] = DF[categorical_cols[i]].replace(less_than_thresh , 'other')


    # Splitting target and inputs
    y = DF.pop('IS_SUCCESSFUL') # Pop off "Is_Succesful" our target column
    X = DF # the remaining features after the pop off
    
    return [y,X]






 


