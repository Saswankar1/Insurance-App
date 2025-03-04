import streamlit as st
import joblib

# Load the trained model
model = joblib.load("insurance_model.pkl")

# Streamlit App Title with Styled Header
st.markdown(
    "<h1 style='text-align: center; color: #007BFF;'> Health Insurance Cross-Sell Prediction</h1>", 
    unsafe_allow_html=True
)
st.markdown("---")

# Layout: Two Columns for Better UX
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🎂 Enter Age", min_value=18, max_value=100, value=30)
    is_senior = st.radio("👴 Are you a Senior?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    credit_score = st.number_input("💳 Credit Score", min_value=300, max_value=850, value=700)
    prior_insurance = st.radio("📑 Prior Insurance?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    claims_frequency = st.slider("🔄 Claims Frequency", min_value=0, max_value=10, value=1)

with col2:
    policy_type = st.selectbox("📜 Policy Type", ["Basic", "Comprehensive", "Premium"])
    premium_amount = st.number_input("💰 Premium Amount ($)", min_value=100, max_value=10000, value=500)
    total_discounts = st.slider("🎟️ Total Discounts (%)", min_value=0, max_value=50, value=10)
    source_of_lead = st.selectbox("🌐 Source of Lead", ["Online", "Agent", "Referral", "Other"])
    website_visits = st.number_input("🖥️ Website Visits", min_value=0, max_value=50, value=5)

# Additional Fields in Full Width
inquiries = st.number_input("📞 Number of Inquiries", min_value=0, max_value=20, value=3)
quotes_requested = st.number_input("📋 Quotes Requested", min_value=0, max_value=10, value=2)
time_since_first_contact = st.number_input("⏳ Days Since First Contact", min_value=0, max_value=365, value=30)

# Encode categorical variables
policy_type_mapping = {"Basic": 0, "Comprehensive": 1, "Premium": 2}
source_of_lead_mapping = {"Online": 0, "Agent": 1, "Referral": 2, "Other": 3}

policy_type_encoded = policy_type_mapping[policy_type]
source_of_lead_encoded = source_of_lead_mapping[source_of_lead]

# Create input data
user_data = [[
    age, is_senior, credit_score, prior_insurance, claims_frequency,
    policy_type_encoded, premium_amount, total_discounts,
    source_of_lead_encoded, website_visits, inquiries, 
    quotes_requested, time_since_first_contact
]]

# Predict with a Styled Button
if st.button("🔍 Predict"):
    prediction = model.predict(user_data)
    
    if prediction[0] == 1:
        st.markdown(
            "<h3 style='text-align: center; color: #28a745; background-color: #d4edda; padding: 10px; border-radius: 5px;'>✅ The customer is likely to buy additional insurance!</h3>", 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h3 style='text-align: center; color: #dc3545; background-color: #f8d7da; padding: 10px; border-radius: 5px;'>❌ The customer is unlikely to buy additional insurance.</h3>", 
            unsafe_allow_html=True
        )
