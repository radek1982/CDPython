# pip **list**  

List installed packages, including editables.  

Packages are listed in a case-insensitive sorted order.

## Output

    DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
    pip (9.0.1)
    pkg-resources (0.0.0)
    pytz (2021.1)
    setuptools (39.0.1)
    sqlparse (0.4.1)

# deactivate

Deactivates the virtual environment

## Output

    (py3Env) pk@pk-XPS-15-7590:~/Desktop/DOJO/assignments/python_stack$ deactivate 
    pk@pk-XPS-15-7590:~/Desktop/DOJO/assignments/python_stack$ 

# pip3 list (with no virt env active)

Lists all pip3 packages **system wide**

## Output
    pk@pk-XPS-15-7590:~/Desktop/DOJO/assignments/python_stack$ pip3 list
    DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
    apt-clone (0.2.1)
    apturl (0.5.2)
    asn1crypto (0.24.0)
    beautifulsoup4 (4.6.0)
    Brlapi (0.6.6)
    certifi (2018.1.18)
    chardet (3.0.4)
    command-not-found (0.3)
    configobj (5.0.6)
    cryptography (2.1.4)
    ... (and many others)

# activate

Acitvates the given virtual env

## Output 
  pk@pk-XPS-15-7590:~/Desktop/DOJO/assignments/python_stack$ source my_environments/py3Env/bin/activate 
  
  **(py3Env)** pk@pk-XPS-15-7590:~/Desktop/DOJO/assignments/python_stack$ 


   

# pip install Django==2.2.4

Install the specific version of a package

*--no-cache-dir* - is used to ski caching of the package and download it fresh.
 
 ## Output
    python_stack$ pip install --no-cache-dir Django==2.2.4
    Collecting Django==2.2.4
    Downloading https://files.pythonhosted.org/packages/d6/57/66997ca6ef17d2d0f0ebcd860bc6778095ffee04077ca8985928175da358/Django-2.2.4-py3-none-any.whl (7.5MB)
        100% |████████████████████████████████| 7.5MB 120.6MB/s 
    Requirement already satisfied: sqlparse in ./my_environments/py3Env/lib/python3.6/site-packages (from Django==2.2.4)
    Requirement already satisfied: pytz in ./my_environments/py3Env/lib/python3.6/site-packages (from Django==2.2.4)
    Installing collected packages: Django
    Successfully installed Django-2.2.4

# pip freeze

Pip freeze lists installed packages in the requirements format. eg: package==version.
This is useful to install multiple packages at the correct versions using ``pip install -r requirements.txt``

# pip uninstall Django

Uninstalls django

# pip show Django

    Shows information about package
    (py3Env) pk@pk-XPS-15-7590:~/Desktop/DOJO/assignments/python_stack$ pip show Django
    Name: Django
    Version: 2.2.4
    Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
    Home-page: https://www.djangoproject.com/
    Author: Django Software Foundation
    Author-email: foundation@djangoproject.com
    License: BSD
    Location: /home/pk/Desktop/DOJO/assignments/python_stack/my_environments/py3Env/lib/python3.6/site-packages
    Requires: pytz, sqlparse

