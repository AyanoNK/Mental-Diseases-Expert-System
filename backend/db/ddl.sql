
-- Data definition language for the backend.

CREATE TABLE Enfermedad (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL
);

CREATE TABLE Consultas (
  id SERIAL PRIMARY KEY ,
  question_1 BOOL NOT NULL,
  question_2 BOOL NOT NULL,
  question_3 BOOL NOT NULL,
  question_4 BOOL NOT NULL,
  question_5 BOOL NOT NULL,
  question_6 BOOL NOT NULL,
  question_7 BOOL NOT NULL,
  question_8 BOOL NOT NULL,
  question_9 BOOL NOT NULL,
  question_10 BOOL NOT NULL,
  question_11 BOOL NOT NULL,
  question_12 BOOL NOT NULL,
  question_13 BOOL NOT NULL,
  Enfermedad_id INTEGER NOT NULL,
  CONSTRAINT Enfermedad_FK FOREIGN KEY (Enfermedad_id) REFERENCES Enfermedad(id)
);

