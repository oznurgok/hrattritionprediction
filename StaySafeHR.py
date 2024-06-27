

import streamlit as st
from PIL import Image


logo = Image.open('/Users/oznurgok/Desktop/logo2.png')
st.sidebar.image(logo, caption='Wellcome to StaySafe.HR()', use_column_width=True)
st.sidebar.markdown("""
## About Us

We are a dedicated team of data analysts and HR experts passionate about 
empowering organizations with predictive analytics. Our goal is to help you 
predict employee turnover with precision, enabling proactive retention 
strategies for a more stable and engaged workforce.
""")

def show_main():

    logo = Image.open('/Users/oznurgok/Desktop/logo2.png')
    st.image(logo, caption='', use_column_width=True)

if __name__ == '__main__':
    show_main()