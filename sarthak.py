"""import streamlit
import base64
from PIL import Image


st.set_page_config(
    page_title = "My app",
    layout = "wide",
    initial_sidebar_state = "expanded"
)
st.title("PMOC :red [Application]")
st.header(":blue[Performing Multiple Opperations]")
st.subheader("Web Application")
st.text("This web application contains multiple mathematical opperations.")

def page_config():
    st.set_page_config(page_title='ESG Data and Reporting', layout='wide', initial_sidebar_state="expanded")
    set_background('image/back.jpeg')
    style()
    with st.sidebar:
        img = Image.open('image/logo.png')
        st.image(img)

    st.markdown('<span class="title-text">ESG Data and Reporting</span>', unsafe_allow_html=True)

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
    st.markdown(page_bg_img, unsafe_allow_html=True)"""



import streamlit as st
import math
import operator
import base64
from PIL import Image
import numpy as np

st.set_page_config(page_title = "PMCO",layout = "wide",initial_sidebar_state = "expanded",page_icon = ":🧮:")
st.title("PMOC :red[Application]")
st.header(":black[Performing Multiple Operations]")
st.subheader("Web Application")
st.text("This web application contains multiple mathematical operations.")

operation = st.radio("Select an operation",("Addition","Substraction","Multiplication","Division","Modulus","Exponential","Floar division","Squareroot_of_arithmetic_operation","Cubesum","Computepay","Fibonnaci_series","Flat_list","list_permutation","list_intersection","list_difference","list_symmetric_diifference","longest_increasing_subsequence","longest_common_subsequence","list_of_even","list_of_odd","square_of number_upto_specific_number"))
st.sidebar.selectbox("Select the operation")

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
set_background('images/background4.jpeg')


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()



my_list = []


def manager():
    with st.expander("Example"):
        st.write(my_list)
        user_input = st.text_input("Enter a key")
        add_button = st.button("insert", key='insert_button')
        if add_button:
            if len(user_input) > 0 :
                my_list.append(user_input)
                st.write(my_list)
            else:
                st.warning("Enter text")

manager()

def Addition():
    with st.expander("Addition"):
        user_input = st.text_input("Enter the number")
        add_button = st.button("add",key='add_button')
        if add_button:
            if len(user_input) > 0 :
                my_list.append(user_input)
                sum=0
                add_list=[]
                for i in my_list:
                    sum = np.add(sum,i)
                    add_list.append(sum)
                st.write(add_list)
                
            else:
                st.warning("Enter text")

Addition()


def Addition():
    ans=0
    for i in list:
        ans = ans + operator.add(0,i)
        return (ans)                