import joblib
import pandas as pd
import sys
from sklearn.preprocessing import StandardScaler


def preprocess_data(from_file: str, to_file: str, scaler_dump: str):
    data = pd.read_csv(from_file)
    X = data[["Temperature"]]
    scaler = StandardScaler()
    data[["Temperature"]] = scaler.fit_transform(X)
    data.to_csv(to_file, index=False)
    joblib.dump(scaler, scaler_dump)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python model_preprocessing.py from.csv to.csv scaler.pkl")
        sys.exit(1)

    from_file = sys.argv[1]
    to_file = sys.argv[2]
    scaler_dump = sys.argv[3]
    preprocess_data(from_file, to_file, scaler_dump)
    print("Model preprocessing: Done")
