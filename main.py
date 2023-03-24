import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


health_data = pd.read_csv("Training_session.csv")
# isolate Average_Pulse and Calorie_Burnage from the dataset
x = health_data['Average_Pulse']
y = health_data['Calorie_Burnage']

<<<<<<< HEAD

=======
corr_health_data = round(health_data.corr(),2) 
>>>>>>> correlation-matrix
# Calculate a linear least-squares regression for two sets of measurements
result = stats.linregress(x, y)


def linear_function(x):
    return result.slope * x + result.intercept


responseValue = list(map(linear_function, x))

plt.scatter(x, y)
plt.plot(x, responseValue)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel('Average_Pulse')
plt.ylabel('Calorie_Burnage')

model = smf.ols('Calorie_Burnage ~ Average_Pulse', health_data)
results = model.fit()
print(corr_health_data, results.summary())
plt.show()
