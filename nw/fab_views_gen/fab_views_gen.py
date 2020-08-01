from nw.fab_views_gen.fab_views_gen_base import FabViewsGenBase

import logging
from typing import NewType

TableModelInstance = NewType('TableModelInstance', object)

log = logging.getLogger(__name__)
log.debug("build_views (overrides here)")


class FabViewsGen(FabViewsGenBase):
    """
        @see fab_code_gen_base
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