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
    3. Copy console contents to your app/views.py file
    4. cd nw; flask run

Features:
    1. Generate views.py with 1 class per (not ab_) table
        a. "Favorite" fields (contains name) first
        b. Numeric keyfields last
    2. With Referenced for master/detail (Order before Customer)
        a. Generated child views first
    3. Predictive Joins (ProductName on Order+OrderDetail
        a. Note - *not* generated for edit/show, else you get fab "key errors"

Status:
    * Technology Preview

Todo:
    * OrderDetail - magnifying glass page fails
    * Complete relationships in models.py
    * Lookups (find/choose Product for Order Detail)
    * Suppress Master on Child (no Order# on each Order Detail)
        ** Big deal, since can't re-use child on multiple differnt parents.  Ugh
    * More overrides in build_views.py (discuss approach with Daniel)
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



    def list_columns(self, a_table_def):
        return self.gen_columns(a_table_def, "list_columns = [", 2, 4)



    def show_columns(self, a_table_def):
        return self.gen_columns(a_table_def, "show_columns = [", 99, 999)



    def edit_columns(self, a_table_def):
        return self.gen_columns(a_table_def, "edit_columns = [", 99, 999)



    def add_columns(self, a_table_def):
        return self.gen_columns(a_table_def, "add_columns = [", 99, 999)



    def gen_columns(self, a_table_def, a_view_type, a_max_joins, a_max_columns):
        """
        Generates statements like:

            list_columns = ["Id", "Product.ProductName", "Order.ShipName", "UnitPrice", "OrderId", "ProductId", "Id"]
        
        Arguments

            a_table_def - metadata for columns, relationships etc

            a_view_type - a string like "list_columns = ["

            a_max_joins - how many joins (e.g., fewer on list)

            a_max_fields - how many columns (e.g., fewer on list)
        """
        result =  a_view_type
        columns = a_table_def.columns;
        id_column_names = set()
        processed_column_names = set()
        result += ""
        if (a_table_def.name == "Territory"):
            print("Territory reached")

        favorite_column_name = self.favorite_column_name(a_table_def)
        column_count = 1
        result += "\"" + favorite_column_name + "\""
        processed_column_names.add(favorite_column_name)

        predictive_joins = self.predictive_join_columns(a_table_def)
        if ("list" in a_view_type or "show" in a_view_type):  # alert - prevent fab key errors!
            for each_join_column in predictive_joins:
                column_count += 1
                if (column_count > 1):
                    result += ", "
                result += "\"" + each_join_column + "\""
                if (column_count > a_max_joins):
                    break
        for each_column in columns:
            if (each_column.name in processed_column_names):
                continue
            if ("id" in each_column.name.lower()):  # ids are boring - do at end
                id_column_names.add(each_column.name)
                continue
            column_count += 1
            if (column_count > a_max_columns):  # - Todo - make external
                break
            if (column_count > 1):
                result += ", "
            result += "\"" + each_column.name + "\""
        for each_id_column_name in id_column_names:
            column_count += 1
            if (column_count > 1):
                result += ", "
            result += "\"" + each_id_column_name + "\""
        result += "]\n"
        return result



    def predictive_join_columns(self, a_table_def):
        """
            Returns set of col names (such Product.ProductName for OrderDetail)
        """
        result = set()
        foreign_keys = a_table_def.foreign_keys
        if (a_table_def.name == "OrderDetail"):
            print ("predictive_joins for: " + a_table_def.name)
        for each_foreign_key in foreign_keys:
            each_parent_name = each_foreign_key.target_fullname
            loc_dot = each_parent_name.index(".")
            each_parent_name = each_parent_name[0:loc_dot]
            each_parent = a_table_def.metadata.tables[each_parent_name]
            favorite_column_name = self.favorite_column_name(each_parent)
            result.add(each_parent_name + "." + favorite_column_name)
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
        related_count = 0
        child_list = self.find_child_list(a_table_def)
        for each_child in child_list:
            related_count += 1
            if (related_count > 1):
                result += ", "
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


    def favorite_column_name(self, a_table_def) -> str:
        """
            returns string of first column that is...
                named <favorite_name> (default to "name"),
                containing <favorite_name>
                (or first column)
        """
        favorite_names = self.favorite_name()
        for each_favorite_name in favorite_names:
            columns = a_table_def.columns
            for each_column in columns:
                col_name = each_column.name.lower()
                if (col_name == each_favorite_name):
                    return each_column.name
            for each_column in columns:
                col_name = each_column.name.lower()
                if (each_favorite_name in col_name):
                    return each_column.name
        for each_column in columns:  # no favorites, just return 1st
            return each_column.name


    def favorite_name(self):
        """
            returns the substring used to find favorite column name

            override per language, db conventions

            eg, 
                name in English
                nom in French
        """
        return ["nom", "description"]



    def process_module_end(self, a_metadata_tables):
        result = "#  " + str(len(a_metadata_tables)) + " table(s) in model, " + \
            str(self.num_pages_generated) + " page(s) generated\n\n"
        return result
