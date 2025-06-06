import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    from caso_estudio import mostrar_caso_estudio
except ImportError:
    mostrar_caso_estudio = None

st.set_page_config(
    page_title="Análisis de Ventas - TechNova Retail",
    page_icon="📊",
    layout="wide"
)

# --- CSS para diseño moderno tipo "app de turismo" ---
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
</style>
""", unsafe_allow_html=True)

st.title("📊 Análisis de Ventas - TechNova Retail")

# --- Tabs para caso de estudio y visualizaciones ---
tabs = st.tabs(["Caso de estudio", "Visualizaciones de ventas"])

with tabs[0]:
    if mostrar_caso_estudio:
        st.markdown("""
        <div class='insight-card'>
        <h2>Caso de Estudio</h2>
        <p>Explora el caso de estudio y descubre cómo se puede aplicar el análisis de ventas en un escenario real.</p>
        </div>
        """, unsafe_allow_html=True)
        mostrar_caso_estudio()
    else:
        st.subheader("Caso de estudio no disponible")
        st.write("No se encontró el módulo 'caso_estudio.py'.")

with tabs[1]:
    st.markdown("""
    <div class='insight-card'>
    <h2>Análisis de Ventas de TechNova Retail</h2>
    <p>Explora los datos de ventas y observa tendencias clave para la toma de decisiones estratégicas.</p>
    </div>
    """, unsafe_allow_html=True)

    import unicodedata
    @st.cache_data
    def load_data():
        df = pd.read_excel("static/Ventas_Minoristas.xlsx")
        # Renombrar columnas para quitar espacios y caracteres especiales
        df = df.rename(columns={
            "ID_cliente": "id_cliente",
            "Nombre_producto": "nombre_producto",
            "Cantidad": "cantidad",
            "Precio_unitario(USD)": "precio_unitario_usd",
            "Fecha": "fecha",
            "categoria": "categoria",
            "pais": "pais",
            "ciudad": "ciudad",
            "metodo_pago": "metodo_pago",
            "edad_cliente": "edad_cliente",
            "genero_cliente": "genero_cliente",
            "calificaci�n_satisfaccion": "calificacion_satisfaccion"
        })
        # Limpiar strings: minúsculas, sin tildes, sin espacios extras
        def limpiar_texto(x):
            if isinstance(x, str):
                x = x.strip().lower()
                x = unicodedata.normalize('NFKD', x).encode('ascii', errors='ignore').decode('utf-8')
            return x
        for col in ["categoria", "pais", "ciudad", "metodo_pago", "genero_cliente", "nombre_producto"]:
            df[col] = df[col].apply(limpiar_texto)
        # Corregir tipos numéricos
        df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
        df["precio_unitario_usd"] = pd.to_numeric(df["precio_unitario_usd"], errors="coerce")
        df["edad_cliente"] = pd.to_numeric(df["edad_cliente"], errors="coerce")
        if "calificacion_satisfaccion" in df.columns:
            df["calificacion_satisfaccion"] = pd.to_numeric(df["calificacion_satisfaccion"], errors="coerce")
        # Crear columna de ventas
        df["ventas"] = df["cantidad"] * df["precio_unitario_usd"]
        # Quitar filas con datos faltantes críticos (solo columnas que existen)
        columnas_criticas = [col for col in ["cantidad", "precio_unitario_usd", "ventas", "categoria", "fecha"] if col in df.columns]
        if columnas_criticas:
            df = df.dropna(subset=columnas_criticas)
        # Opcional: filtrar ventas no positivas
        df = df[df["ventas"] > 0]
        return df

    df = load_data()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3>Ventas Totales por Categoría de Producto</h3>", unsafe_allow_html=True)
        if 'categoria' in df.columns and 'ventas' in df.columns:
            ventas_categoria = df.groupby('categoria')['ventas'].sum().sort_values(ascending=False)
            import matplotlib.ticker as mticker
            import seaborn as sns
            ventas_categoria = ventas_categoria.sort_values(ascending=True)
            fig1, ax1 = plt.subplots(figsize=(8, 4))
            sns.set_style("whitegrid")
            bars = ax1.barh(
                ventas_categoria.index, ventas_categoria.values,
                color=sns.color_palette("crest", len(ventas_categoria)),
                edgecolor="black", linewidth=1.5, height=0.7
            )
            ax1.set_facecolor("#f8f9fa")
            ax1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(",", ".")))
            ax1.set_xlabel("Ventas Totales", fontsize=13, fontweight="bold")
            ax1.set_ylabel("Categoría de Producto", fontsize=13, fontweight="bold")
            for i, v in enumerate(ventas_categoria.values):
                ax1.text(v + max(ventas_categoria.values)*0.01, i, f'${v:,.0f}'.replace(",", "."),
                         color='black', va='center', fontweight='bold', fontsize=13,
                         bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.25', alpha=0.85))
            sns.despine(left=True, bottom=True)
            fig1.tight_layout()
            st.pyplot(fig1)
            # Insight profesional para ventas por categoría
            if len(ventas_categoria) > 1:
                lider = ventas_categoria.index[-1]
                monto_lider = ventas_categoria.values[-1]
                segunda = ventas_categoria.index[-2]
                monto_segunda = ventas_categoria.values[-2]
                diff = monto_lider - monto_segunda
                st.markdown(f"""
                <div class='insight-card'>
                <h3>Insight: Ventas Totales por Categoría</h3>
                <p>La categoría líder en ventas es <b>{lider.capitalize()}</b> con <b>${monto_lider:,.2f}</b>, superando a <b>{segunda.capitalize()}</b> por <b>${diff:,.2f}</b>. Esto indica una clara preferencia del mercado por esta categoría.</p>
                </div>
                """, unsafe_allow_html=True)
            elif len(ventas_categoria) == 1:
                lider = ventas_categoria.index[0]
                monto_lider = ventas_categoria.values[0]
                st.markdown(f"""
                <div class='insight-card'>
                <h3>Insight: Ventas Totales por Categoría</h3>
                <p>Solo existe una categoría registrada: <b>{lider.capitalize()}</b> con ventas totales de <b>${monto_lider:,.2f}</b>.</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No se encontraron las columnas 'categoria' y 'ventas' en el archivo.")

        st.markdown("<h3>Distribución de Ventas</h3>", unsafe_allow_html=True)
        if 'ventas' in df.columns:
            import numpy as np
            from matplotlib import cm
            fig2, ax2 = plt.subplots(figsize=(9, 5))
            sns.set_style("whitegrid")
            # Color degradado para las barras
            cmap = cm.get_cmap('Blues')
            n_bins = 20
            n, bins, patches = ax2.hist(
                df['ventas'].dropna(), bins=n_bins, color=cmap(0.6), alpha=0.85, edgecolor="white", linewidth=2, rwidth=0.92
            )
            for i, patch in enumerate(patches):
                color = cmap(0.3 + 0.7*i/len(patches))
                patch.set_facecolor(color)
            # Línea KDE profesional
            sns.kdeplot(df['ventas'].dropna(), ax=ax2, color="#2c5282", linewidth=3, fill=False, alpha=0.7)
            ax2.set_xlabel("Ventas", fontsize=15, fontweight="bold")
            ax2.set_ylabel("Frecuencia", fontsize=15, fontweight="bold")
            ax2.set_facecolor("#f8f9fa")
            ax2.grid(True, linestyle='--', alpha=0.2)
            # Etiquetas sobre todas las barras
            for rect, freq in zip(patches, n):
                if freq > 0:
                    ax2.text(rect.get_x() + rect.get_width()/2, freq + 2, int(freq), ha='center', va='bottom', fontweight='bold', fontsize=12, color='#2c5282', bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.13', alpha=0.8))
            sns.despine(left=True, bottom=True)
            fig2.tight_layout()
            st.pyplot(fig2)
            # Insight profesional para el histograma
            ventas_min = df['ventas'].min()
            ventas_max = df['ventas'].max()
            ventas_mediana = df['ventas'].median()
            ventas_p25 = df['ventas'].quantile(0.25)
            ventas_p75 = df['ventas'].quantile(0.75)
            st.markdown(f"""
            <div class='insight-card'>
            <h3>Insight: Distribución de Ventas</h3>
            <p>La mayoría de las ventas ({(df['ventas'] <= ventas_p75).mean()*100:.1f}%) están por debajo de <b>${ventas_p75:,.2f}</b>. El 50% central de las ventas se encuentra entre <b>${ventas_p25:,.2f}</b> y <b>${ventas_p75:,.2f}</b>. El valor mediano es <b>${ventas_mediana:,.2f}</b>. El rango completo va de <b>${ventas_min:,.2f}</b> a <b>${ventas_max:,.2f}</b>.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("No se encontró la columna 'ventas' en el archivo.")

    with col2:
        st.markdown("<h3>Evolución de Ventas en el Tiempo</h3>", unsafe_allow_html=True)
        if 'fecha' in df.columns and 'ventas' in df.columns:
            import matplotlib.dates as mdates
            ventas_tiempo = df.groupby('fecha')['ventas'].sum().sort_index()
            rolling = ventas_tiempo.rolling(window=7, min_periods=1).mean()
            fig3, ax3 = plt.subplots(figsize=(9, 4))
            sns.set_style("whitegrid")
            ax3.plot(ventas_tiempo.index, ventas_tiempo.values, color="#2c5282", linewidth=1.5, label="Ventas diarias")
            ax3.plot(rolling.index, rolling.values, color="#4a86e8", linewidth=2.5, linestyle="--", label="Promedio móvil (7 días)")
            ax3.set_xlabel("Fecha", fontsize=13, fontweight="bold")
            ax3.set_ylabel("Ventas Totales", fontsize=13, fontweight="bold")
            ax3.xaxis.set_major_locator(mdates.AutoDateLocator())
            ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
            ax3.grid(True, linestyle='--', alpha=0.3)
            # Pico máximo destacado
            max_idx = ventas_tiempo.idxmax()
            max_val = ventas_tiempo.max()
            ax3.scatter([max_idx], [max_val], color="crimson", s=100, zorder=5)
            ax3.annotate(f"Máximo: ${max_val:,.0f}".replace(",", "."),
                         xy=(max_idx, max_val), xytext=(30, -40),
                         textcoords="offset points", arrowprops=dict(arrowstyle="->", color="crimson", lw=2),
                         fontsize=12, color="crimson", fontweight="bold", bbox=dict(facecolor='white', alpha=0.9, boxstyle='round,pad=0.2'))
            fig3.autofmt_xdate()
            sns.despine(left=True, bottom=True)
            fig3.tight_layout()
            ax3.legend()
            st.pyplot(fig3)
            st.markdown("""
            <div class='insight-card'>
            <h3>Insight: Evolución de Ventas</h3>
            <p>Las ventas han aumentado un {:.2f}% desde {} hasta {}.</p>
            </div>
            """.format((ventas_tiempo.values[-1] - ventas_tiempo.values[0]) / ventas_tiempo.values[0] * 100, ventas_tiempo.index[0], ventas_tiempo.index[-1]), unsafe_allow_html=True)
        else:
            st.warning("No se encontraron las columnas 'fecha' y 'ventas' en el archivo.")

        st.markdown("<h3>Distribución de Ventas por Categoría</h3>", unsafe_allow_html=True)
        if 'categoria' in df.columns and 'ventas' in df.columns:
            fig4, ax4 = plt.subplots(figsize=(9, 5))
            sns.set_style("whitegrid")
            # Dispersión profesional: puntos grandes, alpha, color por categoría, jitter, líneas de mediana
            sns.stripplot(x='categoria', y='ventas', data=df, jitter=0.28, size=9, alpha=0.45, ax=ax4,
                         palette="crest", edgecolor='k', linewidth=0.8)
            # Línea de mediana por categoría
            cats = df['categoria'].unique()
            for i, cat in enumerate(cats):
                mediana = df[df['categoria'] == cat]['ventas'].median()
                ax4.hlines(mediana, i-0.25, i+0.25, colors='#2c5282', linestyles='--', linewidth=3, label=f"Mediana {cat}" if i==0 else "")
            ax4.set_xlabel("Categoría de Producto", fontsize=15, fontweight="bold")
            ax4.set_ylabel("Ventas", fontsize=15, fontweight="bold")
            ax4.set_facecolor("#f8f9fa")
            ax4.grid(True, linestyle='--', alpha=0.2)
            plt.xticks(rotation=28, ha='right', fontsize=13)
            plt.yticks(fontsize=13)
            sns.despine(left=True, bottom=True)
            fig4.tight_layout()
            st.pyplot(fig4)
            # Insight avanzado y comparativo para dispersión por categoría (ahora sí, justo debajo del gráfico de dispersión)
            dispersions = df.groupby('categoria')['ventas'].std().sort_values(ascending=False)
            rango = df.groupby('categoria')['ventas'].agg(lambda x: x.max()-x.min())
            top_disp_cat = dispersions.index[0]
            top_disp_val = dispersions.iloc[0]
            top_rango = rango[top_disp_cat]
            ejemplo_max = df[df['categoria'] == top_disp_cat]['ventas'].max()
            ejemplo_min = df[df['categoria'] == top_disp_cat]['ventas'].min()
            low_disp_cat = dispersions.index[-1]
            low_disp_val = dispersions.iloc[-1]
            low_rango = rango[low_disp_cat]
            ejemplo_max_low = df[df['categoria'] == low_disp_cat]['ventas'].max()
            ejemplo_min_low = df[df['categoria'] == low_disp_cat]['ventas'].min()
            interpretacion = (f"La alta dispersión en <b>{top_disp_cat.capitalize()}</b> puede indicar una oferta diversa y oportunidades para potenciar productos exitosos, pero también sugiere inconsistencia en ventas que debe analizarse. "
                              f"En contraste, <b>{low_disp_cat.capitalize()}</b> muestra ventas mucho más concentradas, lo que puede facilitar la predicción y planeación.")
            st.markdown(f"""
            <div class='insight-card'>
            <h3>Insight: Distribución de Ventas por Categoría</h3>
            <ul>
                <li><b>Mayor dispersión:</b> {top_disp_cat.capitalize()} (std: ${top_disp_val:,.2f}, rango: ${top_rango:,.2f}, de ${ejemplo_min:,.2f} a ${ejemplo_max:,.2f})</li>
                <li><b>Menor dispersión:</b> {low_disp_cat.capitalize()} (std: ${low_disp_val:,.2f}, rango: ${low_rango:,.2f}, de ${ejemplo_min_low:,.2f} a ${ejemplo_max_low:,.2f})</li>
            </ul>
            <p>{interpretacion}</p>
            </div>
            """, unsafe_allow_html=True)

