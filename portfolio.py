import streamlit as st
from tabs import home
from tabs import tugas

TAB_LABEL_MODULES = {
    '🪪 Biodata': home,
    '✍🏻 Tugas': tugas
}

def main():

    st.set_page_config(
        page_icon=':woman:',
        page_title='Aisah',
        layout='wide',
    )
          
    st.markdown("""
        <style>
            .block-container {padding-top: 1rem !important;}
        </style>""",
        unsafe_allow_html=True,
    )

    # layout not final
    left_col, main_col, right_col = st.columns([20, 100, 20])

    with main_col:
        st.title('Aisah')
        st.markdown(
            '[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ichaicha1020@gmail.com)'
            ' | '
            '[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_aisyca_)',
            unsafe_allow_html=True
        )
            
        tabs = st.tabs(TAB_LABEL_MODULES.keys())
        for tab, tab_module in zip(tabs, TAB_LABEL_MODULES.values()):
            with tab:
                tab_module.st_all()

if __name__ == "__main__":
    main()