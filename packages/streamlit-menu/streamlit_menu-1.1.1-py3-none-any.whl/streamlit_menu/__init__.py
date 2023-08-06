import streamlit as st
import os
from streamlit_menu.st_menu import getMenu
from streamlit_menu.multipage import MultiPage

# import your app modules here
from streamlit_menu.my_pages import social, starred, sent, spam, important, bin, settings, logout

parent_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(parent_dir, "style.css")


def st_menu(menu, collapsible=False):    
    pages = MultiPage()

    # Add all your application here
    pages.add_page("Social", social.index)
    pages.add_page("Starred", starred.index)
    pages.add_page("Sent", sent.index)
    pages.add_page("Spam", spam.index)
    pages.add_page("Important", important.index)
    pages.add_page("Bin", bin.index)
    pages.add_page("Settings", settings.index)
    pages.add_page("Logout", logout.index)

    def on_menu_select(widgetkey):
        pages.run(st.session_state["sidemenu"])

    with st.sidebar:
        getMenu(menu=menu,
                collapsible=collapsible,
                key="sidemenu",
                on_select=on_menu_select,
                args=("sidemenu", ))

