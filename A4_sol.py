import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# Read the Excel data into a Pandas DataFrame
df = pd.read_excel(r"C:\Users\G NITHIN\Documents\Machine_learning\Lab Session1 Data.xlsx",sheet_name="IRCTC Stock Price")

# Select the Price column
price_data = df['Price']

# Calculate the mean and variance of the Price column
mean = np.mean(price_data)
variance = np.var(price_data)

print('Mean:', mean)
print('Variance:', variance)

# Select the price data for all Wednesdays
wednesday_data = price_data[df['Day'] == 'Wed']
#print(wednesday_data)
# Calculate the sample mean
sample_mean = np.mean(wednesday_data)

print('Sample mean:', sample_mean)

# Select the price data for the month of April
april_data = price_data[df['Month'] == 'Apr']

# Calculate the sample mean
april_mean = np.mean(april_data)

print('April mean:', april_mean)

chg_data = df['Chg%']

# Create a new column called 'is_loss' that indicates whether the stock price went up or down
is_loss = np.where(chg_data > 0, False, True)

# Calculate the probability of making a loss
probability_of_loss = np.mean(is_loss)

print('Probability of making a loss:', probability_of_loss)



# Filter the data for Wednesdays
wednesday_data = df[df['Day'] == 'Wed']

# Calculate the probability of making a profit
probability_of_profit_on_wednesday = np.mean(wednesday_data['Chg%'] > 0)

print('Probability of making a profit on Wednesday:', probability_of_profit_on_wednesday)



# Calculate the probability of it being a Wednesday
probability_of_wednesday = np.mean(df['Day'] == 'Wed')

# Calculate the conditional probability
conditional_probability = probability_of_profit_on_wednesday / probability_of_wednesday

print('Conditional probability of making a profit, given that today is Wednesday:', conditional_probability)



# Create a scatter plot of Chg% vs Day

plt.scatter(df['Day'], df['Chg%'])
plt.xlabel('Day')
plt.ylabel('Chg%')
plt.title('Chg% vs Day')
plt.show()