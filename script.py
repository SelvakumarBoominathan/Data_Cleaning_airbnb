import pandas as pd

data = pd.read_csv("Airbnb_Open_data.csv")


# to check the columns in the dataset
# print(data.columns)

# to check the first 5 rows of the dataset
# print(data.head())
# print(data.tail())

# to check data information. This will give us how many empty cells are there in each column and the data type of each column
# print(data.info())

# Removing the columns
# print(data.columns)


columns_to_keep = ['NAME', 'host id', 'host_identity_verified', 'host name',
                   'neighbourhood group', 'neighbourhood', 'lat', 'long', 'country',
                   'country code', 'instant_bookable', 'cancellation_policy', 'room type',
                   'Construction year', 'price', 'service fee', 'minimum nights',
                   'number of reviews', 'last review']

columns_to_remove = ['id', 'reviews per month',
                     'review rate number', 'calculated host listings count',
                     'availability 365', 'house_rules', 'license']

# to check the number of columns to keep and remove
# print(len(columns_to_keep))
# print(len(columns_to_remove))


# Deleting redundant columns
newData = data.drop(columns=columns_to_remove)

# print(newData.tail())


# Renaming of columns

print(data.columns)

data.rename(columns={"NAME": "Name",
            'host_identity_verified': 'host_id_verified'}, inplace=True)

print(data.columns)
