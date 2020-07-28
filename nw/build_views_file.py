import logging
from app import db
from app.models import *
import random
import string
import sys

from datetime import datetime

from nw.build_views import build_views

import logging

log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version +"\n\n")

view_builder = build_views.BuildViews()
generated_view = view_builder.generate_view(db)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)