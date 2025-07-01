import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("xgb_model.pkl")
# team_encoder = joblib.load("team_encoder.pkl")
# compound_encoder = joblib.load("compound_encoder.pkl")

st.title("🏎️ F1 Race Result Predictor")

uploaded_file = st.file_uploader("Upload test race data (CSV)", type=["csv"])

if uploaded_file:
    test_data = pd.read_csv(uploaded_file)

    # Encode categorical features
    # test_data['Team'] = team_encoder.transform(test_data['Team'])
    # test_data['Compound'] = compound_encoder.transform(test_data['Compound'])

    # Feature list
    features = [
        'DriverNumber', 'LapNumber', 'Stint', 'SpeedI1', 'SpeedI2', 'SpeedFL',
        'SpeedST', 'IsPersonalBest', 'Compound', 'TyreLife', 'FreshTyre',
        'Team', 'TrackStatus', 'Deleted', 'year', 'LapTime_s',
        'Sector1Time_s', 'Sector2Time_s', 'Sector3Time_s',
        'Sector1SessionTime_s', 'Sector2SessionTime_s', 'Sector3SessionTime_s',
        'LapStartTime_s', 'PitInTime_s', 'PitOutTime_s', 'LapStartDate_s'
    ]

    # Run prediction
    predictions = model.predict(test_data[features])
    test_data['PredictedPosition'] = predictions

    # Aggregate per driver
    result = test_data.groupby('DriverNumber').agg({
        'PredictedPosition': 'mean',
        'Team': 'first'
    }).sort_values(by='PredictedPosition')

    result['PredictedRank'] = range(1, len(result) + 1)

    st.subheader("🏁 Predicted Race Results")
    st.dataframe(result.reset_index())

    st.success("Prediction completed!")

else:
    st.info("Please upload a race CSV file to get started.")
