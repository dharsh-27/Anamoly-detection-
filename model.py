import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pickle

# Step 1: Load your dataset
data = pd.read_csv('your_data.csv')

# Step 2: Preprocess the data
data.fillna(method='ffill', inplace=True)
features = data[['amount']]  # Replace with relevant features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Step 3: Train the model
model = IsolationForest(contamination=0.05)
model.fit(features_scaled)

# Step 4: Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Step 5: (Optional) Load the model
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
