import streamlit as st

# Constantes para textos repetidos
DESCRIPCION = "Descripción:"
VENTAJAS = "Ventajas:"
DESVENTAJAS = "Desventajas:"
CASOSUSO = "Casos de uso ideales:"
VER_DETALLES = "Ver detalles"

def mostrar_caso_estudio():
    st.markdown("<h1 style='font-size: 36px; color: #1a365d;'>Caso de estudio: Análisis de métricas de proyectos de software</h1>", unsafe_allow_html=True)
    
    # Introducción
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Introducción</h2>", unsafe_allow_html=True)
    st.write("""
    El análisis de métricas de proyectos de software es fundamental para evaluar el rendimiento de los equipos de desarrollo, 
    identificar áreas de mejora y optimizar los procesos de desarrollo. En este caso de estudio, analizaremos un conjunto 
    de datos que contiene métricas de diferentes equipos a lo largo de varios sprints, utilizando diversas librerías 
    de visualización de Python para extraer insights valiosos.
    """)
    
    # Objetivos
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Objetivos</h2>", unsafe_allow_html=True)
    st.markdown("""
    - Identificar patrones y tendencias en las métricas de desarrollo a lo largo de los sprints.
    - Comparar el rendimiento de diferentes equipos en términos de productividad, calidad y eficiencia.
    - Analizar la relación entre diferentes métricas (horas de desarrollo, errores detectados, retrasos, etc.).
    - Identificar factores que contribuyen a los retrasos en las entregas y los costos excedentes.
    - Proporcionar recomendaciones basadas en datos para mejorar los procesos de desarrollo.
    """)
    
    # Investigación de herramientas
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Investigación de librerías de visualización de datos</h2>", unsafe_allow_html=True)
    st.write("""
    A continuación, se presenta una comparativa de cinco librerías populares de visualización de datos en Python: 
    Matplotlib, Seaborn, Plotly, Bokeh y GeoPandas. Se analizan sus características principales, 
    ventajas, desventajas y casos de uso ideales.
    """)
    
    # Matplotlib
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Librería 1: Matplotlib</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles", expanded=True):
        st.subheader(DESCRIPCION)
        st.write("""
        Matplotlib es una librería de visualización de datos en Python que proporciona una amplia gama de gráficos estáticos, 
        animados e interactivos. Es la base de muchas otras librerías de visualización y ofrece un control detallado sobre 
        cada aspecto de los gráficos.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Gran flexibilidad y control sobre todos los aspectos de los gráficos.
        - Amplia documentación y comunidad de usuarios.
        - Compatible con muchos formatos de salida (PNG, PDF, SVG, etc.).
        - Integración con bibliotecas numéricas como NumPy y Pandas.
        - Capacidad para crear gráficos personalizados complejos.
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Sintaxis verbosa que requiere más código para visualizaciones básicas.
        - Curva de aprendizaje pronunciada para usuarios principiantes.
        - Gráficos estáticos por defecto (aunque se pueden hacer interactivos con extensiones).
        - Estilo visual anticuado que requiere personalización para obtener resultados modernos.
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Visualizaciones científicas y académicas que requieren precisión y control detallado.
        - Gráficos personalizados complejos que no están disponibles en otras librerías.
        - Publicaciones y reportes que requieren gráficos de alta calidad en formatos específicos.
        - Análisis exploratorio de datos cuando se necesita control total sobre la visualización.
        """)
    
    # Seaborn
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Librería 2: Seaborn</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles"):
        st.subheader(DESCRIPCION)
        st.write("""
        Seaborn es una librería de visualización de datos basada en Matplotlib que proporciona una interfaz de alto nivel 
        para crear gráficos estadísticos atractivos e informativos. Está especialmente diseñada para trabajar con 
        estructuras de datos de Pandas y facilita la creación de visualizaciones complejas con pocas líneas de código.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Interfaz simplificada para crear gráficos estadísticos complejos.
        - Temas y paletas de colores atractivos predefinidos.
        - Integración perfecta con Pandas DataFrames.
        - Funciones específicas para visualizar distribuciones y relaciones entre variables.
        - Manejo automático de agrupaciones y agregaciones de datos.
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Menos flexible que Matplotlib para personalizaciones muy específicas.
        - Limitado a ciertos tipos de gráficos estadísticos.
        - Puede ser lento con conjuntos de datos muy grandes.
        - Gráficos estáticos sin capacidades interactivas nativas.
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Análisis exploratorio de datos estadísticos.
        - Visualización de distribuciones y relaciones entre variables.
        - Creación rápida de gráficos estadísticos atractivos con poco código.
        - Proyectos de ciencia de datos y análisis estadístico.
        """)
    
    # Plotly
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Librería 3: Plotly</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles"):
        st.subheader(DESCRIPCION)
        st.write("""
        Plotly es una librería de visualización de datos interactiva que permite crear gráficos dinámicos y dashboards 
        interactivos. Utiliza JavaScript (a través de la biblioteca Plotly.js) para renderizar gráficos en navegadores web, 
        lo que permite interacciones como zoom, pan, tooltips y selección de datos.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Gráficos interactivos con capacidades de zoom, pan y tooltips.
        - Amplia variedad de tipos de gráficos, incluidos 3D y mapas.
        - Excelente integración con frameworks web como Dash y Streamlit.
        - Exportación a formatos web interactivos (HTML, JSON).
        - Estilo visual moderno y atractivo por defecto.
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Mayor consumo de recursos que las librerías estáticas.
        - Curva de aprendizaje moderada debido a la amplia gama de opciones.
        - Puede ser lento con conjuntos de datos muy grandes debido a la interactividad.
        - Algunas funcionalidades avanzadas requieren una suscripción de pago (Plotly Enterprise).
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Dashboards interactivos y aplicaciones web de análisis de datos.
        - Presentaciones y reportes interactivos para stakeholders.
        - Exploración de datos complejos que se benefician de la interactividad.
        - Visualizaciones que requieren interacción del usuario para descubrir patrones.
        """)
    
    # Bokeh
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Librería 4: Bokeh</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles"):
        st.subheader(DESCRIPCION)
        st.write("""
        Bokeh es una librería de visualización interactiva centrada en la web que se enfoca en proporcionar elegantes 
        gráficos interactivos para aplicaciones web y dashboards. Utiliza HTML5 Canvas y WebGL para renderizar gráficos 
        de alto rendimiento directamente en el navegador.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Visualizaciones interactivas de alto rendimiento.
        - Excelente para grandes conjuntos de datos gracias a su renderizado eficiente.
        - Capacidad para crear aplicaciones web completas con su servidor integrado.
        - Arquitectura modular que permite personalizaciones avanzadas.
        - Buena integración con ecosistemas de datos como Pandas y NumPy.
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Sintaxis más compleja que otras librerías interactivas como Plotly.
        - Documentación menos completa y accesible que Matplotlib o Plotly.
        - Menos tipos de gráficos predefinidos que otras librerías.
        - Curva de aprendizaje pronunciada para funcionalidades avanzadas.
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Visualización de grandes conjuntos de datos que requieren interactividad.
        - Aplicaciones web de análisis de datos personalizadas.
        - Gráficos interactivos que necesitan alto rendimiento.
        - Dashboards que requieren actualizaciones en tiempo real.
        """)
    
    # GeoPandas
    st.markdown("<h2 style='font-size: 24px; color: #1a365d;'>Librería 5: GeoPandas</h2>", unsafe_allow_html=True)
    with st.expander("Ver detalles"):
        st.subheader(DESCRIPCION)
        st.write("""
        GeoPandas es una extensión de Pandas que facilita el trabajo con datos geoespaciales en Python. Combina las 
        capacidades de Pandas con herramientas para el análisis geoespacial, permitiendo operaciones espaciales en 
        tipos de datos geométricos.
        """)
        
        st.subheader(VENTAJAS)
        st.markdown("""
        - Integra perfectamente análisis de datos y operaciones geoespaciales.
        - Extiende DataFrames de Pandas con tipos de datos geométricos.
        - Simplifica la creación de mapas y visualizaciones geoespaciales.
        - Soporte para diferentes sistemas de coordenadas y proyecciones.
        - Capacidad para realizar operaciones espaciales (intersección, unión, etc.).
        """)
        
        st.subheader(DESVENTAJAS)
        st.markdown("""
        - Enfocado exclusivamente en datos geoespaciales.
        - Requiere dependencias adicionales que pueden ser complicadas de instalar.
        - Curva de aprendizaje pronunciada para usuarios sin experiencia en GIS.
        - Rendimiento limitado con conjuntos de datos geoespaciales muy grandes.
        """)
        
        st.subheader(CASOSUSO)
        st.markdown("""
        - Análisis y visualización de datos geoespaciales.
        - Creación de mapas temáticos y coropléticos.
        - Proyectos que combinan análisis de datos tradicionales con componentes geográficos.
        - Visualización de datos estadísticos por regiones o áreas geográficas.
        """)
    
    # Justificación de la selección
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Justificación de la selección de librerías</h2>", unsafe_allow_html=True)
    st.write("""
    Para este caso de estudio sobre métricas de proyectos de software, hemos seleccionado tres librerías principales: 
    Matplotlib, Seaborn y Plotly. Cada una de estas librerías se utilizará para diferentes aspectos del análisis, 
    aprovechando sus fortalezas específicas.
    """)
    
    st.subheader("Objetivo 1: Análisis de tendencias a lo largo del tiempo")
    st.write("""
    Para analizar cómo evolucionan las métricas a lo largo de los sprints, utilizaremos **Matplotlib** debido a su 
    precisión y control detallado sobre los gráficos de líneas. Esto nos permitirá visualizar claramente las tendencias 
    temporales en métricas como horas de desarrollo, errores detectados y retrasos en las entregas.
    """)
    
    st.subheader("Objetivo 2: Comparación entre equipos")
    st.write("""
    Para comparar el rendimiento entre diferentes equipos, **Seaborn** es la elección ideal debido a sus capacidades 
    estadísticas y su facilidad para crear gráficos comparativos como boxplots y barplots. Su integración con Pandas 
    facilitará el análisis agrupado por equipos.
    """)
    
    st.subheader("Objetivo 3: Análisis de correlaciones")
    st.write("""
    Para explorar las relaciones entre diferentes métricas (como la correlación entre horas de prueba y errores detectados), 
    utilizaremos **Plotly** debido a sus capacidades interactivas que permiten explorar en detalle los datos y descubrir 
    patrones complejos a través de gráficos de dispersión y mapas de calor interactivos.
    """)
    
    st.subheader("Objetivo 4: Visualizaciones complejas y dashboards")
    st.write("""
    Para crear visualizaciones más complejas que combinen múltiples métricas y permitan una exploración interactiva 
    profunda, utilizaremos **Plotly**. Su capacidad para manejar grandes conjuntos de datos y crear interfaces interactivas 
    complejas lo hace ideal para dashboards detallados de rendimiento de proyectos.
    """)
    
    # Conclusión
    st.markdown("<h2 style='font-size: 32px; color: #1a365d;'>Conclusión</h2>", unsafe_allow_html=True)
    st.write("""
    La combinación de estas librerías de visualización nos permite abordar de manera integral el análisis de métricas 
    de proyectos de software. Cada librería aporta sus fortalezas específicas:
    
    - **Matplotlib** proporciona control preciso para visualizaciones de tendencias temporales.
    - **Seaborn** facilita la comparación estadística entre equipos con visualizaciones elegantes.
    - **Plotly** ofrece interactividad para explorar correlaciones y patrones complejos, además de permitir crear dashboards 
      interactivos para un análisis integral del rendimiento.
    
    Esta aproximación multi-librería nos permite aprovechar lo mejor de cada herramienta para obtener insights más 
    completos y valiosos sobre el rendimiento de los equipos de desarrollo y la eficiencia de los procesos.
    """)
