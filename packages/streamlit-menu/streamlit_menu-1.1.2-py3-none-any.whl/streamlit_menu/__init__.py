import streamlit as st
import os
from streamlit_menu.st_menu import getMenu

parent_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(parent_dir, "style.css")


def st_menu(menu, collapsible=False):

    def on_menu_select(widgetkey):
        pass

    with st.sidebar:
        getMenu(menu=menu,
                collapsible=collapsible,
                key="sidemenu",
                on_select=on_menu_select,
                args=("sidemenu", ))
