import streamlit as st

def st_justify_align(text: str):
    st.markdown(
        f'<div style="text-align: justify; font-size: 1.1em;">{text}</div>',
        unsafe_allow_html=True
    )

def st_about():
    st.subheader('Tentang', divider=True)
    st_justify_align(
        """

Saya adalah pribadi yang secara alami memiliki rasa ingin tahu yang tinggi dan kemampuan analitis. Saya tertarik dengan bidang pendidikan, khususnya Pendidikan Agama Islam (PAI), terutama dalam upaya memberikan dampak positif, seperti dalam pembangunan karakter generasi muda dan penguatan moralitas masyarakat.

Saat ini, saya sedang menempuh pendidikan S1 dalam bidang Pendidikan Agama Islam (PAI) dan fokus untuk memperdalam pemahaman saya mengenai ilmu agama dan penerapannya dalam kehidupan sehari-hari.

Jika Anda membutuhkan informasi lebih lanjut atau ingin berdiskusi mengenai peluang dan kolaborasi, jangan ragu untuk menghubungi saya melalui [email](mailto:ichaicha1020@gmail.com) atau terhubung dengan saya di [Instagram](https://www.instagram.com/_aisyca_).
        """
    )


def st_bio():
    st.subheader('Profil', divider=True)
    
    st_justify_align("""
                     
Ketika saya berada di bangku sekolah menengah, saya mulai tertarik pada dunia pendidikan dan nilai-nilai agama. Ketertarikan ini berkembang seiring waktu, terutama dalam bidang Pendidikan Agama Islam (PAI). Saya percaya bahwa pendidikan agama memiliki peran penting dalam membentuk karakter generasi muda, dan ini menjadi motivasi utama saya untuk mendalaminya.

Saat ini, saya sedang menempuh pendidikan S1 dalam bidang Pendidikan Agama Islam (PAI). Saya berusaha untuk memperdalam pemahaman saya terhadap ilmu agama ini agar dapat memberikan kontribusi positif, baik dalam dunia pendidikan maupun dalam kehidupan sehari-hari. Selain itu, saya mengikuti seleksi Duta Baca Kampus, sebuah pengalaman yang memperluas wawasan saya tentang pentingnya literasi dalam membangun masyarakat yang cerdas.

Di luar itu, saya juga melakukan penelitian tentang tradisi terempoh yang memberikan wawasan berharga bagi saya.

Semua pengalaman ini membentuk diri saya menjadi seseorang yang berkomitmen untuk terus belajar, berkarya, dan memberikan dampak positif bagi lingkungan sekitar. Saya berharap perjalanan ini membawa saya pada tujuan yang lebih besar, baik dalam karier maupun kehidupan pribadi.""")

def st_interests():
    ...

def st_all():
    st_about()
    st_bio()