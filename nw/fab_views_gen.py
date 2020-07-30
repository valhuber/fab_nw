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

from nw.build_views import build_views


log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")

conn_string = "sqlite:///nw/nw.db"  #  metadata
engine = sqlalchemy.create_engine(conn_string)

connection = engine.connect()
meta = MetaData()
meta.reflect(bind=engine)

items = meta.tables.items()
for each_table in items:
    o = each_table[1]
    print("\nname", o.name)

# base.metadata  metadata
#  insp = reflection.Inspector.from_engine(engine)  #  compare to db

view_builder = build_views.BuildViews()
generated_view = view_builder.generate_view(meta)  #  fails (ab tables only)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)