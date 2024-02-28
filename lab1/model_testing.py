import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import sys

def test_model(model_file: str, test_data: str) -> float:
    model = joblib.load(model_file)
    df = pd.read_csv(test_data)
    df["Date"] = pd.to_datetime(df["Date"])
    # Using day of year as feature
    X = df["Date"].dt.dayofyear.values.reshape(-1, 1)  # type: ignore
    y = df["Temperature"]
    return model.score(X, y)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python model_testing.py model.pkl test_data.csv")
        sys.exit(1)

    model_file = sys.argv[1]
    test_data = sys.argv[2]
    score = test_model(model_file, test_data)
    print("Model score (R^2): ", score)
    print("Model testing: Done")
