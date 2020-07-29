
from nw.build_views.build_views_base import BuildViewsBase

import logging
from typing import NewType

TableModelInstance = NewType('TableModelInstance', object)

log = logging.getLogger(__name__)
log.debug("build_views (overrides here)")


class BuildViews(BuildViewsBase):
    """
        @see build_views_base

        This extends it, to provide overrides as required
    """

    def model_name(self, table_name: str):  # override
        """
            You might want to override this
            depending on your table name.
        """
        return "ModelView"

    def favorite_column(self, a_table_def: TableModelInstance):
        """
            You might want to override this
            depending on your table name.
        """
        result = super().favorite_column(a_table_def)
        return result

    def favorite_name(self):
        """
            You might want to override this
            depending on your language, or db naming conventions.
        """
        return ["name", "description"]
