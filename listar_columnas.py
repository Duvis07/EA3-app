import pandas as pd

def listar_columnas():
    try:
        df = pd.read_excel("static/Ventas_Minoristas.xlsx")
        print("\nColumnas del DataFrame:")
        print("-" * 50)
        for col in df.columns:
            print(f"- {col}")
        print("\nTipos de datos:")
        print("-" * 50)
        print(df.dtypes)
        return True
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return False

if __name__ == "__main__":
    listar_columnas()
