# -*- coding: utf-8 -*-
"""Generates FAB view files from db model.

This is the super class
    Extended by build_views, for overides as required.

Discussion 7/28
    Code cleanup: flake8, black (now activated, done?)
    Standard out: print vs. log (done)
    Annotations (done)
    Command line, using click (but, customization via subclass)
        Needs discussion FIXME
            fab_views_gen_run depends on dir location of app
            to obtain the models (from app.models import *).
                Will that work in cmd line?  Is there a better way?
            Also, the options are sometimes code, not simple strings
                E.g., model_name might depend on table_name
        Also discuss - how will fab user discover fab_views_gen?
            Flask-AppBuilder-Skeleton includes reference?  or code itself??

To run:
    1. Generate model (consider https://pypi.org/project/sqlacodegen/)
        a. Hand-add relationships
        b. Hand-edit classes, e.g.,
            not: def Customer(Model)
            but: def Customer(BaseMixin, Model)
    2. Run fab_views_gen_run.py
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
    * Query_columns
    * OrderDetail - magnifying glass page fails
    * Complete relationships in models.py
    * Lookups (find/choose Product for Order Detail)
    * Suppress Master on Child (no Order# on each Order Detail)
        ** Big deal, since can't re-use child on multiple different parents.
        ** Ugh
    * More overrides in build_views.py (discuss approach with Daniel)
    * Better packaging (requires Daniel discussion)
    * Recognize other views, such as Maps
    * FAB
        * better col/field captions
        * updatable list (=> multi-row save)
"""

import logging
import datetime
from typing import NewType

MetaData = NewType('MetaData', object)
MetaDataTable = NewType('MetaDataTable', object)


log = logging.getLogger(__name__)
log.debug("BuildViewsBase loading...")


