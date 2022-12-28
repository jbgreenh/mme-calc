import streamlit as st
import csv

conversion_factors = {}

with open('data/conversion_factors.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    conversion_factors = {row[0]: row[1] for row in reader}

st.write(
    """
    # MME Calculator
    Please select an opioid in the sidebar and fill in the strength, quantity, and days supply fields   
    *MME = strength * (quantity / days supply) * conversion factor*
    """)

opioid = st.sidebar.selectbox(
    'Select an opioid',
    conversion_factors.keys())

cf = conversion_factors[opioid]
st.sidebar.write(f'`{opioid}` conversion factor: **{cf}**')

strength = st.sidebar.text_input('Strength/Unit', 50)
quantity = st.sidebar.text_input('Quantity', 30)
days_supply = st.sidebar.text_input('Days Supply', 30)
if cf == 'N/A':
    mme = 'N/A'
else:
    try:
        mme = round(float(strength) * (float(quantity) / float(days_supply)) * float(cf), 2)
    except:
        mme = 'please enter numbers in all of the fields'


st.write(f'### MME: <span style="color:#C33921">{mme}</span>', unsafe_allow_html=True)


