
import joblib

model = joblib.load("models/match_prediction_model.pkl")

sample = [[1,2,1,3]]
prediction = model.predict(sample)

print("Predicted Winner:", prediction)
