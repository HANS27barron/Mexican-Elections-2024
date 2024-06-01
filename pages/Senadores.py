import streamlit as st
from Estados import sen
from Estados import chart_data
from Estados import estadoS
from Partidos import chart_Partidos
from Partidos import senadores_partidos
from Partidos import cand_MC
from Partidos import cand_Historia
from Partidos import cand_Fuerza
from Partidos import cand_Morena
from Partidos import cand_PT
from Partidos import cand_PV
from Partidos import cand_PRI
from Partidos import cand_PAN
from Partidos import cand_PRD

st.title(":green[Senadores ] :white[de la LXVI ] :red[Legislatura]")
st.header("", divider='red')

##imagenes
MC = "https://movimientociudadanosonora.com/wp-content/uploads/2021/10/logoMC-naranja.png"
PAN = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/PAN_logo_%28Mexico%29.svg/2048px-PAN_logo_%28Mexico%29.svg.png"
PRI = "https://upload.wikimedia.org/wikipedia/commons/e/ec/PRI_%28partido_revolucionario_institucional%29_logo_%28Mexico%29.png"
PRD = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/PRD_logo_%28Mexico%29.svg/1200px-PRD_logo_%28Mexico%29.svg.png"
MORENA = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Morena_logo_%28alt%29.svg/2048px-Morena_logo_%28alt%29.svg.png"
PT = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Worker%27s_Party_logo_%28Mexico%29.svg/1022px-Worker%27s_Party_logo_%28Mexico%29.svg.png"
PV = "https://upload.wikimedia.org/wikipedia/commons/a/ae/Logo-partido-verde-2020.png"


col1, col2, col3 = st.columns(3)
with col1:
       estados = st.button("Estados")
with col2:
       partidos = st.button("Partidos")
with col3:
       popul = st.button("Popularidad")


if partidos:
        st.header("Candidaturas por Partidos y Coaliciónes")
        st.bar_chart(chart_Partidos)
        st.write("")
        st.header("Partidos o Coaliciónes")

        with st.expander("Movimiento Ciudadano (MC)"):
               st.image(MC, width=200)
               st.write(cand_MC)

        with st.expander("Fuerza y Corazón por México (PRI-PAN-PRD)"):
               col1, col2, col3 = st.columns(3)
               with col1:
                st.image(PRI, width=115)
                with col2:
                 st.image(PAN, width=115)
                with col3:
                 st.image(PRD, width=125)
               st.write(cand_Fuerza)
        
        with st.expander("Sigamos Haciendo Historia (Morena-PT-PVEM)"):
               col1, col2, col3 = st.columns(3)
               with col1:
                st.image(MORENA, width=115)
                with col2:
                 st.image(PT, width=120)
                with col3:
                 st.image(PV, width=115)
               st.write("2")
               st.write(cand_Historia)

        with st.expander("Movimiento de Regeneración Nacional (Morena)"):
               st.image(MORENA, width=125)
               st.write(cand_Morena)

        with st.expander("Partido Verde Ecologista de México (PVEM)"):
               st.image(PV, width=125)
               st.write(cand_PV)

        with st.expander("Partido del Trabajo (PT)"):
               st.image(PT, width=120)
               st.write(cand_PT)   

        with st.expander("Partido Acción Nacional (PAN)"):
               st.image(PAN, width=125)
               st.write(cand_PAN)

        with st.expander("Partido Revolucionario (PRI)"):
               st.image(PRI, width=120)
               st.write(cand_PRI)

        with st.expander("Partido De La Revolución Democrática (PRD)"):
              st.image(PRD, width=120)
              st.write(cand_PRD)

        st.text(senadores_partidos)


elif popul:
       st.write("C")
else:
        st.header("Candidaturas por Estado")
        st.bar_chart(chart_data)
        st.write("")
        st.header("Estados")

        with st.expander("Aguascalientes"):
                st.subheader(":red[Ganador]", divider='red')

        with st.expander("Baja California"):
                st.write("Ganador")

        with st.expander("Baja California Sur"):
                st.write("Ganador")

        with st.expander("Campeche"):
                st.write("Ganador")

        with st.expander("Chiapas"):
                st.write("Ganador")

        with st.expander("Chihuahua"):
                st.write("Ganador")

        with st.expander("CDMX"):
                st.write("Ganador")

        with st.expander("Coahuila"):
                st.write("Ganador")

        with st.expander("Colima"):
                 st.write("Ganador")

        with st.expander("Durango"):
                st.write("Ganador")

        with st.expander("EDOMEX"):
                 st.write("Ganador")

        with st.expander("Guanajuato"):
                 st.write("Ganador")

        with st.expander("Guerrero"):
                  st.write("Ganador")

        with st.expander("Hidalgo"):
                  st.write("Ganador")

        with st.expander("Jalisco"):
         st.write("Ganador")

        with st.expander("Michoacán"):
         st.write("Ganador")

        with st.expander("Morelos"):
                st.write("Ganador")

        with st.expander("Nayarit"):
                st.write("Ganador")

        with st.expander("Nuevo León"):
                st.write("Ganador")

        with st.expander("Oaxaca"):
                st.write("Ganador")

        with st.expander("Puebla"):
         st.write("Ganador")

        with st.expander("Querétaro"):
         st.write("Ganador")

        with st.expander("Quintana Roo"):
                st.write("Ganador")

        with st.expander("San Luis Potosí"):
                st.write("Ganador")

        with st.expander("Sinaloa"):
                st.write("Ganador")

        with st.expander("Sonora"):
                st.write("Ganador")

        with st.expander("Tabasco"):
                st.write("Ganador")

        with st.expander("Tamaulipas"):
                st.write("Ganador")

        with st.expander("Tlaxcala"):
                st.write("Ganador")

        with st.expander("Veracruz"):
                 st.write("Ganador")

        with st.expander("Yúcatan"):
          st.write("Ganador")

        with st.expander("Zacatecas"):
         st.write("Ganador")
        
        st.text(sen)