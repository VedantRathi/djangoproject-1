from django.urls import path
from Books import views
urlpatterns= [
    path('insert-book',views.insertBook),
    path('view-books',views.viewBooks),
    path('save-book',views.insert),
    path('edit-book',views.editBook),
    path('delete-book',views.deleteBook),
    path('update',views.edit),
    path('search-book',views.searchBook),
    path('search',views.search),
    path('user-login',views.userLogin),
    path('user-logout',views.userLogout),
]
