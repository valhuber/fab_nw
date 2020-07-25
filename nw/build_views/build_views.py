"""
    @see build_views_base
    this provides overrides as required
"""

# from composite_keys.build_views.build_views_base import build_views_base.build_views_base
from nw.build_views.build_views_base import build_views_base

print("build_views (overrides here)")

class build_views(build_views_base):

    def model_name(self, table_name):  # override
        return "ModelView"

    def name_column(self, db):  # override as desired
        result = super().name_column(db)
        return result

    def build_views(self, model):
        """Generators have a ``Yields`` section instead of a ``Returns`` section.

            Args:
                model from db.

            Yields:
                Console output to be copied into app/views.py
        """
        
        self.super(model)