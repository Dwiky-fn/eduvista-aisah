import streamlit as st

def st_justify_align(text: str, font_size: str = "2em"):
    st.markdown(
        f'<div style="text-align: justify; font-size: {font_size};">{text}</div>',
        unsafe_allow_html=True
    )

def st_vidPembelajaran():
    st.subheader('PPT', divider=True)
    st_justify_align(
        """

1. Ketentuan Kurban ([Powtoon](https://drive.google.com/file/d/1gVrJjSezMyhxe1VjWdLGAnW0JmCux2EB/view?usp=sharing))
        """
    )

def st_slidePembelajaran():
    st.subheader('QUIZ', divider=True)
    st_justify_align(
        """

1. Ketentuan Kurban ([Wordwall](https://wordwall.net/play/81425/315/856))
        """
    )

def st_filePembelajaran():
    st.subheader('File', divider=True)
    st_justify_align(
        """

1. Resume Media Pembelajaran ([PDF](https://drive.google.com/file/d/1c8vot_-LBlnYFph-0S4mwGdXcBgFyAWF/view))
        """
    )

def st_all():
    st_vidPembelajaran()
    st_slidePembelajaran()
    st_filePembelajaran()