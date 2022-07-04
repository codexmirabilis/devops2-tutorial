import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Read csv file
data = pd.read_csv('data/auto-mpg.csv', sep=';')

print(data)

# Shuffle data
data = data.sample(frac=1)

# Target variable
y_variable = data['mpg']

# All columns that contain the attributes
x_variables = data.drop('mpg', axis=1)

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    x_variables, y_variable, test_size=0.2)

# Create model
regressor = LinearRegression()

regressor = regressor.fit(x_train, y_train)

# Model performance
print('r2-score on training dataset:  ' +
      str(regressor.score(x_train, y_train)))
print('r2-score on test dataset:  ' +
      str(regressor.score(x_test, y_test)))

# Save model
file_to_write = open('data/models/linear_regressor.pickle', 'wb')
pickle.dump(regressor, file_to_write)
