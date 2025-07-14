## Script de Conteo de Casos Únicos (casos_tratados.py)
Descripción
Este script procesa dos reportes exportados de Salesforce (Historial de Casos y Avances) para resolver un problema clave: un agente puede intervenir en el mismo caso y aparecer en ambos reportes.

La finalidad de este script es generar un conteo de casos únicos por agente, asegurando que cada caso se cuente una sola vez por persona, sin importar en cuántos reportes o cuántas veces aparezca.

####  Archivos de Entrada
El script requiere dos (2) archivos en formato CSV como argumentos de línea de comandos. 

historial_path: El reporte de "Historial de Casos" de Salesforce. Contiene cada modificación hecha a un caso.

avances_path: El reporte de "Avances" de Salesforce. Contiene los comentarios o progresos agregados a un caso.

#### Lógica del Proceso (Paso a Paso)
El script sigue una lógica de consolidación y elimina los duplicados en varios pasos para garantizar la precisión del conteo-

1. Carga y Limpieza: Se cargan los dos archivos CSV.

2. Del reporte de historial, se crea una lista de pares únicos (agente, caso).

3. Se repite el mismo proceso para el reporte de avances.

4. Consolidación: Se juntan las dos listas de interacciones en una sola gran tabla. En este punto, un mismo par **(agente, caso)** podría estar duplicado si el agente apareció en ambos reportes para el mismo caso.

5. Desduplicación Final : Sobre la gran tabla consolidada, se vuelven a eliminar duplicados. Esto asegura que si el AGENTE trabajó en el caso X y aparece tanto en el reporte de historial como en el de avances, la combinación ('AGENTE', 'X') se cuente una sola y única vez.

6. Finalmente, se agrupa esta lista definitiva por agente y se cuenta la cantidad de casos asociados a cada uno para obtener el resultado final.


Bash

python casos_tratados.py "ruta/al/historial.csv" "ruta/al/avances.csv"

--------


