"""Frameworks for running multiple Streamlit pages in a single app.
"""


class MultiPage:
    """Framework for combining multiple pages streamlit.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        pages = MultiPage()
        pages.add_page("Foo", foo)
        pages.add_page("Bar", bar)
        pages.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        pages = MultiPage()
        pages.add_page("Foo", foo)
        pages.add_page("Bar", bar)
        pages.run()
    """

    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        """Adds a new page.
        Parameters
        ----------
        func:
            the python function to render this page.
        title:
            title of the page. Appears in the menu in the sidebar.
        """
        self.pages.append({"title": title, "function": func})

    def run(self, title):
        result = next(filter(lambda ele: ele['title'] == title, self.pages),
                      None)
        result["function"]()