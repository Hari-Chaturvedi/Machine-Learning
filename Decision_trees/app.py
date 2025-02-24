import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("D:\Machine Learning\Decision_trees\model.pkl", "rb") as f:
    model = pickle.load(f)

# Custom CSS for better UI
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: black;
        }
        .title {
            text-align: center;
            color: White;
        }
        .stButton button {
            background-color: #2e86c1;
            color: white;
            font-size: 18px;
            border-radius: 10px;
        }
        .stButton button:hover {
            background-color: #1a5276;
        }
        .stSelectbox, .stNumberInput {
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.markdown("<h1 class='title'>🏦 Loan Default Prediction</h1>", unsafe_allow_html=True)
st.markdown("### 📋 Enter the required details to predict loan default:")

# Columns for structured input
col1, col2 = st.columns(2)

with col1:
    no_of_dependents = st.number_input("👨‍👩‍👧‍👦 Number of Dependents", min_value=0, step=1)
    income_annum = st.number_input("💰 Annual Income (₹)", min_value=0.0)
    loan_amount = st.number_input("🏦 Loan Amount (₹)", min_value=0.0)
    loan_term = st.number_input("📆 Loan Term (months)", min_value=0, step=1)
    education = st.selectbox("🎓 Education Level", ["Select", "Graduate", "Not Graduate"], index=0)

with col2:
    residential_assets_value = st.number_input("🏠 Residential Assets Value (₹)", min_value=0.0)
    commercial_assets_value = st.number_input("🏢 Commercial Assets Value (₹)", min_value=0.0)
    luxury_assets_value = st.number_input("🚗 Luxury Assets Value (₹)", min_value=0.0)
    bank_asset_value = st.number_input("🏦 Bank Asset Value (₹)", min_value=0.0)
    cibil_score = st.number_input("📊 CIBIL Score", min_value=0, max_value=900, step=1)
    self_employed = st.selectbox("🧑‍💼 Self Employed?", ["Select", "Yes", "No"], index=0)

# Validation for selection
if education == "Select" or self_employed == "Select":
    st.warning("⚠️ Please select valid options for Education and Self Employment status.")
    st.stop()

# Convert categorical inputs
eduaction = 1 if education == "Not Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

# Predict Button
if st.button("🔍 Predict Loan Default"):
    input_data = np.array([
        no_of_dependents, income_annum, loan_amount, loan_term,
        residential_assets_value, commercial_assets_value, luxury_assets_value,
        bank_asset_value, self_employed, eduaction, cibil_score
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    # Show result in a styled card
    st.markdown("---")
    if prediction[0] == 1:
        st.markdown(
            "<div style='background-color:#ff4c4c;padding:20px;border-radius:10px;'>"
            "<h2 style='color:white;'>❌ High Risk: The applicant is likely to default on the loan.</h2>"
            "</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color:#28a745;padding:20px;border-radius:10px;'>"
            "<h2 style='color:white;'>✅ Low Risk: The applicant is NOT likely to default on the loan.</h2>"
            "</div>",
            unsafe_allow_html=True
        )
