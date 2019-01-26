import pandas as pd
import numpy as np

# Main function
# Read INPUT FILE
dataset = pd.read_csv('20170701_Mark_CSV.CSV')
# 'values' columns
dataset_values = dataset['values']
dataset_values_size = np.size(dataset_values)
# print(dataset_values_size)

