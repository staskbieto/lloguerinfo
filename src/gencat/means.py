import pandas as pd
import os
import sys
import re
from mapping import fotocasa_gencat_map


# Given a fotocasa address,
# retrieves the excel neighbourhood name
def gencat_neighb(fotocasa_address):
    for k in fotocasa_gencat_map.keys():
        if re.search(k, fotocasa_address):
            return fotocasa_gencat_map[k]
    return ""


# Load the excel with mean prices by neighbourhood
# and the CSV generated by scrapy
dirname = os.path.dirname(__file__)
input_csv_file = sys.argv[1]
output_csv_file = sys.argv[2]

csv = pd.read_csv(input_csv_file)
excel = pd.read_excel(os.path.join(dirname, 'mitjana_anual_lloguer_bcn.xls'))

# Select neighbourhood mean prices for year 2019
neighbourhood_meanprices = excel.iloc[18:91, 0:3]

# Prepare the neighbouhood mean prices dataframe
neighbourhood_meanprices.columns = ['id_neighbourhood', 'neighbourhood', 'neighb_meanprice']
neighbourhood_meanprices['neighbourhood'] = neighbourhood_meanprices['neighbourhood'].str.lower().str.strip()
neighbourhood_meanprices = neighbourhood_meanprices.set_index('neighbourhood')

# Create a new column in the CSV dataframe containing the neighbourhood
csv["neighbourhood"] = csv["address"].str.lower().apply(gencat_neighb)

# Left join the CSV dataframe with the neighbourhood dataframe
result = pd.merge(csv, neighbourhood_meanprices, how='left', left_on='neighbourhood',
                  right_on='neighbourhood')

# Save result into a final CSV
result.to_csv(output_csv_file)
