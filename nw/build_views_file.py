import logging
from app import db
from app.models import *
import random
import string
import sys

from datetime import datetime

from nw.build_views import build_views

print("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version +"\n\n")
view_builder = build_views.build_views()
dummy = None
generated_view = view_builder.generate_view(db)
print("\n\nCompleted, generated views.py-->\n\n" + generated_view)

log = logging.getLogger(__name__)