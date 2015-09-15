from settings import DB_URL, DB_USER, DB_PASSWORD, DB_NAME
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine


class GenericModel(object):

    def __init__(self, class_name):
        self.base = automap_base()
        self.engine = create_engine(
            "mysql+pymyql://{0}:{1}@{2}/{3}".format(
                DB_USER, DB_PASSWORD, DB_URL, DB_NAME
            )
        )
        self.base.prepare(self.engine, reflect=True)
        self.this_class = self.base.classes.class_name

    def get_fields(self, class_name):
        return self.this_class.__dict__
