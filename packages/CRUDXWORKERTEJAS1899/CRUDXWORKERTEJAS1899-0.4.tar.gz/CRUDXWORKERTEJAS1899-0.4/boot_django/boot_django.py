import os
import django


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../CRUD"))


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'demo1',
                'USER': 'root',
                'PASSWORD': 'root'
            }
        },
        INSTALLED_APPS=[
            'crudapp'
       ]
    )

    django.setup()