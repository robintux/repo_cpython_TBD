# train_model.py - Nuevo modelo con feature flag
import pandas as pd  
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import train_test_split

def train_model(use_new_model:bool = False):
  df = pd.read_csv("data/dataset.csv")
  X,y = df.drop("target", axis = 1), df["target"]
  X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)

  if use_new_model:
    model = RandomForestClassifier(n_estimators=200, max_depth=25)
  else:
    model = RandomForestClassifier(n_estimators=50, max_depth=10)
  
  model.fit(X_train, y_train)
  acc = accuracy_score(y_test, model.predict(X_test))
  print(f"Accuracy: {acc:.4f}")
  return model