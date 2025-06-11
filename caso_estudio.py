import streamlit as st
import pandas as pd

def mostrar_caso_estudio():

    
    st.markdown("""
    ## Antecedentes
    
    TechNova Retail es una cadena multinacional especializada en productos tecnológicos y electrónicos que opera en diversos países. 
    La empresa ha experimentado un crecimiento sostenido en los últimos años, pero enfrenta desafíos significativos en un mercado 
    cada vez más competitivo y con cambios rápidos en preferencias de los consumidores.
    
    Tras la expansión a nuevos mercados internacionales, la dirección de TechNova necesita comprender mejor los patrones de 
    comportamiento de sus clientes en diferentes regiones, evaluar el rendimiento de sus categorías de productos y optimizar 
    sus estrategias de ventas y marketing.
    """)
    
    st.markdown("""
    ## Objetivos del Análisis
    
    El objetivo principal es analizar los datos de ventas de la cadena multinacional utilizando herramientas de visualización
    como Python, con un enfoque especial en geovisualización para identificar patrones por país y ciudad, evaluar el comportamiento
    del cliente y optimizar estrategias de ventas.
    """)
    
    st.markdown("""
    ## Conjunto de Datos
    
    El conjunto de datos contiene información detallada sobre:
    
    - Productos vendidos (nombre, categoría)
    - Precios y cantidades
    - Fechas de transacción
    - Ubicación geográfica (país, ciudad)
    - Método de pago
    - Datos demográficos del cliente (edad, género)
    - Nivel de satisfacción reportado
    """)
    
    st.markdown("""
    ## Metodología de Análisis
    
    1. **Limpieza y transformación de datos**
    2. **Análisis de distribución de ventas**
    3. **Visualizaciones avanzadas:**
       - Gráfico de Barras Apiladas: Ventas por categoría y método de pago
       - Gráfico de Calor (Heatmap): Correlación entre variables clave
       - Boxplot: Distribución de precios por categoría
       - Gráfico de Líneas: Evolución de la satisfacción del cliente
       - Mapas: Análisis geográfico de ventas
       - Segmentación de mercado por edad y género
    4. **Análisis de insights y recomendaciones estratégicas**
    """)
    
    st.markdown("""
    ## Resultados Esperados
    
    - Identificación de patrones de ventas por ubicación geográfica
    - Comprensión de preferencias de pago por categoría
    - Análisis de correlaciones entre variables clave
    - Segmentación efectiva del mercado
    - Recomendaciones estratégicas basadas en datos
    """)
