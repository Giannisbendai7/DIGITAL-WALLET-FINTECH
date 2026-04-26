from sklearn.linear_model import LinearRegression
import joblib

def train(X, y):
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "model.pkl")
