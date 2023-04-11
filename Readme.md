## The Python Requirements File

Python requirements files are a great way to keep track of the Python modules. It is a simple text file that saves a list of the modules and packages required by your project. By creating a Python `requirements.txt` file, you save yourself the hassle of having to track down and install all the required modules manually.

### Generate a Python requirements.txt file directly from the command line with:
```commandline
pip freeze > requirements.txt
```

### Installing Python Packages From a Requirements File
```commandline
pip install -r requirements.txt
```

## Command lines for the Django 
```commandline
python3 -m django --version
django-admin startproject mysite
python3 manage.py runserver
python3 manage.py migrate
python3 manage.py startapp openai
```

## How to Maintain a Python Requirements File
1. Output a list of outdated packages with `pip3 list --outdated`
2. Upgrade the required package with `pip3 install -U PackageName`
3. It is also possible to upgrade everything with `pip3 install -U -r requirements.txt`
4. Check to see if all the tests pass.
5. Run `pip freeze > requirements.txt` to update the Python requirements file
6. Run `git commit` and `git push` to the production branch
7. If you need to check for missing dependencies, you can do so with the following command: `python3 -m pip check`

## How to Create Python Requirements File After Development
While it is possible to create it manually, it is a good practice to use the `pipreqs` module. It is used to scan your `imports` and build a Python requirements file for you.

- Install by `pip install pipreqs`
- Running pipreqs in the command line generates a requirements.txt file automatically: `pipreqs /home/project/location`

## Resources for the project:
- [Youtube Video](https://www.youtube.com/watch?v=HGOBQPFzWKo)