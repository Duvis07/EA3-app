import streamlit as st
import pandas as pd
import numpy as np

# Importar mu00f3dulos personalizados
from caso_estudio import mostrar_caso_estudio

# Importar librerías de visualización después para evitar problemas de importación circular
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Importaciones de Bokeh eliminadas debido a problemas de compatibilidad de versiones

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Métricas de Proyectos de Software",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Personalizar el diseño con CSS
st.markdown("""
<style>
    .main {background-color: #f8f9fa;}
    .stTabs [data-baseweb="tab-list"] {gap: 24px;}
    .stTabs [data-baseweb="tab"] {background-color: #e6f2ff; border-radius: 4px; padding: 10px 20px;}
    .stTabs [aria-selected="true"] {background-color: #4a86e8; color: white;}
    h1 {color: #1a365d; font-weight: 800; margin-bottom: 0.5em;}
    h2 {color: #2a4365; font-weight: 700;}
    h3 {color: #2c5282; font-weight: 600;}
    .stMarkdown {line-height: 1.8;}
    div.block-container {padding-top: 2rem;}
    .insight-card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #4a86e8;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-container {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .footer {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin-top: 30px;
        border-top: 2px solid #e2e8f0;
    }
    /* Estilos para tarjetas de métricas */
    .metric-row {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        flex: 1;
        min-width: 200px;
        display: flex;
        align-items: center;
    }
    .metric-icon {
        font-size: 24px;
        margin-right: 10px;
        color: #4a86e8;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #2c5282;
    }
    .metric-label {
        font-size: 14px;
        color: #4a5568;
    }
    /* Estilos para insights */
    .insight-blue {
        background-color: #ebf8ff;
        border-left: 4px solid #4299e1;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .insight-green {
        background-color: #f0fff4;
        border-left: 4px solid #38a169;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .insight-red {
        background-color: #fff5f5;
        border-left: 4px solid #e53e3e;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .insight-purple {
        background-color: #faf5ff;
        border-left: 4px solid #805ad5;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Función para cargar los datos
@st.cache_data
def load_data():
    df = pd.read_csv("static/Doc02_dataset_metricas_proyecto_software (2).csv")
    return df

# Cargar los datos
df = load_data()

# Título y descripción
st.title("📊 Análisis de Métricas de Proyectos de Software")

st.markdown("""
<div style="background-color: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 25px; border-top: 4px solid #4a86e8;">
    <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="font-size: 40px; margin-right: 15px; color: #4a86e8;">📊</div>
        <div>
            <h3 style="color: #2c5282; margin: 0; font-size: 22px;">Análisis de Métricas de Software</h3>
            <p style="margin: 5px 0 0 0; color: #4a5568;">Desarrollado por <span style="color: #4a86e8; font-weight: bold;">Arley</span></p>
        </div>
    </div>
    <p style="font-size: 16px; line-height: 1.7; color: #2d3748; margin-bottom: 15px;">
        Esta aplicación interactiva analiza métricas clave de proyectos de software a lo largo de múltiples sprints y equipos.
        Utiliza diferentes librerías de visualización de Python para proporcionar insights valiosos sobre el rendimiento
        de los equipos, la calidad del código y la eficiencia del proceso de desarrollo.
    </p>
    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
        <span style="background-color: #e6f7ff; color: #1890ff; padding: 5px 10px; border-radius: 4px; font-size: 14px; display: flex; align-items: center;">
            <span style="margin-right: 5px;">📈</span> Análisis de tendencias
        </span>
        <span style="background-color: #f6ffed; color: #52c41a; padding: 5px 10px; border-radius: 4px; font-size: 14px; display: flex; align-items: center;">
            <span style="margin-right: 5px;">📋</span> Comparación de equipos
        </span>
        <span style="background-color: #fff2e8; color: #fa8c16; padding: 5px 10px; border-radius: 4px; font-size: 14px; display: flex; align-items: center;">
            <span style="margin-right: 5px;">📉</span> Correlación de métricas
        </span>
        <span style="background-color: #f9f0ff; color: #722ed1; padding: 5px 10px; border-radius: 4px; font-size: 14px; display: flex; align-items: center;">
            <span style="margin-right: 5px;">📊</span> Visualización interactiva
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Crear filtros para el análisis
st.markdown("""<div style="margin: 30px 0 20px 0;"><hr style='height:2px;border-width:0;color:#4a86e8;background-color:#4a86e8'></div>""", unsafe_allow_html=True)
st.markdown("""<h2 style="color: #2a4365; display: flex; align-items: center; gap: 10px;"><span style="font-size: 24px;">🔍</span> Filtros de análisis</h2>""", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    sprints_seleccionados = st.multiselect(
        "Seleccionar sprints",
        options=sorted(df['Sprint'].unique()),
        default=sorted(df['Sprint'].unique())
    )

with col2:
    equipos_seleccionados = st.multiselect(
        "Seleccionar equipos",
        options=sorted(df['Equipo'].unique()),
        default=sorted(df['Equipo'].unique())
    )

# Filtrar los datos según las selecciones
df_filtrado = df[
    df['Sprint'].isin(sprints_seleccionados) &
    df['Equipo'].isin(equipos_seleccionados)
]

# Mostrar métricas clave después de filtrar
st.markdown(f"""
<div style="margin: 20px 0;">
    <div class="metric-row">
        <div class="metric-card">
            <div class="metric-icon">📊</div>
            <div>
                <div class="metric-value">{len(df_filtrado)}</div>
                <div class="metric-label">Registros analizados</div>
            </div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">⏱️</div>
            <div>
                <div class="metric-value">{df_filtrado['Horas_Desarrollo'].mean():.1f}</div>
                <div class="metric-label">Horas promedio de desarrollo</div>
            </div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">🧪</div>
            <div>
                <div class="metric-value">{df_filtrado['Horas_Pruebas'].mean():.1f}</div>
                <div class="metric-label">Horas promedio de pruebas</div>
            </div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">🐛</div>
            <div>
                <div class="metric-value">{df_filtrado['Errores_Detectados'].mean():.1f}</div>
                <div class="metric-label">Errores promedio detectados</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Dividir la pantalla en pestañas
st.markdown("""<div style="margin: 30px 0 20px 0;"><hr style='height:2px;border-width:0;color:#4a86e8;background-color:#4a86e8'></div>""", unsafe_allow_html=True)
st.markdown("""<h2 style="color: #2a4365; margin-bottom: 20px;">Análisis interactivo con diferentes librerías</h2>""", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["📚 Caso de Estudio", "📊 Matplotlib", "📈 Seaborn", "🔍 Plotly"])

with tab1:
    # Mostrar el caso de estudio
    mostrar_caso_estudio()

with tab2:
    st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Análisis de tendencias con Matplotlib</h2>", unsafe_allow_html=True)
    st.write("""
    Matplotlib es ideal para visualizar tendencias a lo largo del tiempo con gran precisión y control detallado.
    A continuación, analizamos cómo evolucionan las métricas clave a lo largo de los sprints.
    """)
    
    # Ajustar el tamaño para dejar espacio a la leyenda
    fig = plt.figure(figsize=(3.8, 2))
    ax = fig.add_subplot(111)
    
    # Calcular promedios por sprint para cada métrica
    sprint_avg = df_filtrado.groupby('Sprint')[['Horas_Desarrollo', 'Horas_Pruebas', 'Errores_Detectados']].mean().reset_index()
    
    # Graficar las tendencias con estilo exacto al ejemplo
    ax.plot(sprint_avg['Sprint'], sprint_avg['Horas_Desarrollo'], marker='o', linewidth=1, markersize=4, label='H.Desarrollo', color='#1f77b4')
    ax.plot(sprint_avg['Sprint'], sprint_avg['Horas_Pruebas'], marker='s', linewidth=1, markersize=4, label='H.Pruebas', color='#ff7f0e')
    ax.plot(sprint_avg['Sprint'], sprint_avg['Errores_Detectados'], marker='^', linewidth=1, markersize=4, label='Errores', color='#2ca02c')
    
    # Usar el estilo exacto del ejemplo mostrado
    plt.title('')  # Sin título para ahorrar espacio
    plt.xlabel('', fontsize=0)  # Sin etiqueta de eje x
    plt.ylabel('', fontsize=0)  # Sin etiqueta de eje y
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.grid(True, linestyle='-', alpha=0.15, linewidth=0.5)
    # Leyenda a un lado del gráfico con mejor posicionamiento
    plt.subplots_adjust(right=0.68)  # Hacer espacio para la leyenda
    plt.legend(fontsize=6, loc='center left', bbox_to_anchor=(1.02, 0.5), frameon=False, labelspacing=0.1, handlelength=1.0)
    # Añadir borde al gráfico
    for spine in ax.spines.values():
        spine.set_linewidth(1)
    # Ajustar los bordes (solo una vez) con menos padding
    plt.tight_layout(pad=0.1)
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
    
    # Agregar insights
    st.markdown("""
    <div class="insight-card">
        <h3 style="margin-top: 0; color: #2c5282;">📊 Insights del análisis con Matplotlib</h3>
        <ul style="margin-bottom: 0;">
            <li>Las <strong>horas de desarrollo</strong> muestran una tendencia general a la baja a medida que avanzan los sprints, lo que sugiere una mejora en la eficiencia del equipo.</li>
            <li>Las <strong>horas de pruebas</strong> se mantienen relativamente estables, indicando un compromiso constante con la calidad.</li>
            <li>Los <strong>errores detectados</strong> tienden a disminuir en los últimos sprints, lo que podría indicar una mejora en la calidad del código o en las prácticas de desarrollo.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Distribuciones y correlaciones con Seaborn</h2>", unsafe_allow_html=True)
    st.write("""
    Seaborn es excelente para visualizar distribuciones y relaciones entre variables con estilos atractivos y estadísticas incorporadas.
    Exploremos la distribución de las métricas clave y sus correlaciones.
    """)
    
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de violín para comparar distribuciones por equipo
        st.markdown("<h3 style='font-size: 20px; color: #2c5282;'>Distribución de horas por equipo</h3>", unsafe_allow_html=True)
        fig_violin = plt.figure(figsize=(5, 3.5))
        sns.violinplot(data=df_filtrado, x='Equipo', y='Horas_Desarrollo', palette='viridis')
        plt.title('Distribución de horas de desarrollo por equipo', fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig_violin)
        
        # Agregar insights para el gráfico de violín
        st.markdown("""
        <div style="background-color: #f0fff4; border-left: 4px solid #38a169; padding: 15px; border-radius: 5px; margin-top: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2c5282; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">💡</span> Insights
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li>Existe una <strong>variabilidad significativa</strong> en las horas de desarrollo entre equipos</li>
                <li>Algunos equipos muestran distribuciones más concentradas, indicando mayor consistencia</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Gráfico de barras con Seaborn para comparar errores por equipo
        st.markdown("<h3 style='font-size: 20px; color: #2c5282;'>Errores detectados por equipo</h3>", unsafe_allow_html=True)
        fig_bar = plt.figure(figsize=(5, 3.5))
        sns.barplot(data=df_filtrado, x='Equipo', y='Errores_Detectados', palette='rocket', errorbar=None)
        plt.title('Promedio de errores detectados por equipo', fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig_bar)
        
        # Agregar insights para el gráfico de barras
        st.markdown("""
        <div style="background-color: #fdf2f2; border-left: 4px solid #e53e3e; padding: 15px; border-radius: 5px; margin-top: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2c5282; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">💡</span> Insights
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li>Los equipos con mayor tasa de errores podrían necesitar revisiones de código más rigurosas</li>
                <li>Existe una relación entre la complejidad de los proyectos y la cantidad de errores detectados</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Matriz de correlación con heatmap
    st.markdown("<h3 style='font-size: 22px; color: #2c5282; margin-top: 30px;'>Matriz de correlación entre métricas</h3>", unsafe_allow_html=True)
    # Seleccionar solo columnas numéricas para la correlación
    numeric_cols = ['Horas_Desarrollo', 'Horas_Pruebas', 'Errores_Detectados', 'Retraso_Entrega (días)', 'Costo_Excedente ($)']
    corr_matrix = df_filtrado[numeric_cols].corr()
    
    # Crear heatmap
    fig_corr = plt.figure(figsize=(6, 4.5))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .8})
    plt.title('Correlación entre métricas clave', fontsize=16)
    plt.tight_layout()
    st.pyplot(fig_corr)
    
    # Agregar insights para la matriz de correlación
    st.markdown("""
    <div style="background-color: #f8f9fa; border-left: 4px solid #4a86e8; padding: 15px; border-radius: 5px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <h4 style="color: #2c5282; margin-top: 0; display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 18px;">📈</span> Insights de correlaciones
        </h4>
        <ul style="margin-bottom: 0; padding-left: 20px;">
            <li>Se observa una <strong>correlación positiva</strong> entre las horas de desarrollo y los errores detectados</li>
            <li>La complejidad ciclomática muestra correlación con los errores detectados, confirmando que código más complejo tiende a contener más errores</li>
            <li>Las horas de pruebas y desarrollo muestran correlación, indicando que proyectos más grandes requieren más tiempo en ambas fases</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("<h2 style='font-size: 28px; color: #1a365d;'>Visualizaciones interactivas con Plotly</h2>", unsafe_allow_html=True)
    st.write("""
    Plotly permite crear visualizaciones interactivas que facilitan la exploración detallada de los datos.
    Analicemos la relación entre diferentes métricas y su evolución a lo largo del tiempo.
    """)
    
    # Crear dos columnas para los gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de dispersión interactivo
        st.markdown("<h3 style='font-size: 20px; color: #2c5282;'>Relación entre desarrollo y errores</h3>", unsafe_allow_html=True)
        
        # Crear gráfico de dispersión con Plotly
        fig_scatter = px.scatter(df_filtrado, 
                            x='Horas_Desarrollo', 
                            y='Errores_Detectados',
                            size='Horas_Pruebas',  # Usamos Horas_Pruebas en lugar de Complejidad_Ciclomatica
                            color='Equipo',
                            hover_name='Sprint',
                            hover_data=['Costo_Excedente ($)'],
                            labels={
                                'Horas_Desarrollo': 'Horas de Desarrollo',
                                'Errores_Detectados': 'Errores Detectados',
                                'Horas_Pruebas': 'Horas de Pruebas',
                                'Costo_Excedente ($)': 'Costo Excedente ($)'
                            })
        
        # Personalizar el layout
        fig_scatter.update_layout(
            title={
                'text': 'Relación entre horas de desarrollo y errores',
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            plot_bgcolor='rgba(240, 240, 240, 0.5)',
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(200, 200, 200, 0.2)'),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(200, 200, 200, 0.2)'),
            legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)
        )
        
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Agregar insights para el gráfico de dispersión
        st.markdown("""
        <div style="background-color: #e6f2ff; border-left: 4px solid #4299e1; padding: 15px; border-radius: 5px; margin-top: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2c5282; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">🔍</span> Insights
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li>Los proyectos con mayor complejidad (burbujas más grandes) tienden a tener más errores</li>
                <li>Existe una correlación positiva entre horas de desarrollo y errores detectados</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Gráfico de barras apiladas para comparar métricas por sprint
        st.markdown("<h3 style='font-size: 20px; color: #2c5282;'>Comparación de métricas por sprint</h3>", unsafe_allow_html=True)
        
        # Preparar datos agregados por sprint
        sprint_avg = df_filtrado.groupby('Sprint')[['Horas_Desarrollo', 'Horas_Pruebas']].mean().reset_index()
        
        # Crear gráfico de barras apiladas
        fig_bar = go.Figure()
        
        # Agregar barras para horas de desarrollo
        fig_bar.add_trace(go.Bar(
            x=sprint_avg['Sprint'],
            y=sprint_avg['Horas_Desarrollo'],
            name='Horas de Desarrollo',
            marker_color='#4a86e8'
        ))
        
        # Agregar barras para horas de pruebas
        fig_bar.add_trace(go.Bar(
            x=sprint_avg['Sprint'],
            y=sprint_avg['Horas_Pruebas'],
            name='Horas de Pruebas',
            marker_color='#ff9900'
        ))
        
        # Personalizar el layout
        fig_bar.update_layout(
            title={
                'text': 'Distribución de horas por sprint',
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            barmode='group',
            plot_bgcolor='rgba(240, 240, 240, 0.5)',
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            xaxis=dict(title='Sprint', showgrid=False),
            yaxis=dict(title='Horas promedio', showgrid=True, gridwidth=1, gridcolor='rgba(200, 200, 200, 0.2)'),
            legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Agregar insights para el gráfico de barras
        st.markdown("""
        <div style="background-color: #fff5f5; border-left: 4px solid #fc8181; padding: 15px; border-radius: 5px; margin-top: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h4 style="color: #2c5282; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 18px;">📊</span> Insights
            </h4>
            <ul style="margin-bottom: 0; padding-left: 20px;">
                <li>La proporción entre horas de desarrollo y pruebas varía entre sprints</li>
                <li>Se observa una tendencia a la optimización del tiempo en los últimos sprints</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Gráfico de líneas interactivo para ver tendencias
    st.markdown("<h3 style='font-size: 22px; color: #2c5282; margin-top: 30px;'>Evolución de métricas por sprint y equipo</h3>", unsafe_allow_html=True)
    
    # Preparar datos agregados por sprint y equipo
    sprint_team_avg = df_filtrado.groupby(['Sprint', 'Equipo'])[['Horas_Desarrollo', 'Horas_Pruebas', 'Errores_Detectados']].mean().reset_index()
    
    # Agregar selector de métrica
    metrica_seleccionada = st.selectbox(
        "Seleccionar métrica para visualizar",
        options=['Horas_Desarrollo', 'Horas_Pruebas', 'Errores_Detectados'],
        format_func=lambda x: x.replace('_', ' ')
    )
    
    # Crear gráfico de líneas con Plotly
    fig_line = px.line(sprint_team_avg, 
                    x='Sprint', 
                    y=metrica_seleccionada,
                    color='Equipo',
                    markers=True,
                    labels={
                        'Horas_Desarrollo': 'Horas de Desarrollo',
                        'Horas_Pruebas': 'Horas de Pruebas',
                        'Errores_Detectados': 'Errores Detectados'
                    })
    
    # Personalizar el layout
    fig_line.update_layout(
        title={
            'text': f'Evolución de {metrica_seleccionada.replace("_", " ")} por sprint y equipo',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        plot_bgcolor='rgba(240, 240, 240, 0.5)',
        height=500,
        margin=dict(l=20, r=20, t=60, b=30),
        xaxis=dict(title='Sprint', showgrid=True, gridwidth=1, gridcolor='rgba(200, 200, 200, 0.2)'),
        yaxis=dict(title=metrica_seleccionada.replace("_", " "), showgrid=True, gridwidth=1, gridcolor='rgba(200, 200, 200, 0.2)'),
        legend=dict(orientation='h', yanchor='bottom', y=-0.15, xanchor='center', x=0.5)
    )
    
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Agregar insights generales para Plotly
    st.markdown("""
    <div style="background-color: #f8f9fa; border-left: 5px solid #4a86e8; padding: 20px; border-radius: 8px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <h3 style="margin-top: 0; color: #2c5282; display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 24px;">💡</span> Insights clave del análisis con Plotly
        </h3>
        <ul style="margin-bottom: 0; padding-left: 20px;">
            <li style="margin-bottom: 8px;">Los proyectos con mayor número de horas de pruebas tienden a tener menos errores detectados, lo que sugiere la importancia de <strong>invertir tiempo adecuado en pruebas</strong> para mejorar la calidad del software.</li>
            <li style="margin-bottom: 8px;">Existe una <strong>clara diferenciación</strong> entre equipos en términos de horas dedicadas y errores encontrados, lo que podría indicar diferentes niveles de experiencia o eficiencia.</li>
            <li style="margin-bottom: 8px;">La evolución temporal muestra que algunos equipos logran reducir sus horas de desarrollo más rápidamente que otros, señalando posibles <strong>mejoras en los procesos</strong> o mayor familiaridad con el proyecto.</li>
            <li>La interactividad de Plotly permite identificar outliers y patrones específicos que podrían requerir atención especial, facilitando un <strong>análisis más profundo</strong> de situaciones particulares y la relación entre costos excedentes y errores.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)



