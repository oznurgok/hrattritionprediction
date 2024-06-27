import streamlit as st
import pandas as pd
import catboost as cb
from catboost import CatBoostClassifier
from PIL import Image

# CatBoost modelini yükleme
model = cb.CatBoostClassifier()
model.load_model('/Users/oznurgok/Desktop/catboost_model3.cbm')

logo = Image.open('/Users/oznurgok/Desktop/logo2.png')
st.sidebar.image(logo, caption='Welcome to StaySafe.HR()', use_column_width=True)
st.sidebar.markdown("""
## About Us

We are a dedicated team of data analysts and HR experts passionate about 
empowering organizations with predictive analytics. Our goal is to help you 
predict employee turnover with precision, enabling proactive retention 
strategies for a more stable and engaged workforce. ...
""")

# Kullanıcıdan girdi almak için sütunlar
cols = [
    'Age', 'DistanceFromHome', 'EnvironmentSatisfaction', 'MonthlyIncome', 'OverTime_Yes'
]

st.title("Employee Attrition Prediction")

# Kullanıcıdan girdi almak için form
def user_input_features():
    age = st.slider("Age", min_value=18, max_value=60, value=30)
    distance_from_home = st.slider("Distance From Home", min_value=1, max_value=10, value=5)
    environment_satisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
    monthly_income = st.slider("Monthly Income ($)", min_value=1000, max_value=20000, value=5000)
    over_time = st.selectbox("OverTime", ["Yes", "No"])

    # Dummy değişkenleri ayarlayın
    data = {
        'Age': age,
        'DistanceFromHome': distance_from_home,
        'EnvironmentSatisfaction': environment_satisfaction,
        'MonthlyIncome': monthly_income,
        f'OverTime_{over_time}': 1
    }

    # Eksik sütunları doldurun
    for col in cols:
        if col not in data:
            data[col] = 0

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

def get_recommendations(data):
    recommendations = []
    if data['EnvironmentSatisfaction'].iloc[0] < 3:
        recommendations.append("Consider improving the work environment to increase satisfaction.")
    if data['MonthlyIncome'].iloc[0] < 5000:
        recommendations.append("Consider offering a salary raise to retain the employee.")
    if data['OverTime_Yes'].iloc[0] == 1:
        recommendations.append("Consider reducing overtime to prevent employee burnout.")
    return recommendations

if st.button('Predict'):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.header(':red[The employee will depart from the job.]')
        recommendations = get_recommendations(input_df)
        if recommendations:
            st.subheader("Recommendations to retain the employee:")
            for rec in recommendations:
                st.write("- " + rec)
    else:
        st.header(':green[The employee will not depart from the job.]')