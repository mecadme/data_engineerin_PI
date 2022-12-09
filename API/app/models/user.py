from sqlalchemy import Table, Column 
from sqlalchemy.types import Integer, String
from config.db import engine, meta 

plataformas = Table("plataformas",meta,
            Column("idStream", String(30)) ,
            Column("category", String(50)),
            Column("title", String(120)) ,
            Column("release_year", Integer),
            Column("duration_len", Integer) ,
            Column("duration_type", String(20)) ,
            Column("platform", String(20)) )



actores = Table("actores",meta,
            Column("idStream", String(30)) ,
            Column("cast", String(120)),
           )


genero = Table("genero",meta,
            Column("idStream", String(30)) ,
            Column("genre", String(120)),
           )



meta.create_all(engine)