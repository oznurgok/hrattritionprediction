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

def show_home():
    st.title('Employee Attrition Prediction App')
    st.text("")
    st.subheader('How to Use It')
    st.text("For detailed instructions on how to use the HR Employee Attrition Prediction ")
    st.text("application, please watch the video below.")
    st.text("")

    video_path = '/Users/oznurgok/Desktop/HRPROJETanırım.mp4'
    st.video(video_path)


if __name__ == '__main__':
    show_home()