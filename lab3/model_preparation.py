import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import sys


def prepare_model(prepared_data: str, model_dump: str):
    data = pd.read_csv(prepared_data)

    data["Date"] = pd.to_datetime(data["Date"])

    # Using day of year as feature
    X = data["Date"].dt.dayofyear.values.reshape(-1, 1)  # type: ignore
    y = data["Temperature"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, model_dump)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python model_preparation.py prepared_data.csv model.pkl")
        sys.exit(1)

    prepared_data = sys.argv[1]
    model_dump = sys.argv[2]
    prepare_model(prepared_data, model_dump)
    print("Model preparation: Done")
    sys.exit(0)
