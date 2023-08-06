import streamlit as st
import os
from streamlit_menu.st_menu import getMenu

parent_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(parent_dir, "style.css")


def st_menu(menu={},  on_change=None, args=None):
    with st.sidebar:
        getMenu(menu=menu,
                collapsible=menu.collapsible,
                key="sidemenu",
                on_select=on_change,
                args=args)
                
    return st.session_state["sidemenu"]