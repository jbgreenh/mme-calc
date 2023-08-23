import streamlit as st
import csv

conversion_factors = {}

with open('data/conversion_factors.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    conversion_factors = {row[0]: row[1] for row in reader}

with st.sidebar:
    opioid = st.selectbox(
        'Select an opioid',
        conversion_factors.keys())

    cf = conversion_factors[opioid]
    st.sidebar.write(f'`{opioid}` conversion factor: **{cf}**')

    strength = st.text_input('Strength/Unit', 50)
    quantity = st.text_input('Quantity', 30)
    days_supply = st.text_input('Days Supply', 30)

try:
    mme = round(float(strength) * (float(quantity) / float(days_supply)) * float(cf), 2)
except:
    mme = 'please enter numbers in all of the fields'

st.markdown(
    f"""
    # MME Calculator
    Please select an opioid in the sidebar and fill in the strength, quantity, and days supply fields   
    *MME = strength * (quantity / days supply) * conversion factor*[^1]  
    
    ## MME: :red[{mme}]

    ___

    [^1]: [Conversions Factors from CDC Prescribing Guidelines](https://www.cdc.gov/mmwr/volumes/71/rr/rr7103a1.htm#T1_down)
    """)