#importar librerias
import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load('./src/catboost.joblib')


rango_edad =  ["Hasta 24 años", "25 a 34 años", "35 a 44 años", "45 a 54 años", "55 a 64 años", "65 a más años"]
genero = ["Femenino", "Masculino"]
departamentos = [ "Amazonas", "Ancash", "Apurímac", "Arequipa", "Ayacucho", "Cajamarca", "Cusco", "Huancavelica",
                 "Huánuco", "Ica", "Junín", "La Libertad", "Lambayeque", "Lima", "Loreto", "Madre de Dios", "Moquegua",
                 "Pasco", "Piura", "Puno", "San Martín", "Tacna", "Tumbes", "Callao", "Ucayali"]
trabajos = [
    "TRABAJADOR PORTUARIO O PANIFICADOR", "PRACTICANTE SENATI", "PENSIONISTA",
    "PENSIONISTA LEY N.28320", "CONSTRUCCION CIVIL", "PILOTO Y COPILOTO DE AVIACION",
    "MARITIMO,FLUVIAL O LACUSTRE", "PERIODISTA", "TRAB. DE LA INDUSTRIA DE CUERO",
    "MINERO DE SOCAVON", "PESCADOR", "TRABAJADORES DEL HOGAR", "PENSIONISTA TRABAJADOR",
    "TRABAJADOR PESQUERO", "MINERO DE TAJO ABIERTO", "FACULTATIVO INDEPENDIENTE",
    "CONTINUACION FACULTATIVA", "ARTISTAS", "TRABAJADOR INDEPENDIENTEAFILIADO OBLIGATORIO",
    "AGRARIO DEPENDIENTE - LEY 27360", "TRABAJADOR ACTIVIDAD ACUICOLA",
    "PESCADOR Y PROCESADORARTESANAL INDEPEN", "PS REG. ESPECIAL D. LEG. 1057",
    "TRABAJADOR DE LA MICROEMPRESA - AFILIAD", "CONDUCTOR DE LA MICROEMPRESA - AFILIADO",
    "CONDUCTOR DE LA MICROEMPRESA - SEGURO R", "CONDUCTOR DE MICROEMPRESAREMYPE - D.LE",
    "PERSONAL DE ESCUELASFISCALIZADAS", "SOCIO COOP AGRARIA LEY 29972",
    "PERSONA CON ING.DE 4TA", "SERVIDOR PÚBLICO - DIRECTIVOSUPERIOR",
    "SERVIDOR PÚBLICO - EJECUTIVO", "SERVIDOR PÚBLICO - ESPECIALISTA",
    "SERVIDOR PÚBLICO - DE APOYO", "GERENTES PÚBLICOS - D. LEG.N. 1024",
    "MIEMBROS DE OTROS REG.ESPECIALES", "FUNCIONARIO PUBLICO - LEY 30057",
    "DIRECTIVO PUBLICO - LEY 30057", "SERVIDOR CIVIL DE CARRERA - LEY 30057",
    "CUARTA - QUINTA INCISO F", "MAGISTERIO - LEY 29944", "SERVIDOR DE ACTIVIDADES COMPLEMENTARIAS",
    "PERSONAS QUE GENERAINGRESOS DE CUARTA", "SCTR"
]

trabajos_dict = {
    "TRABAJADOR PORTUARIO O PANIFICADOR": 22,
    "PRACTICANTE SENATI": 23,
    "PENSIONISTA": 24,
    "PENSIONISTA LEY N.28320": 26,
    "CONSTRUCCION CIVIL": 27,
    "PILOTO Y COPILOTO DE AVIACION": 28,
    "MARITIMO,FLUVIAL O LACUSTRE": 29,
    "PERIODISTA": 30,
    "TRAB. DE LA INDUSTRIA DE CUERO": 31,
    "MINERO DE SOCAVON": 32,
    "PESCADOR": 33,
    "TRABAJADORES DEL HOGAR": 34,
    "PENSIONISTA TRABAJADOR": 35,
    "TRABAJADOR PESQUERO": 36,
    "MINERO DE TAJO ABIERTO": 37,
    "FACULTATIVO INDEPENDIENTE": 53,
    "CONTINUACION FACULTATIVA": 54,
    "ARTISTAS": 56,
    "TRABAJADOR INDEPENDIENTEAFILIADO OBLIGATORIO": 59,
    "AGRARIO DEPENDIENTE - LEY 27360": 64,
    "TRABAJADOR ACTIVIDAD ACUICOLA": 65,
    "PESCADOR Y PROCESADORARTESANAL INDEPEN": 66,
    "PS REG. ESPECIAL D. LEG. 1057": 67,
    "TRABAJADOR DE LA MICROEMPRESA - AFILIAD": 68,
    "CONDUCTOR DE LA MICROEMPRESA - AFILIADO": 69,
    "CONDUCTOR DE LA MICROEMPRESA - SEGURO R": 70,
    "CONDUCTOR DE MICROEMPRESAREMYPE - D.LE": 71,
    "PERSONAL DE ESCUELASFISCALIZADAS": 72,
    "SOCIO COOP AGRARIA LEY 29972": 73,
    "PERSONA CON ING.DE 4TA": 80,
    "SERVIDOR PÚBLICO - DIRECTIVOSUPERIOR": 84,
    "SERVIDOR PÚBLICO - EJECUTIVO": 85,
    "SERVIDOR PÚBLICO - ESPECIALISTA": 86,
    "SERVIDOR PÚBLICO - DE APOYO": 87,
    "GERENTES PÚBLICOS - D. LEG.N. 1024": 90,
    "MIEMBROS DE OTROS REG.ESPECIALES": 91,
    "FUNCIONARIO PUBLICO - LEY 30057": 92,
    "DIRECTIVO PUBLICO - LEY 30057": 93,
    "SERVIDOR CIVIL DE CARRERA - LEY 30057": 94,
    "CUARTA - QUINTA INCISO F": 95,
    "MAGISTERIO - LEY 29944": 96,
    "SERVIDOR DE ACTIVIDADES COMPLEMENTARIAS": 97,
    "PERSONAS QUE GENERAINGRESOS DE CUARTA": 98,
    "SCTR": 99
}

