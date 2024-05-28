#CREAZIONE TABELLE

create_review_table = """
CREATE TABLE review (
  review_id INT AUTO_INCREMENT PRIMARY KEY,
  podcast_id VARCHAR(150),
  titolo VARCHAR(100),
  contenuto TEXT,
  rating FLOAT
);
"""
create_categorie_table = """
CREATE TABLE categorie (
  category_id INT PRIMARY KEY,
  nome_cat VARCHAR(250)
);
"""
create_podcast_table = """
CREATE TABLE podcast (
  podcast_id VARCHAR(150) PRIMARY KEY,
  titolo VARCHAR(250),
  category_id INT
);
"""

create_dettagli_table = """
CREATE TABLE dettagli (
  autore VARCHAR(100),
  descrizione VARCHAR(60),
  avg_rating FLOAT,
  rating_count INT,
  URL VARCHAR(100),
  podcast_id VARCHAR(150),
  img_url VARCHAR(100)
);
"""

create_utenti_table = """
CREATE TABLE utenti (
  utente_id INT PRIMARY KEY,
  user_name VARCHAR(150),
  hashed_password TEXT,
  e_mail VARCHAR (200)
);
"""

create_recensioni_sito_table = """
CREATE TABLE recensioni_sito (
  recensione_id INT PRIMARY KEY,
  titolo_recensione VARCHAR(150),
  testo VARCHAR(200),
  voto INT,
  podcast_id VARCHAR(150),
  utente_id INT
);
"""
create_autori_table = """
CREATE TABLE autori (
  autore_id INT PRIMARY KEY,
  name VARCHAR(250)
);
"""
create_autori_podcast_table = """
CREATE TABLE autori_podcast(
  podcast_id VARCHAR(150),
  autore_id INT
);
"""

#inserimento ALTER TABLE

alter_podcast ="""
ALTER TABLE podcast
ADD FOREIGN KEY(category_id)
REFERENCES categorie(category_id)
ON DELETE CASCADE
;
"""

alter_review = """
ALTER TABLE review
ADD FOREIGN KEY(podcast_id)
REFERENCES podcast(podcast_id)
ON DELETE SET NULL
ON UPDATE RESTRICT;
"""

alter_dettagli = """
ALTER TABLE dettagli
ADD FOREIGN KEY(podcast_id)
REFERENCES podcast(podcast_id)
ON DELETE SET NULL
ON UPDATE RESTRICT;
"""

alter_recensioni_sito = """
ALTER TABLE recensioni_sito
ADD FOREIGN KEY(podcast_id)
REFERENCES podcast(podcast_id)
ON DELETE SET NULL
ON UPDATE RESTRICT,
ADD FOREIGN KEY(utente_id)
REFERENCES utenti(utente_id)
ON DELETE SET NULL
;
"""

alter_autori_podcast = """
ALTER TABLE autori_podcast
ADD FOREIGN KEY(podcast_id)
REFERENCES podcast(podcast_id)
ON DELETE SET NULL
ON UPDATE RESTRICT,
ADD FOREIGN KEY(autore_id)
REFERENCES autori(autore_id)
ON DELETE SET NULL;
"""

query_autori = "INSERT INTO autori VALUES (%s,%s)"
query_podcast = "INSERT INTO podcast VALUES (%s,%s,%s)"
query_autori_podcast = "INSERT INTO autori_podcast VALUES (%s,%s)"
query_categorie = "INSERT INTO categorie VALUES (%s,%s)"
query_reviews = "INSERT INTO review (podcast_id,titolo,contenuto,rating) VALUES (%s,%s,%s,%s)"