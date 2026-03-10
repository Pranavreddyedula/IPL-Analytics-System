
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/Cricket_data.csv")

features = ['home_team','away_team','toss_won','venue_name']
target = 'winner'

df = df[features + [target]].dropna()

encoder = LabelEncoder()

for col in df.columns:
    df[col] = encoder.fit_transform(df[col])

X = df.drop('winner',axis=1)
y = df['winner']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

accuracy = model.score(X_test,y_test)

print("Model Accuracy:",accuracy)

joblib.dump(model,"models/match_prediction_model.pkl")
