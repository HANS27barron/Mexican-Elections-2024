import streamlit as st
#from file import newFile
#from sheets import select

# pip install streamlit
# streamlit run home.py
# https://docs.streamlit.io/develop/concepts/architecture/run-your-app

if 'presiSi' not in st.session_state:
    st.session_state.presiSi = 0
if 'presiNo' not in st.session_state:
    st.session_state.presiNo = 0
if 'selection_made' not in st.session_state:
    st.session_state.selection_made = False

st.title(":green[Elecciones] :white[Federales] :red[2024]")

st.subheader("Inicio", divider='violet')


st.write("En este sitio podrás encontrar todas la información sobre los resultados de las elecciones federales de este año.")
st.write("Aquí podrás conocer a nuestra próxima presidente, senadores, diputados, gobernadores y alcaldes de todos los estados. Además, podrás consultar las estadísticas de los votos obtenidos por candidato.")
st.image('https://www.eleconomista.com.mx/__export/1712159949716/sites/eleconomista/img/2024/04/01/elecciones_2024_mexicanos_votaran_20708_cargos_publicos.png_783160999.png', caption='(Mapa Electoral 2024)')


st.write("Selecciona en cada de los siguientes cargos para conocer a los ganadores y dar tu aprobación o rechazo")

with st.expander("Presidente de la República"):
    st.write("Claudia Sheinbaum Pardo")
    st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/06/230619105835-mexico-city-mayor-claudia-sheinbaum-full-169.jpg?quality=100&strip=info&w=320&h=240&crop=1")
    st.page_link("pages/Presidente.py", label="Haz click aquí para más información")
    presiSi = 0
    presiNo = 0
    Opcion = st.radio( "",
        ["Apruebo", "Rechazo"],
        key="visibility",
        label_visibility="visible",
        disabled=False,
        horizontal=True,
    )
    if Opcion == "Apruebo" and not st.session_state.selection_made:
        st.session_state.presiSi += 1
        st.write(f"{st.session_state.presiSi} personas también aprobaron")
        st.session_state.selection_made = True
    elif Opcion == "Rechazo" and not st.session_state.selection_made:
        st.session_state.presiNo += 1
        st.write(f"{st.session_state.presiNo} personas también rechazaron")
        st.session_state.selection_made = True

with st.expander("Cámara de Senadores del Congreso de la Unión"):
    st.page_link("pages/Senadores.py", label="Haz click aquí para más información")
    st.write(select)

x = st.slider("How much do u know?", 0,10)
if x<3:
    st.write("You need to start learning!")
if 3<=x<=6:
    st.write("Keep on learning")
if 6<x<=9:
    st.write("Just a few more!")
if x==10:
    st.write("Finished!")

#sidebar_logo = "https://www.ibo.org/globalassets/new-structure/icons-and-logos/images/dp-programme-logo-es.png"

#st.logo(sidebar_logo)
#st.sidebar.markdown("Mathematics AA IB")

#st.write(F)
