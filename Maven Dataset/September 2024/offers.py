import pandas as pd
import os
import ast

filename = os.path.realpath(__file__)
dirname = os.path.dirname(filename)
filepath = os.path.join(dirname, "offers.csv")

offers_df = pd.read_csv(filepath, header=0)
offers_df["channels"] = offers_df["channels"].apply(ast.literal_eval)
adjusted_df = offers_df.explode('channels')
adjusted_df = adjusted_df.rename(columns={'channels': 'channel'})

adjusted_offers_file_path = os.path.join(dirname, "adjusted_offers.csv")
adjusted_df.to_csv(adjusted_offers_file_path, index=False, header=True)

print(adjusted_df)