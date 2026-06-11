import streamlit as st 
import joblib 
import pandas as pd 
import os


st.title('RYAN T STORES ') 
st.write("iPHONE REVENUE PREDICTION SYSTEM")


if os.path.exists("iphone_revenue_model.pkl"):
    model = joblib.load("iphone_revenue_model.pkl")
else:
    st.error("Model file not found")
    st.stop()

country = st.selectbox( 
'Country', 
['USA','UK','Canada','Germany','UAE','Pakistan'] 
) 
model_name = st.selectbox( 
'Model', 
[ 
'iPhone 12', 
'iPhone 13', 
'iPhone 14', 
'iPhone 14 Pro', 
'iPhone 15', 
'iPhone 15 Pro Max' 
] 
) 
storage = st.selectbox( 
'Storage', 
['128GB','256GB','512GB'] 
) 
color = st.selectbox( 
'Color', 
['Black','Blue','White','Purple','Gold'] 
) 
quantity = st.number_input( 
'Quantity', 
min_value=1, 
max_value=10 
) 
price = st.number_input( 
'Price' 
) 
payment = st.selectbox( 
'Payment Method', 
[ 
'Debit Card', 
'Credit Card', 
'PayPal', 
'Cash' 
] 
) 
if st.button('Predict Revenue'):
    Data = pd.DataFrame({ 
        'Country':[country], 
        'iPhone_Model':[model_name], 
        'Storage':[storage], 
        'Color':[color], 
        'Quantity':[quantity], 
        'Price':[price], 
        'Payment_Method':[payment]
        }) 
    Revenue = model.predict(Data) 
    st.success( 
        f'Predicted Revenue: ${Revenue[0]:,.2f}' 
)
