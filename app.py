import streamlit as st

# Set the page config with the icon and wide layout at the start of the app
st.set_page_config(
    page_title="A7's Document Converter",
    page_icon="🛠️️",  # Unicode icon
    layout="wide",  # Page layout to wide
)

# Define the pages with file names and titles
pages = {
    "Utility Tools": [
        st.Page("home.py", title=" 🏡  Home"),
        st.Page("exceltoword.py", title="Excel to Word"),
        st.Page("pdftoword.py", title="PDF to Word"),
        st.Page("rtftopdf.py", title="RTF to PDF"),
        st.Page("txttopdf.py", title="TXT to PDF"),
        st.Page("wordtopdf.py", title="Word to PDF"),
        st.Page("jsontopdf.py", title="JSON to PDF"),
        st.Page("phototopdf.py", title="Images to PDF"),
    ],
}

# Create the navigation menu
pg = st.navigation(pages)
pg.run()

# Footer content for the sidebar
st.sidebar.markdown(
    """
    <br><br><br><br>  <!-- Spacing for footer to be pushed to the bottom -->
    Made by A7 Nostalgic under A7's Garage<br>
    Any Bugs or Suggestions<br><br>
    Feel free to reach out at: <a href="mailto:a7sgarage@gmail.com">a7sgarage@gmail.com</a>
    """,
    unsafe_allow_html=True,
)
