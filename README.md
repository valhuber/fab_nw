# fab_nw
Work in Progress - Generate Flask Application Builder `views.py` file - to build a multi-page app (1 page per table) of multi-table pages (includes 'references' for related child data). 

This is a fab project for nw (sqllite). It contains the generation code (see Explore, below), along with the nw project for illustration and testing.


## Background
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder) provides a rapid means for building web pages for database apps, based on Python and Flask ([QuickStart here](https://sites.google.com/view/app-logic-server/python-fab)).

FAB requires that you build a `views.py` file.  This project seeks generated this file from the model, to save time and reduce learning curve.

## Key Features

1. Generate `views.py` with 1 class per (not ab_) table

    a. "Favorite" fields (contains name) first

    b. Numeric keyfields last

2. With Referenced for master/detail (e.g., Order before Customer)

    a. Generated child views first

3. Predictive Joins (e.g, ProductName on Order+OrderDetail

    a. Note - *not* generated for edit/show, else you get fab "key errors"



## Install

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

Then, in VSCode, open the file `build_views_file.py`, and run it (e.g, under the debugger).

Copy the console output over the `app/views.py` file


## Run
```
cd nw
export FLASK_APP=app
flask run
```



## Explore

The main code is `build_views/build_views_base.py`.

Overrides for customization are in `build_views/build_views.py`, which is invoked by `build_views_file.py`

## Screenshot
    
![image](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)
