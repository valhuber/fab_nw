import logging
from app import db
from app.models import *
import random
import string

from datetime import datetime

from nw.build_views import build_views

view_builder = build_views.build_views()
dummy = None
generated_view = view_builder.generate_view(db)
print("running, views.py: " + generated_view)

log = logging.getLogger(__name__)