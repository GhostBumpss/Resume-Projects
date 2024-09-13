import numpy as np
import pandas as pd
import ast
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'events.csv')
events_df = pd.read_csv(file_path, header=0)

distinct_events = events_df["event"].unique()

events_df_offer_received = events_df[events_df["event"]==distinct_events[0]]
events_df_offer_viewed = events_df[events_df["event"]==distinct_events[1]]
events_df_transaction = events_df[events_df["event"]==distinct_events[2]]
events_df_offer_completed = events_df[events_df["event"]==distinct_events[3]]

events_df_offer_completed['value'] = events_df_offer_completed['value'].apply(lambda x: ast.literal_eval(x))
events_df_offer_completed['offer_id'] = events_df_offer_completed['value'].apply(lambda x: x.get('offer_id', 'N/A'))
events_df_offer_completed['reward'] = events_df_offer_completed['value'].apply(lambda x: x.get('reward', '0'))

events_df_offer_received['value'] = events_df_offer_received['value'].apply(lambda x: ast.literal_eval(x))
events_df_offer_received['offer_id'] = events_df_offer_received['value'].apply(lambda x: x.get('offer id', 'N/A'))

events_df_transaction['value'] = events_df_transaction['value'].apply(lambda x: ast.literal_eval(x))
events_df_transaction['amount'] = events_df_transaction['value'].apply(lambda x: x.get('amount', 'N/A'))