sexo_dic = {
    "Femenino" : 0,
    "Masculino" : 1
}

departamentos_dic = {
    "Amazonas": 1, "Ancash": 2, "Apurímac": 3, "Arequipa": 4, "Ayacucho": 5, "Cajamarca": 6, 
    "Cusco": 7, "Huancavelica": 8, "Huánuco": 9, "Ica": 10, "Junín": 11, "La Libertad": 12,
    "Lambayeque": 13, "Lima": 14, "Loreto": 15, "Madre de Dios": 16, "Moquegua": 17, 
    "Pasco": 18, "Piura": 19, "Puno": 20, "San Martín": 21, "Tacna": 22, "Tumbes": 23, 
    "Callao": 24, "Ucayali": 25
}

rango_edad_dic = {
    "Hasta 24 años": 1,
    "25 a 34 años": 2,
    "35 a 44 años": 3,
    "45 a 54 años": 4,
    "55 a 64 años": 5,
    "65 a más años": 6
}

aportante_dic = {
    "No": 0,
    "Sí": 1
}

tipo_afil_dic = {
    "Obligatorio" : 1,
    "Facultativo" : 2,
    "Libre desafiliación" : 3
}

tipo_dep_dic = {
    "Dependiente": 1,
    "Independiente": 2
}

tipo_empleo_dic = {
    "Privado" : 0,
    "Publico" : 1
}

cat_columns = ['departamento', 'tipo_afil', 'tipo_dep', 'tipo_trabajador']


def main():
    
    st.title('Predicción de cantidad de aportes al Sistema Nacional de Pensiones (SNP)')
    
    st.sidebar.header('User Input Parameters')
   
    def user_input_parameters():
        sexo = st.sidebar.selectbox('Sexo', genero)
        edad = st.sidebar.slider('Edad', 1, 100, 50)
        r_edad = st.sidebar.selectbox('Rando de edad', rango_edad)
        departamento = st.sidebar.selectbox('Departamento', departamentos)
        aportante = st.sidebar.selectbox('Aportante', ['No', 'Sí'])
        tipo_afil = st.sidebar.selectbox('Tipo de afiliación', ['Obligatorio', 'Facultativo', 'Libre desafiliación'])
        tipo_dep = st.sidebar.selectbox('Tipo de dependencia', ['Dependiente', 'Independiente'])
        tipo_trabajador = st.sidebar.selectbox('Ocupación', trabajos)
        tipo_empleo = st.sidebar.selectbox('Tipo Empleo', ['Privado', 'Publico'])
        aporte = st.sidebar.slider('Cantidad Aportada en el último mes', 0.0, 24050.0, 5.3)
        remuneración = st.sidebar.slider('Remuneración obtenida en el último mes', 0.0, 185000.0, 10.1)
        aportes = st.sidebar.slider('Cantidad de aportes', 0, 50, 1)
        tiempo_aportado = st.sidebar.slider('Tiempo aportado en meses', 0, 631, 1)

        data = {'sexo': sexo,
                'edad': edad,
                'r_edad': r_edad,
                'departamento': departamento,
                'aportante': aportante,
                'tipo_afil': tipo_afil,
                'tipo_dep': tipo_dep,
                'tipo_trabajador' : tipo_trabajador,
                'tipo_empleo' : tipo_empleo,
                'aporte' : aporte,
                'remuneracion' : remuneración,
                'nro_aportes' : aportes,
                'tiempo_aporte_mes' : tiempo_aportado
                }
        
        features = pd.DataFrame(data, index=[0])

        features['sexo'] = features['sexo'].replace(sexo_dic)
        features['r_edad'] = features['r_edad'].replace(rango_edad_dic)
        features['departamento'] = features['departamento'].replace(departamentos_dic)
        features['aportante'] = features['aportante'].replace(aportante_dic)
        features['tipo_trabajador'] = features['tipo_trabajador'].replace(trabajos_dict)
        features['tipo_afil'] = features['tipo_afil'].replace(tipo_afil_dic)
        features['tipo_dep'] = features['tipo_dep'].replace(tipo_dep_dic)
        features['tipo_empleo'] = features['tipo_empleo'].replace(tipo_empleo_dic)

        features[cat_columns] = features[cat_columns].astype(str)
        features['tiempo_aporte_mes'] = features['tiempo_aporte_mes'].astype(np.float64)
        print(features.info())

        return features

    df = user_input_parameters()


    st.subheader('User Input Parameters')
    st.write(df)

    if st.button('RUN'):
        prediction = model.predict(df)
        st.subheader('Monto aportado')
        st.write(f'S/{prediction[0]:.2f}')


if __name__ == '__main__':
    main()
    