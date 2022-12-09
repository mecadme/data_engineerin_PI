from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:0000@host.docker.internal:3306/plat_streaming")

meta = MetaData()