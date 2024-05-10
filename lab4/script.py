import pandas as pd
import numpy as np
import seaborn as sns

# Создание датасета о пассажирах Титаника
def create_titanic_dataset():
    # Загрузка датасета о пассажирах Титаника из seaborn
    titanic_df = sns.load_dataset('titanic')
    
    # Создание датасета с необходимыми признаками
    titanic_subset = titanic_df[['pclass', 'sex', 'age']].copy()
    
    return titanic_subset

# Создание новой версии датасета с заполненными пропущенными значениями в поле "Age"
def fill_missing_age(df):
    df_filled = df.copy()
    mean_age = df_filled['Age'].mean()
    df_filled['Age'].fillna(mean_age, inplace=True)
    return df_filled

# Создание нового признака с использованием one-hot-encoding для признака "Sex"
def one_hot_encoding(df):
    df_encoded = pd.get_dummies(df, columns=['Sex'])
    return df_encoded

# Загрузка исходного датасета
titanic_df = create_titanic_dataset()

# Сохранение исходного датасета в DVC
titanic_df.to_csv('data/titanic.csv', index=False)

# Добавление пропущенных значений в возраст

titanic_df = pd.read_csv("data/titanic.csv")
titanic_subset = titanic_df[['pclass', 'sex', 'age']].copy()
titanic_subset.loc[titanic_subset['age'].isnull(), 'age'] = np.random.randint(1, 80, size=titanic_subset['age'].isnull().sum())

titanic_subset.to_csv('data/titanic.csv', index=False)

# !dvc add data/titanic.csv

# # Создание новой версии датасета с заполненными пропущенными значениями в поле "Age"
# titanic_filled_df = fill_missing_age(titanic_df)

# # Сохранение датасета с заполненными пропущенными значениями в DVC
# titanic_filled_df.to_csv('data/titanic_filled.csv', index=False)

# # !dvc add data/titanic_filled.csv
# # !git add data/titanic_filled.csv.dvc
# # !git commit -m "Added Titanic dataset with filled missing age values"
# # !git push origin master

# # Создание нового признака с использованием one-hot-encoding для признака "Sex"
# titanic_encoded_df = one_hot_encoding(titanic_filled_df)

# # Сохранение закодированного датасета в DVC

# # titanic_encoded_df.to_csv('data/titanic_encoded.csv', index=False)
# # !dvc add data/titanic_encoded.csv
# # !git add data/titanic_encoded.csv.dvc
# # !git commit -m "Added Titanic dataset with one-hot encoded 'Sex' feature"
# # !git push origin master

# # Переключение между версиями датасета можно выполнить с помощью команды `dvc checkout`
