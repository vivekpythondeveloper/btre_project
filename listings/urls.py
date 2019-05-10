from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='listings'),
    path('<int:listing_id>', views.listing,name='listing'),
    path('search', views.search,name='search'),
    path('make_query',views.make_query,name='make_query')
]
