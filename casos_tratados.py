import pandas as pd
import sys

def count_unique_cases(historial, avances):
    col_agente_historial = 'Modificado por'
    col_caso_historial = 'Número del caso'
    col_fecha_historial = 'Fecha de modificación'

    col_agente_avances = 'Avance: Creado por'
    col_caso_avances = 'Caso'
    col_fecha_avances = 'Avance: Fecha de creación'

    try:
        df_historial = pd.read_csv(historial, sep=';', encoding='latin1')
        df_avances = pd.read_csv(avances, sep=';', encoding='latin1')

    except FileNotFoundError as e:
        print(f"Error: No se encontró el archivo {e.filename}.")
        return None 

    df_historial[col_fecha_historial] = pd.to_datetime(df_historial[col_fecha_historial], dayfirst=True, errors='coerce')
    df_avances[col_fecha_avances] = pd.to_datetime(df_avances[col_fecha_avances], dayfirst=True, errors='coerce')

    # Historial de Casos
    casos_historial = df_historial[[col_agente_historial, col_caso_historial]].drop_duplicates()
    print(casos_historial)
    casos_historial.columns = ['agente', 'caso']

    # Avances
    casos_avances = df_avances[[col_agente_avances, col_caso_avances]].drop_duplicates()
    casos_avances.columns = ['agente', 'caso']

    casos_totales_unicos = pd.concat([casos_historial, casos_avances]).drop_duplicates()
    casos_totales_unicos.dropna(inplace=True)


    print("Realizando el conteo final...")
    conteo_final = casos_totales_unicos.groupby('agente').size().reset_index(name='Casos Únicos Tratados')
    conteo_final = conteo_final.sort_values(by='agente')
    print(conteo_final["Casos Únicos Tratados"].sum(), "casos únicos tratados en total.")

    return conteo_final

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Ejemplo: python casos_tratados.py historial.csv avances.csv")
        sys.exit(1)

    historial_file = sys.argv[1]
    avances_file = sys.argv[2]
    
    resultado = count_unique_cases(historial_file, avances_file)
    resultado.to_clipboard(index=False, header=False, decimal=',')
    print(resultado)