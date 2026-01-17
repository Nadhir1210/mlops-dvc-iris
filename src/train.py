import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

in_file = sys.argv[1]      # data/raw/iris.csv
out_model = sys.argv[2]    # models/model.pkl

# Charger le dataset
df = pd.read_csv(in_file)

X = df.drop("species", axis=1)
y = df["species"]

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

joblib.dump(model, out_model)

print(f"Modèle entraîné et sauvegardé dans {out_model}")
