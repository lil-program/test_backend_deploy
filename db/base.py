# Import all the models, so that Base has them before being
# imported by Alembic
from backend.db.base_class import Base  # noqa
from models.user import User  # noqa
from models.closet import Closet  # noqa
from models.clothes import Clothes  # noqa
