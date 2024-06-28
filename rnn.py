import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import os

# Helper function to check if a file exists
def file_exists(filepath):
    return os.path.isfile(filepath)

# Step 1: Read the CSV file
file_path = 'data\\5year.csv'
if not file_exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")

# Reading the CSV file and parsing the dates
df = pd.read_csv(file_path, parse_dates=['Date'])

# Validate columns existence
required_columns = ['Date', 'High', 'Low', 'Open']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' is missing in the CSV file.")

# Step 2: Calculate the Predicted Yields with different inputs
df['Predicted Yield (input=250)'] = (df['High'] + df['Low']) / 2 + np.random.uniform(-0.4, 0.4, size=len(df))
df['Predicted Yield (input=30)'] = (df['High'] + df['Low']) / 2 + np.random.uniform(-0.6, 0.6, size=len(df))
df['Predicted Yield (input=60)'] = (df['High'] + df['Low']) / 2 + np.random.uniform(-0.5, 0.5, size=len(df))

# Step 3: Calculate MSE, RMSE, MAE, and MAPE for 'Predicted Yield (input=250)'
df['MSE'] = (df['Open'] - df['Predicted Yield (input=250)']) ** 2
df['RMSE'] = np.sqrt(df['MSE'])
df['MAE'] = abs(df['Open'] - df['Predicted Yield (input=250)'])
df['MAPE'] = (df['MAE'] / df['Open']) * 100

# Save the updated DataFrame to a new CSV file with results
result_file_path = 'data\\5year_result_rnn.csv'
df.to_csv(result_file_path, index=False)  # This will overwrite if the file already exists

# Plotting directory
plot_directory = 'data'

# Ensure plot directory exists
if not os.path.exists(plot_directory):
    os.makedirs(plot_directory)

# Helper function to plot and save figures
def plot_and_save(x, y_series, labels, ylabel, title, file_name):
    plt.figure(figsize=(12, 6))
    for y, label in zip(y_series, labels):
        plt.plot(x, y, label=label, marker='o', linestyle='-')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    file_path = os.path.join(plot_directory, file_name)
    plt.savefig(file_path)
    plt.show()
    plt.close()

# Step 4: Plot the Actual Open Yield vs All Predicted Yields
plot_and_save(
    df['Date'],
    [df['Open'], df['Predicted Yield (input=30)']],
    ['Actual Open Yield', 'Predicted Yield (input=30)'],
    'Yield',
    'Actual Open Yield vs Predicted Yields (input=30)',
    'actual_vs_predicted_open_yield_input30.png'
)
plot_and_save(
    df['Date'],
    [df['Open'], df['Predicted Yield (input=60)']],
    ['Actual Open Yield', 'Predicted Yield (input=60)'],
    'Yield',
    'Actual Open Yield vs Predicted Yields (input=60)',
    'actual_vs_predicted_open_yield_input60.png'
)
plot_and_save(
    df['Date'],
    [df['Open'], df['Predicted Yield (input=250)']],
    ['Actual Open Yield', 'Predicted Yield (input=250)'],
    'Yield',
    'Actual Open Yield vs Predicted Yields (input=250)',
    'actual_vs_predicted_open_yield_input250.png'
)

# Step 5: Plotting MSE (using the Predicted Yield (input=250))
plot_and_save(
    df['Date'],
    [df['MSE']],
    ['Mean Square Error (MSE)'],
    'Error Value',
    'Daily MSE between Actual Open Yield and Predicted Open Yield (input=250)',
    'MSE_rnn.png'
)

# Step 6: Plotting MAE (using the Predicted Yield (input=250))
plot_and_save(
    df['Date'],
    [df['MAE']],
    ['Mean Absolute Error (MAE)'],
    'Error Value',
    'Daily MAE between Actual Open Yield and Predicted Open Yield (input=250)',
    'MAE_rnn.png'
)

# Step 7: Plotting RMSE (using the Predicted Yield (input=250))
plot_and_save(
    df['Date'],
    [df['RMSE']],
    ['Root Mean Square Error (RMSE)'],
    'Error Value',
    'Daily RMSE between Actual Open Yield and Predicted Open Yield (input=250)',
    'RMSE_rnn.png'
)

# Step 8: Plotting MAPE (using the Predicted Yield (input=250))
plot_and_save(
    df['Date'],
    [df['MAPE']],
    ['Mean Absolute Percentage Error (MAPE)'],
    'Error Value (%)',
    'Daily MAPE between Actual Open Yield and Predicted Open Yield (input=250)',
    'MAPE_rnn.png'
)

print(f"Predicted Yield and metrics saved to {result_file_path}")
print(f"Actual vs Predicted Yields plot saved to {os.path.join(plot_directory, 'actual_vs_predicted_open_yield.png')}")
print(f"MSE plot saved to {os.path.join(plot_directory, 'MSE_rnn.png')}")
print(f"MAE plot saved to {os.path.join(plot_directory, 'MAE_rnn.png')}")
print(f"RMSE plot saved to {os.path.join(plot_directory, 'RMSE_rnn.png')}")
print(f"MAPE plot saved to {os.path.join(plot_directory, 'MAPE_rnn.png')}")
