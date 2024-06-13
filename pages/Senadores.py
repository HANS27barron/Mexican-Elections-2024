import streamlit as st
from Estados import sen
from Estados import chart_data
from Estados import estadoS
from Partidos import chart_Partidos
from Partidos import senadores_partidos
from Estados import cand_Estado
from Estados import sen_Ganador
from Estados import color_Sen_Ganador

from Partidos import sen_Partido

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
               st.write(sen_Partido("Movimiento Ciudadano"))

        with st.expander("Fuerza y Corazón por México (PRI-PAN-PRD)"):
               col1, col2, col3 = st.columns(3)
               with col1:
                st.image(PRI, width=115)
                with col2:
                 st.image(PAN, width=115)
                with col3:
                 st.image(PRD, width=125)
               st.write(sen_Partido("Fuerza Y Corazon Por Mexico"))
        
        with st.expander("Sigamos Haciendo Historia (Morena-PT-PVEM)"):
               col1, col2, col3 = st.columns(3)
               with col1:
                st.image(MORENA, width=115)
                with col2:
                 st.image(PT, width=120)
                with col3:
                 st.image(PV, width=115)
               st.write("2")
               st.write(sen_Partido("Sigamos Haciendo Historia"))

        with st.expander("Movimiento de Regeneración Nacional (Morena)"):
               st.image(MORENA, width=125)
               st.write(sen_Partido("Morena"))

        with st.expander("Partido Verde Ecologista de México (PVEM)"):
               st.image(PV, width=125)
               st.write(sen_Partido("Partido Verde Ecologista De México"))

        with st.expander("Partido del Trabajo (PT)"):
               st.image(PT, width=120)
               st.write(sen_Partido("Partido Del Trabajo"))   

        with st.expander("Partido Acción Nacional (PAN)"):
               st.image(PAN, width=125)
               st.write(sen_Partido("Partido Acción Nacional"))

        with st.expander("Partido Revolucionario Institucional (PRI)"):
               st.image(PRI, width=120)
               st.write(sen_Partido("Partido Revolucionario Institucional"))

        with st.expander("Partido De La Revolución Democrática (PRD)"):
              st.image(PRD, width=120)
              st.write(sen_Partido("Partido De La Revolución Democrática"))

        st.text(senadores_partidos)


elif popul:
       st.write("C")
else:
        st.header("Candidaturas por Estado")
        st.bar_chart(chart_data)
        st.write("")
        st.header("Estados")

        with st.expander("Aguascalientes"):
                color = color_Sen_Ganador("Aguascalientes")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Aguascalientes"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Aguascalientes"))

        with st.expander("Baja California"):
                color = color_Sen_Ganador("Baja California")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Baja California"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Baja California"))

        with st.expander("Baja California Sur"):
                color = color_Sen_Ganador("Baja California Sur")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Baja California Sur"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Baja California Sur"))

        with st.expander("Campeche"):
                color = color_Sen_Ganador("Campeche")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Campeche"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Campeche"))

        with st.expander("Chiapas"):
                color = color_Sen_Ganador("Chiapas")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Chiapas"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Chiapas"))

        with st.expander("Chihuahua"):
                color = color_Sen_Ganador("Chihuahua")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Chihuahua"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Chihuahua"))

        with st.expander("Ciudad de México"):
                color = color_Sen_Ganador("Ciudad De México")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Ciudad De México"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Ciudad De México"))
  
        with st.expander("Coahuila"):
                color = color_Sen_Ganador("Coahuila")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Coahuila"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Coahuila"))

        with st.expander("Colima"):
                color = color_Sen_Ganador("Colima")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Colima"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Colima"))

        with st.expander("Durango"):
                color = color_Sen_Ganador("Durango")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Durango"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Durango"))

        with st.expander("Estado de México"):
                color = color_Sen_Ganador("Estado De México")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Estado De México"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Estado De México"))

        with st.expander("Guanajuato"):
                color = color_Sen_Ganador("Guanajuato")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Guanajuato"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Guanajuato"))

        with st.expander("Guerrero"):
                color = color_Sen_Ganador("Guerrero")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Guerrero"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Guerrero"))

        with st.expander("Hidalgo"):
                color = color_Sen_Ganador("Hidalgo")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Hidalgo"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Hidalgo"))

        with st.expander("Jalisco"):
                color = color_Sen_Ganador("Jalisco")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Jalisco"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Jalisco"))

        with st.expander("Michoacán"):
                color = color_Sen_Ganador("Michoacán")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Michoacán"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Michoacán"))

        with st.expander("Morelos"):
                color = color_Sen_Ganador("Morelos")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Morelos"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Morelos"))

        with st.expander("Nayarit"):
                color = color_Sen_Ganador("Nayarit")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Nayarit"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Nayarit"))

        with st.expander("Nuevo León"):
                color = color_Sen_Ganador("Nuevo León")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Nuevo León"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Nuevo León"))

        with st.expander("Oaxaca"):
                color = color_Sen_Ganador("Oaxaca")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Oaxaca"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Oaxaca"))

        with st.expander("Puebla"):
                color = color_Sen_Ganador("Puebla")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Puebla"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Puebla"))

        with st.expander("Querétaro"):
                color = color_Sen_Ganador("Querétaro")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Querétaro"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Querétaro"))

        with st.expander("Quintana Roo"):
                color = color_Sen_Ganador("Quintana Roo")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Quintana Roo"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Quintana Roo"))

        with st.expander("San Luis Potosí"):
                color = color_Sen_Ganador("San Luis Potosí")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("San Luis Potosí"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("San Luis Potosí"))

        with st.expander("Sinaloa"):
                color = color_Sen_Ganador("Sinaloa")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Sinaloa"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Sinaloa"))

        with st.expander("Sonora"):
                color = color_Sen_Ganador("Sonora")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Sonora"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Sonora"))

        with st.expander("Tabasco"):
                color = color_Sen_Ganador("Tabasco")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Tabasco"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Tabasco"))

        with st.expander("Tamaulipas"):
                color = color_Sen_Ganador("Tamaulipas")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Tamaulipas"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Tamaulipas"))

        with st.expander("Tlaxcala"):
                color = color_Sen_Ganador("Tlaxcala")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Tlaxcala "))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Tlaxcala"))

        with st.expander("Veracruz"):
                color = color_Sen_Ganador("Veracruz")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Veracruz"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Verecruz"))

        with st.expander("Yucatán"):
                color = color_Sen_Ganador("Yucatán")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Yucatán"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Yucatán"))

        with st.expander("Zacatecas"):
                color = color_Sen_Ganador("Zacatecas")
                st.subheader(f":{color}[Ganadores]", divider=color)
                st.write(sen_Ganador("Zacatecas"))
                st.subheader("Candidatos", divider="grey")
                st.write(cand_Estado("Zacatecas"))
        
        st.text(sen)