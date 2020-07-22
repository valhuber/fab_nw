print("build_views_base")


class build_views_base(object):
    """
    Iterate over all tables, create view statements for each
    """
    _result = "from flask_appbuilder import ModelView\n"

    _result += "from flask_appbuilder.models.sqla.interface import SQLAInterface\n"

    _result += "from . import appbuilder, db\n"
    _result += "from .models import *\n"

    def generate_view(self, db):

        tables = db.Model.metadata.tables
        for each_table in tables.items():
            print(each_table)
            each_result = self.process_each_table(each_table[1])
            self._result += each_result
        return self._result

    def process_each_table(self, each_table):
        table_name = each_table.name
        if (table_name.startswith("ab_")):
            return "# skip admin table: " + table_name + "\n"
        else:
            table_view_class_definition = "class " + table_name + "ModelView(ModelView):"
            print("processing table: " + each_table)
            return table_view_class_definition

    def name_column(self, metadata):
        return "name"


