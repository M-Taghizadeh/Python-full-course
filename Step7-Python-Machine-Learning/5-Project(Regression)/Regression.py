"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import xlrd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def read_excel_files(loc):
    file = xlrd.open_workbook(loc) 
    sheet = file.sheet_by_index(0)
    return sheet

def show_data(year, population):
    for i in range(0, len(year)):
        print(year[i] , " ---> " ,population[i])
	
# Create dataset with read from excel file: 
sheet = read_excel_files("C:/Users/Zanis/Desktop/AI Docs/AI03/Regression/Guilan_Population.xlsx")
list_year = []
list_population = []
for i in range(0, sheet.nrows):
    list_year.append([sheet.cell_value(i, 0)])
    list_population.append([sheet.cell_value(i, 1)])
print("[Data Set]")
show_data(list_year, list_population)
print("-------------------------")

# Reshape dataset 
x = np.array(list_year).reshape(-1, 1) # reshape mean that vectorize list
y = np.array(list_population).reshape(-1, 1)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x, y)

# Test set
list_test = [1400, 1405, 1410, 1415, 1420, 1425, 1430]
x_test = np.array(list_test).reshape(-1, 1)  

# Make predictions using the testing set
y_pred = regr.predict(x_test)

# Show output of predictions
print("[Test Set]")
show_data(list_test, y_pred)
print("-------------------------")
# Plot outputs
plt.scatter(x, y,  color='black')
plt.plot(x_test, y_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()