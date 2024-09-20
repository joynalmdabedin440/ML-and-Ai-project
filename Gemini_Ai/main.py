import os
import streamlit as st
from streamlit_option_menu import option_menu

working_dir = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(
    page_title='New Ai Text Generator',
    page_icon='✨',
    layout='centered'
)

