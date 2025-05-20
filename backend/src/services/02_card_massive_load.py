import psycopg2
import pandas as pd
import ast

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname="sparkcarddb",
    user="postgres",
    password="spk2025--",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

path = "C:/Users/rober/OneDrive/Desktop/Coding_for_living/Rob-DVLP2024/sparkcard/app/services/"
file = (f"{path}cards.csv")
       
df = pd.read_csv(file, sep=",")  

# Funciones auxiliares para insertar y obtener IDs
#                 ("area", "area_name", row["area_name"], "area_id")
def get_or_create_id(table, col, value, return_id_col):
    if pd.isna(value):
        return None
    cur.execute(f"SELECT {return_id_col} FROM {table} WHERE {col} = %s", (value,))
    row = cur.fetchone()
    # print (f"1=========={return_id_col}========{row}")
    if row:
        return row[0]
    
    print (f"1.1====INSERT INTO======{table}|{col}|RETURNING {return_id_col}| value:{value}======{row}")
    
    #                       "authors" "author_name"                  "author_id"    "juan perez"
    cur.execute(f"INSERT INTO {table} ({col}) VALUES (%s) RETURNING {return_id_col}", (value,))
    return cur.fetchone()[0]

def get_or_create_author(name): # Juan Perez
    return get_or_create_id("authors", "author_name", name, "author_id")

def get_or_create_source(title, author_name): # libro de proyectos, Juan Perez
    author_id = get_or_create_author(author_name) # Juan Perez
    # print (f"2=======================author_id={author_id}")
    # print (f"2.1======================title={title}, author_id={author_id}")
    cur.execute("SELECT sources_id FROM sources WHERE sources_title = %s AND sources_author_id = %s", (title, author_id))
    row = cur.fetchone()
    # print (f"3================================={row}")
    # Si la fuente ya existe, devolver su ID
    if row:
        return row[0]
    
    print (f"3.1====INSERT INTO sources====title={title}, author_id={author_id}============{row}")
    cur.execute("INSERT INTO sources (sources_title, sources_author_id) VALUES (%s, %s) RETURNING sources_id", (title, author_id))
    return cur.fetchone()[0]

def get_or_create_array(table, col, values, return_id_col):
    ids = []
    for val in values:
        if not val.strip():
            continue
        cur.execute(f"SELECT {return_id_col} FROM {table} WHERE {col} = %s", (val,))
        row = cur.fetchone()
        if row:
            ids.append(row[0])
        else:
            cur.execute(f"INSERT INTO {table} ({col}) VALUES (%s) RETURNING {return_id_col}", (val,))
            ids.append(cur.fetchone()[0])
    return ids

# Procesar cada fila
for _, row in df.iterrows():
    area_id          = get_or_create_id("area", "area_name", row["card_area"], "area_id")
    subarea_id       = get_or_create_id("subarea", "subarea_name", row["card_subarea"], "subarea_id")
    topic_id         = get_or_create_id("topic", "topic_name", row["card_topic"], "topic_id")
    subtopic_id      = get_or_create_id("subtopic", "subtopic_name", row["card_subtopic"], "subtopic_id")
    
    language_id      = get_or_create_id("languages", "language_name", row["card_language"], "language_id")
    source_id        = get_or_create_source(row["card_source"], row["card_source_author"])
    cardtype_id      = get_or_create_id("card_type", "cardtype_name", row["card_type"], "cardtype_id")
    diff_level_id    = get_or_create_id("diff_level", "diff_level_name", row["card_diff_level"], "diff_level_id")

    tags             = get_or_create_array("tags", "tags_name", row["card_tags"].split(";"), "tags_id")
    keywords         = get_or_create_array("keywords", "keywords_name", row["card_keywords"].split(";"), "keywords_id")

    question_type_id = get_or_create_id("question_type", "question_type_name", row["card_question_type"], "question_type_id")
    
    user_id          = 3  # sustituir por el valor del usuario de la sesión
    status_id        = 1  # Asignar "Draft" como estado predeterminado

    answer_options_str = row["card_answer_options"]
    correct_answers_str = row["card_correct_answers"]

    # Evalúa la cadena como una lista de Python y luego formatea como literal de array de PostgreSQL
    try:
        answer_options_list = ast.literal_eval(answer_options_str)
        formatted_answer_options = '{' + ','.join(answer_options_list) + '}' if answer_options_list else None
    except (ValueError, SyntaxError):
        formatted_answer_options = None  # Manejar casos donde la cadena no es una lista válida

    try:
        correct_answers_list = ast.literal_eval(correct_answers_str)
        formatted_correct_answers = '{' + ','.join(correct_answers_list) + '}' if correct_answers_list else None
    except (ValueError, SyntaxError):
        formatted_correct_answers = None  # Manejar casos donde la cadena no es una lista válida

    cur.execute("""
        INSERT INTO card (
            card_area_id,
            card_subarea_id,
            card_topic_id,
            card_subtopic_id,
            card_language_id,
            card_source_id,
            card_type_id,
            card_diff_level_id,
            card_tags_id,
            card_keywords_id,
            card_question_concept,
            card_question_type_id,
            card_answer_options,
            card_correct_answers,
            card_explanation,
            card_creator_id,
            card_status_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        area_id,
        subarea_id,
        topic_id,
        subtopic_id,
        language_id,
        source_id,
        cardtype_id,
        diff_level_id,
        tags,
        keywords,
        row["card_question_concept"],
        question_type_id,
        # row["card_answer_options"],
        # row["card_correct_answers"],
        formatted_answer_options,  # Usar el formato de PostgreSQL
        formatted_correct_answers,  # Usar el formato de PostgreSQL
        row["card_explanation"],
        user_id,
        status_id
    ))

conn.commit()
print("Fichas importadas exitosamente.")

cur.close()
conn.close()
