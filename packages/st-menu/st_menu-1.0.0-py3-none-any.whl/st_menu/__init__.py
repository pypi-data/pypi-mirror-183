def st_menu():  
    import streamlit as st
    import data.menu_data.menu
    from st_menu import getMenu
    from multipage import MultiPage
    from my_pages import social, starred, sent, spam, important, bin, settings, logout  # import your app modules here

    with open("style.css") as stylefile:
        st.markdown(f"<style>{stylefile.read()}</style>", unsafe_allow_html=True)

    # st.subheader("Menu Component")

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


    # column_left, column_center, column_right = st.columns(3)

    with st.sidebar:
        getMenu(menu=data.menu_data.menu.menu,
                collapsible=data.menu_data.menu.collapsible,
                key="sidemenu",
                on_select=on_menu_select,
                args=("sidemenu", ))

    # with column_left:
    #     st.write('You have selected: ', st.session_state["sidemenu"])

    # with column_right:
    #     st.write("right side")

st_menu()