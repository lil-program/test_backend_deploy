from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from termcolor import colored

if settings.SQLALCHEMY_DATABASE_URI:
    engine = create_engine(
        settings.SQLALCHEMY_DATABASE_URI,
        pool_pre_ping=True,
    )
    SessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    if settings.is_development():
        db_info = f"Using database at {settings.SQLALCHEMY_DATABASE_URI}"
        print(colored(db_info, "blue"))
else:
    raise ValueError(colored("SQLALCHEMY_DATABASE_URI is not set", "red"))
