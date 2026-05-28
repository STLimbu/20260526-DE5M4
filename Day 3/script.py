import pandas as pd
from sklearn.datasets import fetch_openml

titanic = fetch_openml(name="titanic", version=1, as_frame=True)
data = pd.DataFrame(titanic.data)

print(data)

# Check for missing values
print(data.isnull().sum())

# Fill missing values properly
data['age'] = data['age'].fillna(data['age'].median())
data['fare'] = data['fare'].fillna(data['fare'].median())
data['embarked'] = data['embarked'].fillna(data['embarked'].mode()[0])


# Drop weak columns
data.drop(columns=['cabin', 'boat', 'body', 'home.dest'], inplace=True)

print(data.isnull().sum())

print("Duplicate rows:", data.duplicated().sum())