import pandas as pd

data = pd.read_csv("Airbnb_Open_data.csv")


# to check the columns in the dataset
# print(data.columns)

# to check the first 5 rows of the dataset
# print(data.head())

# to check data information. This will give us how many empty cells are there in each column and the data type of each column
# print(data.info())


print(data['license'].value_counts())
