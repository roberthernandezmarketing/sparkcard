import psycopg2
import pandas as pd

# DB connection
try:
    conn = psycopg2.connect(
        dbname="sparkcarddb",
        user="postgres",
        password="spk2025--",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("""
      -- SELECT * FROM card;
      SELECT * FROM vw_cards;
    """)

    resultados = cur.fetchall()

    print("Datos de la tabla card:")
    for fila in resultados:
        print(fila)  # Imprime cada fila como una tupla

    conn.commit()  # No estrictamente necesario para SELECT, pero no causa daño
    print("\nOK Connection.\n")

except psycopg2.Error as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()