class FabViewsGenBase(object):
    """
    Iterate over all tables, create view statements for each
    """

    _result = (
        "# default views.py, generated at: " +
        str(datetime.datetime.now()) + "\n\n"
    )

    _indent = "   "
    _tables_generated = set()  # to address "generate children first"
    num_pages_generated = 0

    def generate_view(self, a_metadata: MetaData) -> str:
        """
            Returns a string of views.py content

            This is the main entry / starting point.

            Parameters:
                argument1 a_metadata - MetaData (e.g, metadata = MetaData())
        """
        meta_tables = a_metadata.tables  # a_db.Model.metadata.tables
        self._result += self.generate_module_imports()
        for each_table in meta_tables.items():
            each_result = self.process_each_table(each_table[1])
            self._result += each_result
        self._result += self.process_module_end(meta_tables)
        return self._result

    def generate_module_imports(self) -> str:
        """
            Returns a string of views.py imports

            (first portion of views.py file)
        """
        result = "from flask_appbuilder import ModelView\n"
        result += "from flask_appbuilder.models.sqla.interface import SQLAInterface\n"
        result += "from . import appbuilder, db\n"
        result += "from .models import *\n"
        result += "\n"
        return result

    def process_each_table(self, a_table_def: MetaDataTable) -> str:
        """
            Generate class and add_view for given table.

            These must be ordered children first,
            so view.py compiles properly
            ("related_views" would otherwise fail to compile).

            We therefore recurse for children first.

            Parameters
                argument1 a_table_def - TableModelInstance

            Returns
                string class and add_view for given table.
        """
        result = ""
        table_name = a_table_def.name
        log.debug("process_each_table: " + table_name)
        if table_name.startswith("ab_"):
            return "# skip admin table: " + table_name + "\n"
        elif table_name in self._tables_generated:
            log.debug("table already generated per recursion: " + table_name)
            return "# table already generated per recursion: " + table_name
        else:
            child_list = self.find_child_list(a_table_def)
            for each_child in child_list:  # recurse to ensure children first
                log.debug(".. but children first: " + each_child.name)
                result += self.process_each_table(each_child)
                self._tables_generated.add(each_child.name)
            self.num_pages_generated += 1
            model_name = self.model_name(table_name)
            class_name = a_table_def.name + model_name
            result += "\n\n\nclass " + class_name + "(" + model_name + "):\n"
            result += (
                self._indent + "datamodel = SQLAInterface(" +
                a_table_def.name + ")\n"
            )
            result += self._indent + self.list_columns(a_table_def)
            result += self._indent + self.show_columns(a_table_def)
            result += self._indent + self.edit_columns(a_table_def)
            result += self._indent + self.add_columns(a_table_def)
            result += self._indent + self.related_views(a_table_def)
            result += (
                "\nappbuilder.add_view(\n"
                + self._indent
                + self._indent
                + class_name
                + ", "
                + '"'
                + table_name
                + ' List", '
                + 'icon="fa-folder-open-o", category="Menu")\n'
            )
            return result + "\n\n"

    def list_columns(self, a_table_def: MetaDataTable) -> str:
        """
            Generate list_columns = [...]

            These must be children first, so "related_views" compile.\n
            We therefore recurse for children first.

            Parameters
                argument1 a_table_def - TableModelInstance

            Returns
                string class and add_view for given table.
        """
        return self.gen_columns(a_table_def, "list_columns = [", 2, 4)

    def show_columns(self, a_table_def: MetaDataTable):
        return self.gen_columns(a_table_def, "show_columns = [", 99, 999)

    def edit_columns(self, a_table_def: MetaDataTable):
        return self.gen_columns(a_table_def, "edit_columns = [", 99, 999)

    def add_columns(self, a_table_def: MetaDataTable):
        return self.gen_columns(a_table_def, "add_columns = [", 99, 999)

    def gen_columns(self, a_table_def: MetaDataTable,
                    a_view_type: int, a_max_joins: int, a_max_columns: int):
        """
        Generates statements like:

            list_columns =["Id", "Product.ProductName", ... "Id"]

            This is *not* simply a list of columms:
                1. favorite column first,
                2. then join (parent) columns, with predictive joins
                3. and id fields at the end.

            Parameters
                argument1 a_table_def - TableModelInstance
                argument2 a_view_type - str like "list_columns = ["
                argument3 a_max_joins - int max joins (list is smaller)
                argument4 a_max_fields - int how many columns (list smaller)

            Returns
                string like list_columns =["Name", "Parent.Name", ... "Id"]
        """
        result = a_view_type
        columns = a_table_def.columns
        id_column_names = set()
        processed_column_names = set()
        result += ""
        if a_table_def.name == "Territory":
            log.debug("Territory reached")

        favorite_column_name = self.favorite_column_name(a_table_def)
        column_count = 1
        result += '"' + favorite_column_name + '"'
        processed_column_names.add(favorite_column_name)

        predictive_joins = self.predictive_join_columns(a_table_def)
        if (
            "list" in a_view_type or "show" in a_view_type
        ):  # alert - prevent fab key errors!
            for each_join_column in predictive_joins:
                column_count += 1
                if column_count > 1:
                    result += ", "
                result += '"' + each_join_column + '"'
                if column_count > a_max_joins:
                    break
        for each_column in columns:
            if each_column.name in processed_column_names:
                continue
            if "id" in each_column.name.lower():  # ids are boring - do at end
                id_column_names.add(each_column.name)
                continue
            column_count += 1
            if column_count > a_max_columns:  # - Todo - make external
                break
            if column_count > 1:
                result += ", "
            result += '"' + each_column.name + '"'
        for each_id_column_name in id_column_names:
            column_count += 1
            if column_count > 1:
                result += ", "
            result += '"' + each_id_column_name + '"'
        result += "]\n"
        return result

    def predictive_join_columns(self, a_table_def: MetaDataTable) -> set:
        """
        Generates set of predictive join column name:

            (Parent1.FavoriteColumn, Parent2.FavoriteColumn, ...)

            Parameters
                argument1 a_table_def - TableModelInstance

            Returns
                set of col names (such Product.ProductName for OrderDetail)
        """
        result = set()
        foreign_keys = a_table_def.foreign_keys
        if a_table_def.name == "OrderDetail":  # for debug
            log.debug("predictive_joins for: " + a_table_def.name)
        for each_foreign_key in foreign_keys:
            each_parent_name = each_foreign_key.target_fullname
            loc_dot = each_parent_name.index(".")
            each_parent_name = each_parent_name[0:loc_dot]
            each_parent = a_table_def.metadata.tables[each_parent_name]
            favorite_column_name = self.favorite_column_name(each_parent)
            result.add(each_parent_name + "." + favorite_column_name)
        return result

    def related_views(self, a_table_def: MetaDataTable) -> str:
        """
            Generates statments like
                related_views = ["Child1", "Child2"]

            Todo
                * are child roles required?
                    ** e.g., children = relationship("Child"
                * are multiple relationsips supported?
                    ** e.g., dept has worksFor / OnLoan Emps
                * are circular relationships supported?
                    ** e.g., dept has emps, emp has mgr

            Parameters
                argument1 a_table_def - TableModelInstance

            Returns
                str like related_views = ["Child1", "Child2"]
        """
        result = "related_views = ["
        related_count = 0
        child_list = self.find_child_list(a_table_def)
        for each_child in child_list:
            related_count += 1
            if related_count > 1:
                result += ", "
            result += each_child.fullname + self.model_name(each_child)
        result += "]\n"
        return result

    def find_child_list(self, a_table_def: MetaDataTable) -> list:
        """
            Returns list of models w/ fKey to a_table_def

            Not super efficient
                pass entire table list for each table
                ok until very large schemas

            Parameters
                argument1 a_table_def - TableModelInstance

            Returns
                list of models w/ fKey to each_table
        """
        child_list = []
        all_tables = a_table_def.metadata.tables
        for each_possible_child_tuple in all_tables.items():
            each_possible_child = each_possible_child_tuple[1]
            parents = each_possible_child.foreign_keys
            # if (a_table_def.name == "Customer" and
            #   each_possible_child.name == "Order"):
            #    print (a_table_def)
            for each_parent in parents:
                each_parent_name = each_parent.target_fullname
                loc_dot = each_parent_name.index(".")
                each_parent_name = each_parent_name[0:loc_dot]
                if each_parent_name == a_table_def.name:
                    child_list.append(each_possible_child)
        return child_list

    def model_name(self, a_table_name: str):  # override as req'd
        """
            returns view model_name for a_table_name, defaulted to "ModelView"

            intended for subclass override, for custom views

            Parameters
                argument1 a_table_name - str

            Returns
                view model_name for a_table_name, defaulted to "ModelView"
        """
        return "ModelView"

    def favorite_column_name(self, a_table_def: MetaDataTable) -> str:
        """
            returns string of first column that is...
                named <favorite_name> (default to "name"), else
                containing <favorite_name>, else
                (or first column)

            Parameters
                argument1 a_table_name - str

            Returns
                string of column name that is favorite (e.g., first in list)
        """
        favorite_names = self.favorite_name()
        for each_favorite_name in favorite_names:
            columns = a_table_def.columns
            for each_column in columns:
                col_name = each_column.name.lower()
                if col_name == each_favorite_name:
                    return each_column.name
            for each_column in columns:
                col_name = each_column.name.lower()
                if each_favorite_name in col_name:
                    return each_column.name
        for each_column in columns:  # no favorites, just return 1st
            return each_column.name

    def favorite_name(self) -> str:
        """
            returns array of substrings used to find favorite column name

            override per language, db conventions

            eg,
                name in English
                nom in French
        """
        return ["nom", "description"]

    def process_module_end(self, a_metadata_tables: MetaData) -> str:
        """
            returns the last few lines

            comments - # tables etc
        """
        result = (
            "#  "
            + str(len(a_metadata_tables))
            + " table(s) in model, "
            + str(self.num_pages_generated)
            + " page(s) generated\n\n"
        )
        return result
