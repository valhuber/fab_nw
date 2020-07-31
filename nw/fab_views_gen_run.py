import logging
# not required: from app.models import *
import sys
import sqlalchemy
import sqlalchemy.ext
from sqlalchemy import MetaData

from nw.fab_views_gen import fab_views_gen

log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")

conn_string = "sqlite:///nw/nw.db"  #  TODO - use config file, per cmd line args
engine = sqlalchemy.create_engine(conn_string)

connection = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine, resolve_fks=True)

fab_views_gen = fab_views_gen.FabViewsGen()
generated_view = fab_views_gen.generate_view(metadata)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)
