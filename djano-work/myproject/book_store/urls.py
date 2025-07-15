from django.contrib import admin/nfrom django.urls import include, path/nurlpatterns =  [
path('books/',include('book_store.urls')),
path('admin/', admin.site.urls),
]
