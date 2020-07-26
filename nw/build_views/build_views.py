"""
    @see build_views_base
    this provides overrides as required
"""

# from composite_keys.build_views.build_views_base import build_views_base.build_views_base
from nw.build_views.build_views_base import BuildViewsBase

print("build_views (overrides here)")

class BuildViews(BuildViewsBase):

    def model_name(self, table_name):  # override
        return "ModelView"

    def favorite_column(self, a_table_def):  # override as desired
        result = super().favorite_column(a_table_def)
        return result

    def favorite_name(self):
        return ["name", "description"]

    def build_views_unused(self, model):
        """Generators have a ``Yields`` section instead of a ``Returns`` section.

            Args:
                model from db.

            Yields:
                Console output to be copied into app/views.py
        """
        
        self.super(model)