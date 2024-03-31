#!/bin/bash

python3 data_creation.py
python3 model_preprocessing.py test/test_data.csv test/test_data_scaled.csv scaler.pkl
python3 model_preprocessing.py train/train_data.csv train/train_data_scaled.csv scaler.pkl
python3 model_preparation.py train/train_data_scaled.csv model.pkl
python3 model_testing.py model.pkl test/test_data_scaled.csv