import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        margin: 0;
    }
    .main-content {
        flex: 1;
    }
    .title {
        text-align: left;
        font-family: 'Gill Sans', sans-serif;
        color: #2E86C1;
        font-size: 2.0em;
        margin-top: 20px;
    }
    .description {
        text-align: left;
        font-family: 'Verdana', sans-serif;
        color: #555;
        font-size: 1.0em;
        margin-top: 15px;
        margin-bottom: 40px;
        line-height: 1.6;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-family: 'Arial', sans-serif;
        color: #888;
        font-size: 0.9em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Content
st.markdown("<div class='title'>A7's Document Converter</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class='description main-content'>
        <br>
        Hello there, this is a small Python, Streamlit-based web application. This web app allows document
        conversion from one format to another. I hope all my work will help you and make your day better.
        Have a nice day!<br><br>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer at the bottom right
st.markdown(
    """
    <div class='footer'>
        By A7 Nostalgic under A7's Garage.<br>
        Freeware and Shareware, licensed by PENNAR.
    </div>
    """,
    unsafe_allow_html=True,
)
