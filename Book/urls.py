from django.urls import path, include
from . import views




urlpatterns =[
    # path('', views.book, name='books'),
    path('', views.BookAddView.as_view(), name='books'),
    path('edit/<int:id>', views.BookEditView.as_view(), name='bookedit'),
    path('delete/<int:id>', views.BookDeleteView.as_view(), name='bookdelete'),
    path('bookrentto/<int:id>', views.BookRentToView.as_view(), name='bookrentto'),
        
    path('transaction', views.TransactionView.as_view(), name='transaction'),
    path('transaction/<int:id>', views.ReturnView.as_view(), name='return')
]   
