# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    'default':  {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'likethat',
        'USER': 'root',
        'PASSWORD': 'qburst'
    }
}