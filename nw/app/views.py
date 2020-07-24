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
   list_columns = ["CategoryName", "Description"]
   show_columns = ["CategoryName", "Description", "Id"]





class CustomerModelView(ModelView):
   datamodel = SQLAInterface(Customer)
   list_columns = ["CompanyName", "ContactName", "ContactTitle", "Address"]
   show_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "Id"]





class OrderModelView(ModelView):
   datamodel = SQLAInterface(Order)
   list_columns = ["CustomerId", "EmployeeId", "OrderDate", "RequiredDate"]
   show_columns = ["CustomerId", "EmployeeId", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "Id"]





class OrderDetailModelView(ModelView):
   datamodel = SQLAInterface(OrderDetail)
   list_columns = ["OrderId", "ProductId", "UnitPrice", "Quantity"]
   show_columns = ["OrderId", "ProductId", "UnitPrice", "Quantity", "Discount", "Id"]





class ProductModelView(ModelView):
   datamodel = SQLAInterface(Product)
   list_columns = ["ProductName", "SupplierId", "CategoryId", "QuantityPerUnit"]
   show_columns = ["ProductName", "SupplierId", "CategoryId", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "Id"]


#  13 table(s) in model, 5 page(s) generated
