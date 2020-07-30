# fab_nw
Generates Flask Application Builder `views.py` file - to build a __multi-page__ app (1 page per table) of __multi-table__ pages (includes `related_views` for related child data). 

This is a fab project for a sqlite version northwind (nw). The project contains the __Fab Views Gen__ code (work in progress - see Explore, below), along with the nw project for illustration and testing.


## Background
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder) provides a rapid means for building web pages for database apps, based on Python and Flask ([QuickStart here](https://sites.google.com/view/app-logic-server/python-fab)).

FAB inputs are a `models.py` file, and a `views.py` file.  You can build models with tools like [sqlacodegen](https://www.google.com/url?q=https%3A%2F%2Fpypi.org%2Fproject%2Fsqlacodegen%2F&sa=D&sntz=1&usg=AFQjCNHZ3ERjfnSO8MA8V20gzLjfeBaIxw).

The `view.py` file consists of segments like this, one for each page:
```
class OrderModelView(ModelView):
   datamodel = SQLAInterface(Order)
   list_columns = ["ShipName", "Customer.CompanyName", ... "EmployeeId", "CustomerId"]
   show_columns = ["ShipName", "Customer.CompanyName", "OrderDate", ... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
   edit_columns = ["ShipName", "OrderDate",... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
   add_columns = ["ShipName", "OrderDate", ... "ShipCountry", "Id", "EmployeeId", "CustomerId"]
   related_views = [OrderDetailModelView]

appbuilder.add_view(
      OrderModelView, "Order List", icon="fa-folder-open-o", category="Menu")
```


This project seeks to generate this file from the model, to save time and reduce learning curve.

## Key Features

1. Generate `views.py` with 1 class per (not ab_) table

    a. "Favorite" field (called "name", or contains "name") first
          
          Eg, List of Products - ProductName is more interesting than ProductId, so show it first
    
    b. Join Fields (join in parents' favorite field)
          
          Eg, List of Order + OrderDetails: show ProductName (not id)

    b. Numeric keyfields last

2. With Referenced for master/detail (e.g., Order before Customer)

    a. Generated child views first

3. Predictive Joins (e.g, ProductName on Order+OrderDetail

    a. Note - *not* generated for edit/show, else you get fab "key errors"



## Install

### Pre Reqs

To get started, you will need:

* Python3: run the windows installer; on mac/Unix, consider [using brew](https://opensource.com/article/19/5/python-3-default-mac#what-to-do)
* virtualenv - see [here](https://www.google.com/url?q=https%3A%2F%2Fpackaging.python.org%2Fguides%2Finstalling-using-pip-and-virtual-environments%2F%23creating-a-virtual-environment&sa=D&sntz=1&usg=AFQjCNEu-ZbYfqRMjNQ0D0DqU1mhFpDYmw)  (e.g.,  `pip install virtualenv`)


### Project Installation
open VSCode, and clone this repo.

In VSCode Python Debug Console:

```
virtualenv venv
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```

Note: Windows Powershell requires privileges as described [here](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershel)


## Generate

Then, in VSCode, open the file `fab_views_gen_run.py`, and run it (e.g, under the debugger) using the launch config `FAB Views Gen Run`.

Copy the console output over the `app/views.py` file.


## Run
```
cd nw
export FLASK_APP=app
flask run
```



## Explore

The main code is `fab_views_gen/fab_views_gen_base.py`.

For customizations, it is extended by its subclass `fab_views_gen/fab_views_gen.py`, which is invoked by `fab_views_gen_run.py`

## Screenshot
    
![image](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)
