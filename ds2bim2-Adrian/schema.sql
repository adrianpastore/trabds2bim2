CREATE DATABASE "ds2bim2";

CREATE TABLE "usuario" (
	"cod" serial, 
	"nome" VARCHAR(100) NOT NULL,
	"login" VARCHAR(100) UNIQUE NOT NULL,
	"senha" VARCHAR(32) NOT NULL,
	CONSTRAINT "AutorPK" PRIMARY KEY (cod));

INSERT INTO "usuario" ("nome", "login", "senha") VALUES
('Carlos Sempre','perdeCarros', md5('vouDeMoto'));

CREATE TABLE "ideia" (
	"cod" serial,
	"titulo" varchar(100) NOT NULL,
	"descricao" text NOT NULL,
	"codusuario" int,
	"datahoraatualizacao" timestamp,
	CONSTRAINT "TrabalhoPK" PRIMARY KEY ("cod"),
    CONSTRAINT "IdeiaUserFK" FOREIGN KEY ("codusuario")
        REFERENCES "usuario" 
        ON DELETE SET NULL
        ON UPDATE SET NULL);