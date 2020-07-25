print("\n\nbuild_views_base loading")


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
        self._result += self.process_module_end(tables)
        return self._result



    def process_each_table(self, each_table):
        table_name = each_table.name
        print("process_each_table: " + table_name)
        if (table_name.startswith("ab_")):
            return "# skip admin table: " + table_name + "\n"
        else:
            self._pages_generated += 1
            model_name = self.model_name(table_name)
            class_name = each_table.name + model_name
            result = "\n\n\nclass " + class_name + "(" + model_name + "):\n"
            result += self._indent + "datamodel = SQLAInterface(" + each_table.name + ")\n"
            result += self._indent + self.list_columns(each_table)
            result += self._indent + self.show_columns(each_table)
            result += self._indent + self.edit_columns(each_table)
            result += self._indent + self.add_columns(each_table)
            result += self._indent + self.related_views(each_table)
            result += "\nappbuilder.add_view(\n" + \
                self._indent + self._indent + class_name + ", " +\
                "\"" + table_name + " List\", " +\
                "icon=\"fa-folder-open-o\", category=\"Menu\")\n"
            return result + "\n\n"



    def generate_module_imports(self):
        result = "from flask_appbuilder import ModelView\n"
        result += "from flask_appbuilder.models.sqla.interface import SQLAInterface\n"
        result += "from . import appbuilder, db\n"
        result += "from .models import *\n"
        result += "\n"
        result += "#TODO - if you get compile errors due to class reference depencencies\n"
        result += "#  - temporary fix - edit this file to move class defs\n\n"
        return result

    def generate_class_for_table(self, each_table):
        return self.perform_class_for_table(each_table, "ModelView")

    def perform_class_for_table(self, each_table, model_name):
        result = "\n\n\nclass " + each_table.name + \
            model_name + "(" + model_name + "):\n"
        result += self._indent + \
            "datamodel = SQLAInterface(" + each_table.name + ")"
        return result
    


    def list_columns(self, each_table):
        result =  "list_columns = ["
        columns = each_table.columns;
        has_id = "*"
        result += ""
        column_count = 0
        for each_column in columns:
            if (each_column.name.lower() == "id"):
                has_id = each_column.name
                continue
            column_count += 1
            if (column_count > 4):
                break
            if (column_count > 1):
                result += ", "
            result += "\"" + each_column.name + "\""
        result += "]\n"
        return result
   


    def show_columns(self, each_table):
        result =  "show_columns = ["
        columns = each_table.columns;
        has_id = "*"
        result += ""
        column_count = 0
        for each_column in columns:
            if (each_column.name.lower() == "id"):
                has_id = each_column.name
                continue
            column_count += 1
            if (column_count > 1):
                result += ", "
            result += "\"" + each_column.name + "\""
        if (has_id != "*"):
            result += ", \"" + has_id + "\""
        result += "]\n"
        return result
   


    def edit_columns(self, each_table):
        result =  "edit_columns = ["
        columns = each_table.columns;
        has_id = "*"
        result += ""
        column_count = 0
        for each_column in columns:
            if (each_column.name.lower() == "id"):
                has_id = each_column.name
                continue
            column_count += 1
            if (column_count > 1):
                result += ", "
            result += "\"" + each_column.name + "\""
        if (has_id != "*"):
            result += ", \"" + has_id + "\""
        result += "]\n"
        return result
   


    def add_columns(self, each_table):
        result =  "add_columns = ["
        columns = each_table.columns;
        has_id = "*"
        result += ""
        column_count = 0
        for each_column in columns:
            if (each_column.name.lower() == "id"):
                has_id = each_column.name
                continue
            column_count += 1
            if (column_count > 1):
                result += ", "
            result += "\"" + each_column.name + "\""
        if (has_id != "*"):
            result += ", \"" + has_id + "\""
        result += "]\n"
        return result
   


    def related_views(self, each_table):  # TODO - stub, for testing
        result =  "related_views = ["
        if (each_table.name == "Customer"):
            result += "OrderModelView"
        elif (each_table.name == "Order"):
            result += "OrderDetailModelView"
        elif (each_table.name == "Product"):
            result += "OrderDetailModelView"
        result += "]\n"
        return result



    def model_name(self, table_name):  # override as req'd
        return "ModelViewSuper"


    def name_column(self, metadata):
        return "name"

    def process_module_end(self, tables):
        result = "#  " + str(len(tables)) + " table(s) in model, " + \
            str(self._pages_generated) + " page(s) generated\n\n"
        return result
