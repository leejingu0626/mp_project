import pandas as pd
import numpy as np

def STAMP_standalone(target_series, query_series=None, subsequence_length=10, max_time=600, self_join=False, verbose=False):
    #If query is None, calculate the matrix profile distance(value) between target_series itself!!
    if(query_series == type(None)):
        query_series = target_series
        self_join = True

# Main function
# Read INPUT FILE
dataset = pd.read_csv('20170701_Mark_CSV.CSV')
# 'values' columns
dataset_values = dataset['values']
dataset_values_size = np.size(dataset_values)
# print(dataset_values_size)

matrix_profile_result = STAMP_standalone(dataset_values, subsequence_length=700, max_time=600000, verbose=True)