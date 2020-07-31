# default views.py, generated at: 2020-07-31 08:40:36.222987

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import *




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
   list_columns = ["Id", "Customer.CompanyName", "CustomerTypeId"]
   show_columns = ["Id", "Customer.CompanyName", "CustomerTypeId"]
   edit_columns = ["Id", "CustomerTypeId"]
   add_columns = ["Id", "CustomerTypeId"]
   related_views = []

appbuilder.add_view(
      CustomerCustomerDemoModelView, "CustomerCustomerDemo List", icon="fa-folder-open-o", category="Menu")





class OrderDetailModelView(ModelView):
   datamodel = SQLAInterface(OrderDetail)
   list_columns = ["Id", "Order.ShipName", "Product.ProductName", "UnitPrice", "ProductId", "OrderId"]
   show_columns = ["Id", "Order.ShipName", "Product.ProductName", "UnitPrice", "Quantity", "Discount", "ProductId", "OrderId"]
   edit_columns = ["Id", "UnitPrice", "Quantity", "Discount", "ProductId", "OrderId"]
   add_columns = ["Id", "UnitPrice", "Quantity", "Discount", "ProductId", "OrderId"]
   related_views = []

appbuilder.add_view(
      OrderDetailModelView, "OrderDetail List", icon="fa-folder-open-o", category="Menu")





class OrderModelView(ModelView):
   datamodel = SQLAInterface(Order)
   list_columns = ["ShipName", "Customer.CompanyName", "OrderDate", "RequiredDate", "CustomerId", "Id", "EmployeeId"]
   show_columns = ["ShipName", "Customer.CompanyName", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "CustomerId", "Id", "EmployeeId"]
   edit_columns = ["ShipName", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "CustomerId", "Id", "EmployeeId"]
   add_columns = ["ShipName", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "CustomerId", "Id", "EmployeeId"]
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
   list_columns = ["Id", "CustomerDesc"]
   show_columns = ["Id", "CustomerDesc"]
   edit_columns = ["Id", "CustomerDesc"]
   add_columns = ["Id", "CustomerDesc"]
   related_views = []

appbuilder.add_view(
      CustomerDemographicModelView, "CustomerDemographic List", icon="fa-folder-open-o", category="Menu")





class EmployeeTerritoryModelView(ModelView):
   datamodel = SQLAInterface(EmployeeTerritory)
   list_columns = ["Id", "Employee.LastName", "Territory.TerritoryDescription", "EmployeeId", "TerritoryId"]
   show_columns = ["Id", "Employee.LastName", "Territory.TerritoryDescription", "EmployeeId", "TerritoryId"]
   edit_columns = ["Id", "EmployeeId", "TerritoryId"]
   add_columns = ["Id", "EmployeeId", "TerritoryId"]
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


# table already generated per recursion: EmployeeTerritory# table already generated per recursion: EmployeeTerritory


class TerritoryModelView(ModelView):
   datamodel = SQLAInterface(Territory)
   list_columns = ["TerritoryDescription", "RegionId", "Id"]
   show_columns = ["TerritoryDescription", "RegionId", "Id"]
   edit_columns = ["TerritoryDescription", "RegionId", "Id"]
   add_columns = ["TerritoryDescription", "RegionId", "Id"]
   related_views = [EmployeeTerritoryModelView]

appbuilder.add_view(
      TerritoryModelView, "Territory List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: Order# table already generated per recursion: OrderDetail# table already generated per recursion: OrderDetail


class ProductModelView(ModelView):
   datamodel = SQLAInterface(Product)
   list_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "SupplierId", "Id", "CategoryId"]
   show_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "SupplierId", "Id", "CategoryId"]
   edit_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "SupplierId", "Id", "CategoryId"]
   add_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "SupplierId", "Id", "CategoryId"]
   related_views = [OrderDetailModelView]

appbuilder.add_view(
      ProductModelView, "Product List", icon="fa-folder-open-o", category="Menu")





class RegionModelView(ModelView):
   datamodel = SQLAInterface(Region)
   list_columns = ["RegionDescription", "Id"]
   show_columns = ["RegionDescription", "Id"]
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


# skip admin table: ab_permission
# skip admin table: ab_permission_view
# skip admin table: ab_view_menu
# skip admin table: ab_permission_view_role
# skip admin table: ab_role
# skip admin table: ab_register_user
# skip admin table: ab_user
# skip admin table: ab_user_role
#  21 table(s) in model, 13 page(s) generated