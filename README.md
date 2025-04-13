# Real Estate Price Prediction Web Application

This is a web application that predicts real estate prices based on location, area, and other features.

## Link

Open your web browser and go to `[http://127.0.0.1:5000/](https://proppredict.onrender.com)`

## Features

- Select location from dropdown menu
- Enter square footage, number of bathrooms, and BHK (Bedroom, Hall, Kitchen)
- Get instant price prediction
- Beautiful and responsive UI

## Setup Instructions

1. Make sure you have Python installed on your system
2. Create a virtual environment:
   ```
   python -m venv env_new
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     env_new\Scripts\activate.bat
     ```
   - On Unix or MacOS:
     ```
     source env_new/bin/activate
     ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python app.py
   ```
6. Open your web browser and go to `http://127.0.0.1:5000/`

## Model Information

The application uses a pre-trained machine learning model (`predicted_price.pkl`) that was trained on historical real estate data. The model takes the following inputs:
- Location (one-hot encoded)
- Area in square feet
- Number of bathrooms
- Number of BHK (Bedroom, Hall, Kitchen)

## Technology Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript, Bootstrap
- ML Libraries: NumPy, Pandas, Scikit-learn 
