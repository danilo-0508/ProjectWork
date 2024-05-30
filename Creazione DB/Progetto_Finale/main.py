import csv
from funzioni_DB import *
from query import *
from tqdm import tqdm


DB_NAME = "PodcastPro"
connection = create_server_connection("localhost", "root", "root")
# execute_query(connection, f'Create {DB_NAME}')
create_database(connection,DB_NAME)
connection = create_db_connection("localhost", "root","root", DB_NAME)

# esecuzione create tables
execute_query(connection, create_podcast_table)
execute_query(connection, create_dettagli_table)
execute_query(connection, create_categorie_table)
execute_query(connection, create_utenti_table)
execute_query(connection, create_recensioni_sito_table)
execute_query(connection, create_autori_table)
execute_query(connection, create_autori_podcast_table)
execute_query(connection, create_review_table)
# esecuzione alter table
execute_query(connection,alter_podcast)
execute_query(connection, alter_review)
execute_query(connection, alter_dettagli)
execute_query(connection, alter_recensioni_sito)
execute_query(connection, alter_autori_podcast)


inserimento_dati(connection,query_autori,"authors.csv")
inserimento_dati(connection, query_categorie, "categories.csv")
inserimento_dati(connection, query_podcast, "podcast.csv")
inserimento_dati(connection,query_autori_podcast,"authors_podcast.csv")
inserimento_review(connection,"reviews.csv")
inserimento_dati(connection,query_dettagli, "dettagli_podcast.csv")
