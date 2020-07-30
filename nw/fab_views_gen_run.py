import logging
#  from app.models import *
#  from app import db
from app.models import *
import random
import string
import sys
import sqlalchemy
import sqlalchemy.ext
from sqlalchemy import create_engine, select, MetaData, Table
# from sqlalchemy.engine import reflection

# FAILS - not getting metadata for nw, just ab_

from datetime import datetime

from nw.fab_views_gen import fab_views_gen


log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")

conn_string = "sqlite:///nw/nw.db"  #  TODO - use config file, per cmd line args
engine = sqlalchemy.create_engine(conn_string)

connection = engine.connect()
meta = MetaData()
meta.reflect(bind=engine)

fab_views_gen = fab_views_gen.FabViewsGen()
generated_view = fab_views_gen.generate_view(meta)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)