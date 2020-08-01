import sqlalchemy
import sqlalchemy.ext
from sqlalchemy import MetaData

import fab_views_gen_base

import logging
from typing import NewType
# not required: from app.models import *
import sys

TableModelInstance = NewType('TableModelInstance', object)


class FabViewsGen(fab_views_gen_base.FabViewsGenBase):
    """
        @see fab_code_gen_base

        This extends it, to execute, and provide overrides as required
    """

    def model_name(self, table_name: str):  # override
        """
            You might want to override this
            depending on your table name.
        """
        return "ModelView"

    def favorite_column(self, a_table_def: TableModelInstance):
        """
            You might want to override this
            depending on your table name.
        """
        result = super().favorite_column(a_table_def)
        return result

    def favorite_name(self):
        """
            You might want to override this
            depending on your language, or db naming conventions.
        """
        return ["name", "description"]

log = logging.getLogger(__name__)
log.debug("build_views (overrides here)")

log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")

conn_string = "sqlite:///nw/nw.db"  #  TODO - use config file, per cmd line args
engine = sqlalchemy.create_engine(conn_string)

connection = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine, resolve_fks=True)

fab_views_gen = FabViewsGen()
generated_view = fab_views_gen.generate_view(metadata)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)
