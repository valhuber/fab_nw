# -*- coding: utf-8 -*-
"""Generates FAB view files from db model.

This is the super class
    Use build_views, and provide overides as required.


To run:
    1. Generate model (consider https://pypi.org/project/sqlacodegen/)
        a. Hand-add relationships
        b. Hand-edit classes, e.g.,
            not: def Customer(Model)
            but: def Customer(BaseMixin, Model)
    2. Run build_views_base.py
    3. Copy contents to your app/views.py file

Todo:
    * Proper related_views handling (and fix models.py)
    * Predictive Joins
    * Override Show-Name field first (eg, not "name" in French)
    * Lookups (find/choose Product for Order Detail)
    * Tune edit / add cols (e.g. no Ids)
    * Suppress Master on Chid (no Order# on each Order Detail)
    * More overrides (discuss approach with Daniel)
    * Better packaging (requires Daniel discussion)
    * Recognize other views, such as Maps
    * FAB
        * better col/field captions
        * updatable list (=> multi-row save)

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

print("\n\BuildViewsBase loading")


class BuildViewsBase(object):
    """
    Iterate over all tables, create view statements for each
    """
    _result = "# default view.py\n\n"

    _indent = "   "
    _tables_generated = set()  # to address "generate children first"
    num_pages_generated = 0

    def generate_view(self, a_db):
        meta_tables = a_db.Model.metadata.tables
        self._result += self.generate_module_imports()
        for each_table in meta_tables.items():
            each_result = self.process_each_table(each_table[1])
            self._result += each_result
        self._result += self.process_module_end(meta_tables)
        return self._result



    def generate_module_imports(self) -> str:
        result = "from flask_appbuilder import ModelView\n"
        result += "from flask_appbuilder.models.sqla.interface import SQLAInterface\n"
        result += "from . import appbuilder, db\n"
        result += "from .models import *\n"
        result += "\n"
        return result



    def process_each_table(self, a_table_def)  -> str:
        """
            Generate class and add_view for given table.

            These must be children first, so "related_views" compile.
                We therefore recurse for children first.

            Args:
                a_table_def - tables' model instance
        """
        result = ""
        table_name = a_table_def.name
        print("process_each_table: " + table_name)
        if (table_name.startswith("ab_")):
            return "# skip admin table: " + table_name + "\n"
        elif (table_name in self._tables_generated):
            print("table already generated per recursion: " + table_name)
            return "# table already generated per recursion: " + table_name
        else:
            child_list = self.find_child_list(a_table_def)
            for each_child in child_list:  # recurse to ensure children first
                print(".. but children first: " + each_child.name)
                result += self.process_each_table(each_child)
                self._tables_generated.add(each_child.name)
            self.num_pages_generated += 1
            model_name = self.model_name(table_name)
            class_name = a_table_def.name + model_name
            result += "\n\n\nclass " + class_name + "(" + model_name + "):\n"
            result += self._indent + "datamodel = SQLAInterface(" + a_table_def.name + ")\n"
            result += self._indent + self.list_columns(a_table_def)
            result += self._indent + self.show_columns(a_table_def)
            result += self._indent + self.edit_columns(a_table_def)
            result += self._indent + self.add_columns(a_table_def)
            result += self._indent + self.related_views(a_table_def)
            result += "\nappbuilder.add_view(\n" + \
                self._indent + self._indent + class_name + ", " +\
                "\"" + table_name + " List\", " +\
                "icon=\"fa-folder-open-o\", category=\"Menu\")\n"
            return result + "\n\n"



    def generate_class_for_table(self, a_table_def):
        return self.perform_class_for_table(a_table_def, "ModelView")

    def perform_class_for_table(self, a_table_def, a_model_name):
        result = "\n\n\nclass " + a_table_def.name + \
            a_model_name + "(" + a_model_name + "):\n"
        result += self._indent + \
            "datamodel = SQLAInterface(" + a_table_def.name + ")"
        return result
    


    def list_columns(self, a_table_def):
        result =  "list_columns = ["
        columns = a_table_def.columns;
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
   


    def show_columns(self, a_table_def):
        result =  "show_columns = ["
        columns = a_table_def.columns;
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
   


    def edit_columns(self, a_table_def):
        result =  "edit_columns = ["
        columns = a_table_def.columns;
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
   


    def add_columns(self, a_table_def):
        result =  "add_columns = ["
        columns = a_table_def.columns;
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
   


    def related_views(self, a_table_def):  # TODO - stub, for testing
        """
            Builds related_views from Foreign Key definitions

            Todo
                * are child roles req's (e.g.,) children = relationship("Child")
                * are multiple relationsips supported (dept has worksFor / OnLoan Emps)
                * are circular relationships supports (dept has emps, emp has mgr)
        """
        result =  "related_views = ["
        child_list = self.find_child_list(a_table_def)
        for each_child in child_list:
            result += each_child.fullname + self.model_name(each_child)
        """
        if (each_table.name == "Customer"):
            result += "OrderModelView"
        elif (each_table.name == "Order"):
            result += "OrderDetailModelView"
        elif (each_table.name == "Product"):
            result += "OrderDetailModelView"
        """
        result += "]\n"
        return result



    def find_child_list(self, a_table_def):
        """
            Returns list of models w/ fKey to each_table

            Not super efficient
                pass entire table list for each table
                ok until very large schemas
        """
        child_list = []
        all_tables = a_table_def.metadata.tables
        all_tables_items = all_tables.items()
        for each_possible_child_tuple in all_tables.items():
            each_possible_child = each_possible_child_tuple[1]
            parents = each_possible_child.foreign_keys
            # if (a_table_def.name == "Customer" and each_possible_child.name == "Order"):
            #    print (a_table_def)
            for each_parent in parents:
                each_parent_name = each_parent.target_fullname
                loc_dot = each_parent_name.index(".")
                each_parent_name = each_parent_name[0:loc_dot]
                if (each_parent_name == a_table_def.name):
                    child_list.append(each_possible_child)
        return child_list

    def model_name(self, a_table_name):  # override as req'd
        """
            returns model_name, defaulted to "ModelView"

            intended for subclass override, for custom views
        """
        return "ModelView"


    def name_column(self, metadata):
        return "name"

    def process_module_end(self, a_metadata_tables):
        result = "#  " + str(len(a_metadata_tables)) + " table(s) in model, " + \
            str(self.num_pages_generated) + " page(s) generated\n\n"
        return result
