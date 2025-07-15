INSTALLED_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib,contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book_store.apps.BookStoreConfig',
]

DATABASES = {
'default' : {
'ENGINE' : 'django.db.backends.mysql',
'NAME' : 'Product.sql',
'USER' : 'root',
'PASSWORD' : 'Dee99_Christelle#6',
'HOST' : 'localhost',
'PORT' : '8000',
}
}
