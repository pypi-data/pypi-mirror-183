from setuptools import setup, find_packages
setup(name="CRUDXWORKERTEJAS1899",
      # version="0.1", # first version of code it will be fuction do()
      #version="0.2", # now i have changed the code and it will be now run (class Tejas for modified version of 1.0 to 2.0)
      # version="0.1", # due to error in program code we need to run setup command again and then pip isntall again the latest version
      # version="0.2",
      # version="0.3",
      version="0.4",
      description="This is django CRUD web application 2",
      long_description="This is django CRUD web application 2 contain Create Read,Update,Delete operations",
      long_description_content_type="text/markdown",
      author="wati",
      author_email = "wati@wati.com",
      # packages=['packagetejas'],

      install_requires=["asgiref==3.6.0",
                        "Django==4.1.4",
                        "django-crispy-forms==1.14.0",
                        "mssql-django==1.2",
                        "mysqlclient==2.1.1",
                        "pyodbc==4.0.35",
                        "pytz==2022.7",
                        "sqlparse==0.4.3",
                        "tzdata==2022.7",
                        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    package_dir={"": "."},
    packages = find_packages(where="."),
    python_requires=">=3.9",
    scripts=["manage.py"],
    )