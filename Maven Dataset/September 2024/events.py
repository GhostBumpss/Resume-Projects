import numpy as np
import pandas as pd
import ast
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'events.csv')
events_df = pd.read_csv(file_path, header=0)

distinct_events = events_df["event"].unique()

# Converting the value column from string to dictionary
events_df["value"] = events_df["value"].apply(lambda x: ast.literal_eval(x))

# Separate dataframes for different events
events_df_offer_received = events_df[events_df["event"]==distinct_events[0]]
events_df_offer_viewed = events_df[events_df["event"]==distinct_events[1]]
events_df_transaction = events_df[events_df["event"]==distinct_events[2]]
events_df_offer_completed = events_df[events_df["event"]==distinct_events[3]]

# Extracting value into different appropriate columns
events_df_offer_received['offer_id'] = events_df_offer_received['value'].apply(lambda x: x.get('offer id', 'N/A'))
events_df_offer_received['reward'] = events_df_offer_received['value'].apply(lambda x: x.get('reward', '0'))
events_df_offer_received['amount'] = events_df_offer_received['value'].apply(lambda x: x.get('amount', '0'))

events_df_offer_viewed['offer_id'] = events_df_offer_viewed['value'].apply(lambda x: x.get('offer id', 'N/A'))
events_df_offer_viewed['reward'] = events_df_offer_viewed['value'].apply(lambda x: x.get('reward', '0'))
events_df_offer_viewed['amount'] = events_df_offer_viewed['value'].apply(lambda x: x.get('amount', '0'))

events_df_offer_completed['offer_id'] = events_df_offer_completed['value'].apply(lambda x: x.get('offer_id', 'N/A'))
events_df_offer_completed['reward'] = events_df_offer_completed['value'].apply(lambda x: x.get('reward', '0'))
events_df_offer_completed['amount'] = events_df_offer_completed['value'].apply(lambda x: x.get('amount', '0'))

events_df_transaction['offer_id'] = events_df_transaction['value'].apply(lambda x: x.get('offer id', 'N/A'))
events_df_transaction['reward'] = events_df_transaction['value'].apply(lambda x: x.get('reward', '0'))
events_df_transaction['amount'] = events_df_transaction['value'].apply(lambda x: x.get('amount', '0'))

# Union of all 4 dataframes to create a combined dataframe
adjusted_events_df = pd.concat([events_df_offer_received, events_df_offer_viewed, events_df_transaction, events_df_offer_completed], axis=0, ignore_index=True)

# Drop value column as its fields are already extracted and removing duplicates as well
adjusted_events_df.drop('value', axis=1, inplace=True)
adjusted_events_df = adjusted_events_df.drop_duplicates()

# save the adjusted dataframe to a new csv file
adjusted_csv_file_path = os.path.join(script_dir, "adjusted_events.csv")
adjusted_events_df.to_csv(adjusted_csv_file_path, index=False, header=True)