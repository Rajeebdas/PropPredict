from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("predicted_price.pkl", "rb"))

# Load dataset to extract real locations
df = pd.read_csv("Bengaluru_House_Data.csv")

# Clean and prepare locations
df['location'] = df['location'].apply(lambda x: x.strip() if isinstance(x, str) else x)
# Remove NaN values and convert to string
locations = [str(loc) for loc in df['location'].dropna().unique()]
# Sort locations alphabetically
locations = sorted([loc for loc in locations if loc != 'nan' and loc != ''])

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        location = request.form.get('location')
        sqft = float(request.form.get('sqft'))
        bath = int(request.form.get('bath'))
        bhk = int(request.form.get('bhk'))
        
        # Create location one-hot encoding
        loc_index = locations.index(location) if location in locations else -1
        
        # Prepare input for model prediction (adjust based on your model's requirements)
        input_features = np.zeros(len(locations) + 3)
        input_features[0] = sqft
        input_features[1] = bath
        input_features[2] = bhk
        if loc_index >= 0:
            input_features[3 + loc_index] = 1
            
        # Make prediction
        prediction = model.predict([input_features])[0]
        
        # Divide prediction by 1000
        prediction = prediction / 1000
        
        # Format price (lakhs/crores based on Indian currency system)
        if prediction >= 100:
            price = f"₹{prediction/100:.2f} Crores"
        else:
            price = f"₹{prediction:.2f} Lakhs"
            
        return render_template('index.html', prediction=price, locations=locations, 
                              selected_location=location, sqft=sqft, bath=bath, bhk=bhk)
                              
    except Exception as e:
        return render_template('index.html', error=f"Error in prediction: {str(e)}", locations=locations)

if __name__ == "__main__":
    app.run(debug=True)
