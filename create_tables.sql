CREATE TABLE Oppilaat (
    opiskelija_id SERIAL PRIMARY KEY,
    nimi VARCHAR(100) NOT NULL,
    syntyma_aika DATE NOT NULL,
    yhteystiedot VARCHAR(200)
);

CREATE TABLE Kurssit (
    kurssi_id SERIAL PRIMARY KEY,
    kurssi_nimi VARCHAR(100) NOT NULL,
    opettaja VARCHAR(100) NOT NULL
);

CREATE TABLE Ilmoittautumiset (
    ilmoittautumis_id SERIAL PRIMARY KEY,
    opiskelija_id INT REFERENCES Oppilaat(opiskelija_id),
    kurssi_id INT REFERENCES Kurssit(kurssi_id),
    ilmoittautumispaiva DATE NOT NULL
);
