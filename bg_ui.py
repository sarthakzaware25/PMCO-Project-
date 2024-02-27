import streamlit as st
import base64
from PIL import Image
import time

def page_config():
    st.set_page_config(page_title = "PMCO",layout = "wide",initial_sidebar_state = "expanded",page_icon = ":🧮:")
    st.title("PMOC :red[Application]")
    st.header(":black[Performing Multiple Operations]")
    img = Image.open('images/logo.jpeg')
    st.sidebar.image(img, width = 150)
    st.sidebar.title("PMOC Web Application")
    st.sidebar.subheader("This web application contains multiple mathematical operations.")
    rad = st.sidebar.radio("Navigation",["Home","About Us"])
    
    if rad == "Home":
        with st.sidebar:
            set_background('images/wallpaper.jpeg')
                    
            operations = ["Operations","Addition","Substraction","Multiplication","Division","Modulus","Exponential","Floar division","Cubes","Computepay","Fibonnaci_series","list_permutation","list_intersection","list_difference","list_symmetric_difference","longest_increasing_subsequence","longest_common_subsequence","list_of_even","list_of_odd","square_of number_upto_specific_number"]
            operation = st.sidebar.selectbox("Select the operation",operations)
            return operation
    
    if rad == "About Us":
        st.write("Here you get to know About US")
        progress  = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)

        st.balloons()
        st.subheader("Created by:")
        st.title("Sarthak Zaware")
        



    
    


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover; }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


