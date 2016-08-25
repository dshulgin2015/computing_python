import pandas as pd
import scitools as sct
import numpy as np

# Read the file
data = pd.read_csv("carma22AUG.csv", low_memory=False)

context__countryCode = data['context__countryCode']
# Output the number of rows 
print(len([item for item in context__countryCode if item == 'IT']))

print(set(context__countryCode))