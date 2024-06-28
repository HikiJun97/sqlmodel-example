from sqlmodel import create_engine

db_url: str = f"mysql+pymysql://sgn04088:whgudwns1997@localhost:3306/test"

engine = create_engine(db_url, echo=True)
