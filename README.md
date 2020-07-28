# fab_nw
Work in Progress - Generate Flask Application Builder views file - 1 page (with related) for each table in the model.

This is a fab project for nw (sqllite).  It includes __build_views__, which can generate a `view.py` multi-page/multi-table app.


## Key Features

1. Generate `views.py` with 1 class per (not ab_) table

    a. "Favorite" fields (contains name) first

    b. Numeric keyfields last

2. With Referenced for master/detail (e.g., Order before Customer)

    a. Generated child views first

3. Predictive Joins (e.g, ProductName on Order+OrderDetail

    a. Note - *not* generated for edit/show, else you get fab "key errors"



## Install

open VSCode, and clone this repo

In VSCode Python Debug Console:

```
virtualenv venv
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```



## Generate

Then, open the file `build_views_file.py`, and run it (e.g, under the debugger).

Copy the console output over the `app/views.py` file


## Run
```
cd nw
export FLASK_APP=app
flask run
```



## Explore

The main code is `buid_views/build_views_base.py`.

Overrides for customization are in `build_views/build_views.py`, which is invoked by `build_views_file.py`

## Screenshot
    
![image](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)
