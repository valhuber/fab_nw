import logging

from nw import app
# this works, but hard-coded -- prefer something like: from .. import app
# from ../app import app
from app.models import *

import random
import string
import sys

# FIXME - this experiment fails... also unable to make this "just run"

from datetime import datetime

from nw.build_views import build_views

print("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version +"\n\n")
view_builder = build_views.build_views()
dummy = None
generated_view = view_builder.generate_view(db)
print("\n\nCompleted, generated views.py-->\n\n" + generated_view)

log = logging.getLogger(__name__)

print("build_views (overrides here)")

class build_views(build_views_base):

    def model_name(self, table_name):  # override
        return "ModelView"

    def name_column(self, db):  # override as desired
        result = super().name_column(db)
        return result
