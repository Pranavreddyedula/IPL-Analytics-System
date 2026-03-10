
import pandas as pd

def prepare_features(path="data/Cricket_data.csv"):
    df = pd.read_csv(path)
    features = ['home_team','away_team','toss_won','venue_name']
    target = 'winner'
    df = df[features + [target]].dropna()
    return df
