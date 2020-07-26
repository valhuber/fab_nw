# default view.py

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import *

# skip admin table: ab_permission
# skip admin table: ab_view_menu
# skip admin table: ab_permission_view_role
# skip admin table: ab_role
# skip admin table: ab_permission_view
# skip admin table: ab_user_role
# skip admin table: ab_user
# skip admin table: ab_register_user



class CategoryModelView(ModelView):
   datamodel = SQLAInterface(Category)
   list_columns = ["CategoryName", "Description", "Id"]
   show_columns = ["CategoryName", "Description", "Id"]
   edit_columns = ["CategoryName", "Description", "Id"]
   add_columns = ["CategoryName", "Description", "Id"]
   related_views = []

appbuilder.add_view(
      CategoryModelView, "Category List", icon="fa-folder-open-o", category="Menu")





class CustomerCustomerDemoModelView(ModelView):
   datamodel = SQLAInterface(CustomerCustomerDemo)
   list_columns = ["Id", "Customer.CompanyName", "Id", "CustomerTypeId"]
   show_columns = ["Id", "Customer.CompanyName", "Id", "CustomerTypeId"]
   edit_columns = ["CustomerTypeId", "Id"]
   add_columns = ["CustomerTypeId", "Id"]
   related_views = []

appbuilder.add_view(
      CustomerCustomerDemoModelView, "CustomerCustomerDemo List", icon="fa-folder-open-o", category="Menu")





class OrderDetailModelView(ModelView):
   datamodel = SQLAInterface(OrderDetail)
   list_columns = ["Id", "Order.ShipName", "Product.ProductName", "UnitPrice", "OrderId", "Id", "ProductId"]
   show_columns = ["Id", "Order.ShipName", "Product.ProductName", "UnitPrice", "Quantity", "Discount", "OrderId", "Id", "ProductId"]
   edit_columns = ["OrderId", "ProductId", "UnitPrice", "Quantity", "Discount", "Id"]
   add_columns = ["OrderId", "ProductId", "UnitPrice", "Quantity", "Discount", "Id"]
   related_views = []

appbuilder.add_view(
      OrderDetailModelView, "OrderDetail List", icon="fa-folder-open-o", category="Menu")





class OrderModelView(ModelView):
   datamodel = SQLAInterface(Order)
   list_columns = ["ShipName", "Customer.CompanyName", "OrderDate", "RequiredDate", "EmployeeId", "Id", "CustomerId"]
   show_columns = ["ShipName", "Customer.CompanyName", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "EmployeeId", "Id", "CustomerId"]
   edit_columns = ["CustomerId", "EmployeeId", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "Id"]
   add_columns = ["CustomerId", "EmployeeId", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "Id"]
   related_views = [OrderDetailModelView]

appbuilder.add_view(
      OrderModelView, "Order List", icon="fa-folder-open-o", category="Menu")





class CustomerModelView(ModelView):
   datamodel = SQLAInterface(Customer)
   list_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "Id"]
   show_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "Id"]
   edit_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "Id"]
   add_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "Id"]
   related_views = [CustomerCustomerDemoModelView, OrderModelView]

appbuilder.add_view(
      CustomerModelView, "Customer List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: CustomerCustomerDemo


class CustomerDemographicModelView(ModelView):
   datamodel = SQLAInterface(CustomerDemographic)
   list_columns = ["Id", "CustomerDesc", "Id"]
   show_columns = ["Id", "CustomerDesc", "Id"]
   edit_columns = ["CustomerDesc", "Id"]
   add_columns = ["CustomerDesc", "Id"]
   related_views = []

appbuilder.add_view(
      CustomerDemographicModelView, "CustomerDemographic List", icon="fa-folder-open-o", category="Menu")





class EmployeeTerritoryModelView(ModelView):
   datamodel = SQLAInterface(EmployeeTerritory)
   list_columns = ["Id", "Employee.LastName", "Territory.Id", "EmployeeId", "Id", "TerritoryId"]
   show_columns = ["Id", "Employee.LastName", "Territory.Id", "EmployeeId", "Id", "TerritoryId"]
   edit_columns = ["EmployeeId", "TerritoryId", "Id"]
   add_columns = ["EmployeeId", "TerritoryId", "Id"]
   related_views = []

appbuilder.add_view(
      EmployeeTerritoryModelView, "EmployeeTerritory List", icon="fa-folder-open-o", category="Menu")





class EmployeeModelView(ModelView):
   datamodel = SQLAInterface(Employee)
   list_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "Id"]
   show_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath", "Id"]
   edit_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath", "Id"]
   add_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath", "Id"]
   related_views = [EmployeeTerritoryModelView]

appbuilder.add_view(
      EmployeeModelView, "Employee List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: EmployeeTerritory# table already generated per recursion: Order# table already generated per recursion: OrderDetail# table already generated per recursion: OrderDetail


class ProductModelView(ModelView):
   datamodel = SQLAInterface(Product)
   list_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "Id", "CategoryId", "SupplierId"]
   show_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "Id", "CategoryId", "SupplierId"]
   edit_columns = ["ProductName", "SupplierId", "CategoryId", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "Id"]
   add_columns = ["ProductName", "SupplierId", "CategoryId", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "Id"]
   related_views = [OrderDetailModelView]

appbuilder.add_view(
      ProductModelView, "Product List", icon="fa-folder-open-o", category="Menu")





class RegionModelView(ModelView):
   datamodel = SQLAInterface(Region)
   list_columns = ["Id", "RegionDescription", "Id"]
   show_columns = ["Id", "RegionDescription", "Id"]
   edit_columns = ["RegionDescription", "Id"]
   add_columns = ["RegionDescription", "Id"]
   related_views = []

appbuilder.add_view(
      RegionModelView, "Region List", icon="fa-folder-open-o", category="Menu")





class ShipperModelView(ModelView):
   datamodel = SQLAInterface(Shipper)
   list_columns = ["CompanyName", "Phone", "Id"]
   show_columns = ["CompanyName", "Phone", "Id"]
   edit_columns = ["CompanyName", "Phone", "Id"]
   add_columns = ["CompanyName", "Phone", "Id"]
   related_views = []

appbuilder.add_view(
      ShipperModelView, "Shipper List", icon="fa-folder-open-o", category="Menu")





class SupplierModelView(ModelView):
   datamodel = SQLAInterface(Supplier)
   list_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "Id"]
   show_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage", "Id"]
   edit_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage", "Id"]
   add_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage", "Id"]
   related_views = []

appbuilder.add_view(
      SupplierModelView, "Supplier List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: EmployeeTerritory


class TerritoryModelView(ModelView):
   datamodel = SQLAInterface(Territory)
   list_columns = ["Id", "TerritoryDescription", "Id", "RegionId"]
   show_columns = ["Id", "TerritoryDescription", "Id", "RegionId"]
   edit_columns = ["TerritoryDescription", "RegionId", "Id"]
   add_columns = ["TerritoryDescription", "RegionId", "Id"]
   related_views = [EmployeeTerritoryModelView]

appbuilder.add_view(
      TerritoryModelView, "Territory List", icon="fa-folder-open-o", category="Menu")


#  21 table(s) in model, 13 page(s) generated