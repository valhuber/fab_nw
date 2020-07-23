print("build_views_base")


class build_views_base(object):
    """
    Iterate over all tables, create view statements for each
    """
    _result = "# default view.py\n\n"

    _indent = "   "
    _pages_generated = 0

    def generate_view(self, db):

        tables = db.Model.metadata.tables
        self._result += self.generate_module_imports()

        for each_table in tables.items():
            each_result = self.process_each_table(each_table[1])
            self._result += each_result

        self._result += self.process_add_views(tables)
        return self._result

    def process_each_table(self, each_table):
        table_name = each_table.name
        print("process_each_table: " + table_name)
        if (table_name.startswith("ab_")):
            return "# skip admin table: " + table_name + "\n"
        else:
            self._pages_generated += 1
            table_view_class_definition = ""
            table_view_class_definition += self.generate_class_for_table(
                each_table)
            return table_view_class_definition + "\n\n"

    def generate_module_imports(self):
        result = "from flask_appbuilder import ModelView\n"
        result += "from flask_appbuilder.models.sqla.interface import SQLAInterface\n"
        result += "from . import appbuilder, db\n"
        result += "from .models import *\n"
        result += "\n"
        return result

    def generate_class_for_table(self, each_table):
        return self.perform_class_for_table(each_table, "ModelViewSuper")

    def perform_class_for_table(self, each_table, model_name):
        result = "\n\n\nclass " + each_table.name + \
            model_name + "(" + model_name + "):\n"
        result += self._indent + \
            "datamodel = SQLAInterface(" + each_table.name + ")"
        return result

    def name_column(self, metadata):
        return "name"

    def process_add_views(self, tables):
        result = "\n\n# stub - appbuilder.add_view(...)\n\n"
        result += "#  " + str(len(tables)) + " table(s) in model, " + \
            str(self._pages_generated) + " page(s) generated\n\n"
        return result
