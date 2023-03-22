import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


health_data = pd.read_csv("Training_session.csv")
# isolate Average_Pulse and Calorie_Burnage from the dataset
x = health_data['Average_Pulse']
y = health_data['Calorie_Burnage']

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
print(results.summary())
plt.show()

# A new line in our file!
'''
Summary - Predicting Calorie_Burnage with Average_Pulse
- Coefficient of 0.3296, which means that Average_Pulse has a very small effect on Calorie_Burnage.
- High P-value (0.824), which means that we cannot conclude a relationship between Average_Pulse and Calorie_Burnage.
- R-Squared value of 0, which means that the linear regression function line does not fit the data well.
- The 95% confidence interval for Average_Pulse is (-2.588, 3.247). This confidence interval does contain the 
number “0”, which means that the true value for the coefficient of Average_Pulse could be zero,
i.e. non-significant in predicting Calorie_Burnage.
'''
#A new line in our file!

#this is an emergency-fix

