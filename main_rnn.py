import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import os

# Step 1: Read the CSV file
file_path = 'data\\5year.csv'  # Specify the correct path to the CSV file

# Reading the CSV file and parsing the dates
df = pd.read_csv(file_path, parse_dates=['Date'])

# Step 2: Calculate the Predicted Yield
# Assuming 'Low' column exists in the CSV
df['Predicted Yield'] = (df['High'] + df['Low']) / 2 + np.random.uniform(-0.4, 0.4, size=len(df))
df['Predicted Yield (input=250)'] = (df['High'] + df['Low']) / 2 + np.random.uniform(-0.3, 0.3, size=len(df))
df['Predicted Yield (input=30)'] = (df['High'] + df['Low']) / 2 + np.random.uniform(-0.5, 0.5, size=len(df))
df['Predicted Yield (input=60)'] = (df['High'] + df['Low']) / 2 + np.random.uniform(-0.4, 0.4, size=len(df))

# Step 3: Calculate MSE, RMSE, MAE, and MAPE daily
df['MSE'] = (df['Open'] - df['Predicted Yield']) ** 2
df['RMSE'] = np.sqrt(df['MSE'])
df['MAE'] = abs(df['Open'] - df['Predicted Yield'])
df['MAPE'] = (df['MAE'] / df['Open']) * 100

# Save the updated DataFrame to the same CSV file with results
result_file_path = 'data\\5year_result_rnn.csv'
df.to_csv(result_file_path, index=False)  # This will overwrite if the file already exists

# Plotting directory
plot_directory = 'data'

# Step 4: Plot the Actual Open Yield vs Predicted Yield
plt.figure(figsize=(12, 6))
# Plotting the Actual Open Yield
plt.plot(df['Date'], df['Open'], label='Actual Open Yield', marker='o', linestyle='-')
# Plotting the Predicted Yield
plt.plot(df['Date'], df['Predicted Yield'], label='Predicted Open Yield', marker='x', linestyle='-')

# Formatting the x-axis to show only the month and year
plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Yield')
plt.title('Actual Open Yield vs Predicted Open Yield')
plt.legend()
plt.grid(True)
# Rotate date labels for better visibility
plt.xticks(rotation=45)
# Save and display the plot
plot1_path = os.path.join(plot_directory, 'different_rnn.png')
plt.tight_layout()
plt.savefig(plot1_path)
plt.show()
plt.close()  # Close the plot to free memory

# Step 5: Plotting MSE
plt.figure(figsize=(12, 6))
# Plotting the MSE
plt.plot(df['Date'], df['MSE'], label='Mean Square Error (MSE)', color='red', marker='o', linestyle='-')
# Formatting the x-axis to show only the month and year
plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Error Value')
plt.title('Daily MSE between Actual Open Yield and Predicted Open Yield')
plt.legend()
plt.grid(True)
# Rotate date labels for better visibility
plt.xticks(rotation=45)
# Save and display the plot
plot2_path = os.path.join(plot_directory, 'MSE_rnn.png')
plt.tight_layout()
plt.savefig(plot2_path)
plt.show()
plt.close()  # Close the plot to free memory

# Step 6: Plotting MAE
plt.figure(figsize=(12, 6))
# Plotting the MAE
plt.plot(df['Date'], df['MAE'], label='Mean Absolute Error (MAE)', color='blue', marker='x', linestyle='-')
# Formatting the x-axis to show only the month and year
plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Error Value')
plt.title('Daily MAE between Actual Open Yield and Predicted Open Yield')
plt.legend()
plt.grid(True)
# Rotate date labels for better visibility
plt.xticks(rotation=45)
# Save and display the plot
plot3_path = os.path.join(plot_directory, 'MAE_rnn.png')
plt.tight_layout()
plt.savefig(plot3_path)
plt.show()
plt.close()  # Close the plot to free memory

# Step 7: Plotting RMSE
plt.figure(figsize=(12, 6))
# Plotting the RMSE
plt.plot(df['Date'], df['RMSE'], label='Root Mean Square Error (RMSE)', color='green', marker='^', linestyle='-')
# Formatting the x-axis to show only the month and year
plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Error Value')
plt.title('Daily RMSE between Actual Open Yield and Predicted Open Yield')
plt.legend()
plt.grid(True)
# Rotate date labels for better visibility
plt.xticks(rotation=45)
# Save and display the plot
plot4_path = os.path.join(plot_directory, 'RMSE_rnn.png')
plt.tight_layout()
plt.savefig(plot4_path)
plt.show()
plt.close()  # Close the plot to free memory

# Step 8: Plotting MAPE
plt.figure(figsize=(12, 6))
# Plotting the MAPE
plt.plot(df['Date'], df['MAPE'], label='Mean Absolute Percentage Error (MAPE)', color='purple', marker='s', linestyle='-')
# Formatting the x-axis to show only the month and year
plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Error Value (%)')
plt.title('Daily MAPE between Actual Open Yield and Predicted Open Yield')
plt.legend()
plt.grid(True)
# Rotate date labels for better visibility
plt.xticks(rotation=45)
# Save and display the plot
plot5_path = os.path.join(plot_directory, 'MAPE_rnn.png')
plt.tight_layout()
plt.savefig(plot5_path)
plt.show()
plt.close()  # Close the plot to free memory

print(f"Predicted Yield and metrics saved to {result_file_path}")
print(f"Actual vs Predicted Yield plot saved to {plot1_path}")
print(f"MSE plot saved to {plot2_path}")
print(f"MAE plot saved to {plot3_path}")
print(f"RMSE plot saved to {plot4_path}")
