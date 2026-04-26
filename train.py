import joblib
from sklearn.linear_model import LinearRegression

def train(X, y):
    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "model.pkl")
    return model
