from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLAlchemy setup for both SQLite sources
DB_EXTERNAL = r"sqlite:///C:\\Users\\phuong\\OneDrive\\Private\\Xokthavi\\HR\\ZKTimeNet.db"
DB_LOCAL = "sqlite:///./local.db"

engEXT = create_engine(DB_EXTERNAL, connect_args={"check_same_thread": False})
engLOC = create_engine(DB_LOCAL, connect_args={"check_same_thread": False})


# # Create a metadata instance
# metadataEXT = MetaData()
# metadataLOC = MetaData()

# # Bind engines to metadata
# metadataEXT.bind = engEXT
# metadataLOC.bind = engLOC

# BasEXT = declarative_base(metadata=metadataEXT)
# BasLOC = declarative_base(metadata=metadataLOC)
Base = declarative_base()

SesEXT = sessionmaker(autocommit=False, autoflush=False, bind=engEXT)
SesLOC = sessionmaker(autocommit=False, autoflush=False, bind=engLOC)
