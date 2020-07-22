# from composite_keys.build_views.build_views_base import build_views_base.build_views_base
from nw.build_views.build_views_base import build_views_base

print("build_views (overrides here")

class build_views(build_views_base):

    def name_column(self, db):  # override as desired
        result = super().name_column(db)
        return result