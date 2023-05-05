import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

global archivo
archivo = False
def leer_archivos():
	# Elegimos el archivo deseado
	open_file = filedialog.askopenfilename(title='Abrir archivo', filetypes=(('Archivos de excel', '*.xlsx'),))
	
	# Chequeamos que se halla elegido un archivo
	if open_file:
		# Hacemos global al archivo, para poder acceder luego
		global archivo
		archivo = open_file
		
def renombrar_col(df):
    df.rename(columns=str.lower, inplace=True)
    df.columns = df.columns.str.replace(' ', '_')
    return df	

def ejecutar():
	if archivo:
		# Importamos las tablas
		df_arg = pd.read_excel(archivo,sheet_name=0)
		df_urg = pd.read_excel(archivo,sheet_name=1)
		df_chi = pd.read_excel(archivo,sheet_name=2)
		
		# Renombramos las columnas
		renombrar_col(df_arg)
		renombrar_col(df_urg)
		renombrar_col(df_chi)

		# Creamos la columna de cada pais
		df_arg['pais'] = 'Argentina'
		df_urg['pais'] = 'Uruguay'
		df_chi['pais'] = 'Chile'

		# Concatenamos los dataframes
		df = pd.concat([df_arg,df_chi,df_urg], ignore_index=True)
		
		# Creamos la columna venta
		df['venta'] =  [0 if plan == 'Prueba' else 1 for plan in df.plan_actual]
	
		# Eliminamos parte del origen crudo que trae errores
		df.origen_crudo = df['origen_crudo'].str.replace('undefined\|', '', regex=True)

		# Separamos la columna por '|'
		df_c= df.origen_crudo.str.split('|', expand=True)

		# Separamos la columna por '-' y le asignamos los nombres
		df_c[['tipo_anuncio', 'pais2', 'grupo_anuncio', 'mes_anuncio','otro']] = df_c[4].str.split('-', expand=True)

		# Asignamos nombre a las columnas faltantes
		df_c.rename(columns={0: 'source', 1: 'canal', 2: 'objetivo',3: 'audiencia', 4: 'crudo'}, inplace=True)

		# Verificamos si la columna source contiene la palabra "google"
		df_c.loc[df_c.source.str.contains('google'), 'source'] = 'google'

		# Agregamos la columna segment con la condición especificada
		df_c['segment'] = ['POS' if 'pos' in val else 'ERP' for val in df_c.tipo_anuncio]

		# Eliminamos las columnas innecesarias
		df_c = df_c.drop(['crudo','pais2','otro'], axis=1)

		# Concatenamos los registros inicial y desconcatenados
		df = pd.concat([df, df_c], axis=1)

		
		# Exportamos el archivo
		df.to_excel('Registro.xlsx', index=False)
		messagebox.showinfo("Finalizado", "El proceso se ha realizado con éxito.")
		
	else: messagebox.showwarning("Advertencia", "Debe cargar el archivo.")