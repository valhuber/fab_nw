import logging
from app import db
from app.models import *
import random
import string
import sys

from datetime import datetime

from nw.fab_views_gen import fab_views_gen

import logging

log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version +"\n\n")

metadata = db.Model.metadata   #  hmm.... depends on from app import db
fab_views_gen = fab_views_gen.FabViewsGen()
generated_view = fab_views_gen.generate_view(metadata)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)