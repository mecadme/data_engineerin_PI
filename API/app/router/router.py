#Modularizar o dividir nuestros routers
from fastapi import APIRouter
from config.db import engine
from models.user import plataformas, actores, genero
from sqlalchemy import func, select


user = APIRouter()

#1-Máxima duración según tipo de film (película/serie), por plataforma y por año:
# El request debe ser: get_max_duration(año, plataforma, [min o season])

@user.get("/get_max_duration/{year}/{platform}/{tipo}", tags=["Querys"])
def get_max_duration(year:int,platform:str,tipo:str):
    with engine.connect() as conn:
        result = conn.execute(select(plataformas.c.duration_len,plataformas.c.title)
                            .where(plataformas.c.release_year == year)
                            .where(plataformas.c.platform==platform)
                            .where(plataformas.c.duration_type==tipo)
                            .order_by(plataformas.c.duration_len.desc())
                            )
        
        return result.first()
    
    
#2-Cantidad de películas y series (separado) por plataforma
#   El request debe ser: get_count_plataform(plataforma)

@user.get("/get_count_platform/{platform}", tags=["Querys"])
def get_count_platform(platform:str):
    with engine.connect() as conn:
        result = conn.execute(select(func.count(plataformas.c.category).label("Cantidad"),plataformas.c.category)                            
                            .where(plataformas.c.platform==platform)
                            .group_by(plataformas.c.category)
                            )
        
        return result.fetchall()
    

   
    
#3-Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
# El request debe ser: get_listedin('genero')
#Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 
# para la plataforma de amazon.   

@user.get("/get_listedin/{genre}", tags=["Querys"])
def get_listedin(genre:str):
    with engine.connect() as conn:
        result = conn.execute(select(plataformas.c.platform,func.count(plataformas.c.platform).label("Cantidad_repetidas"))
                            .join(genero,plataformas.c.idStream==genero.c.idStream)
                            .where(genero.c.genre == genre)
                            .group_by(plataformas.c.platform)
                            .order_by(func.count(plataformas.c.platform).desc()) )
        
        return result.first()



#4-Actor que más se repite según plataforma y año.
#El request debe ser: get_actor(plataforma, año)

@user.get("/get_actor/{platform}", tags=["Querys"])
def get_actor(platform:str,year:int):
    with engine.connect() as conn:
        result = conn.execute(select(func.count(actores.c.cast).label("Cantidad_apariciones"),actores.c.cast)
                                    .join(plataformas,plataformas.c.idStream==actores.c.idStream)
                                    .where(plataformas.c.release_year == year)
                                    .where(plataformas.c.platform==platform)
                                    .where(actores.c.cast!="sin dato")
                                    .group_by(actores.c.cast)
                                    .order_by(func.count(actores.c.cast).desc()))
        
        return result.first()