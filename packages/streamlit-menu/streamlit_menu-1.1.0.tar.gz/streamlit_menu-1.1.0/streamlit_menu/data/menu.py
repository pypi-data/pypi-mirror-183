from data.logo import logo
from data.style import dividerBetweenHeaderAndBody, menuWrapperStyle, menuHeaderStyle, mainMenuStyle, submenuStyle

logo = logo

collapsible = False
title = "Gmail Clone"

menuData = [
    {
        "id": 1,
        "title": "Social",
        "icon": "fa-solid fa-users",
        "children": None,
    },
    {
        "id": 2,
        "title": "Starred",
        "icon": "fa-solid fa-star",
        "children": None,
    },
    {
        "id":
        3,
        "title":
        "All mails",
        "icon":
        "fa-solid fa-envelope",
        "children": [
            {
                "id": 4,
                "title": "Sent",
                "icon": "fa-solid fa-share-from-square",
                "children": None,
            },
            {
                "id": 5,
                "title": "Important",
                "icon": "fa-solid fa-note-sticky",
                "children": None,
            },
            {
                "id": 6,
                "title": "Spam",
                "icon": "fa-solid fa-triangle-exclamation",
                "children": None,
            },
        ],
    },
    {
        "id": 7,
        "title": "Bin",
        "icon": "fa-solid fa-trash-can",
        "children": None,
    },
    {
        "id": 8,
        "title": "Settings",
        "icon": "fa-solid fa-gear",
        "children": None,
    },
    {
        "id": 9,
        "title": "Logout",
        "icon": "fa-solid fa-right-from-bracket",
        "children": None,
    },
]

menuHeader = {"logo": logo, "title": title}

menu = {
    "menuHeader": menuHeader,
    "menuData": menuData,
    "dividerBetweenHeaderAndBody": dividerBetweenHeaderAndBody,
    "menuWrapperStyle": menuWrapperStyle,
    "menuHeaderStyle": menuHeaderStyle,
    "mainMenuStyle": mainMenuStyle,
    "submenuStyle": submenuStyle,
}
