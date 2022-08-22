from django.urls import path , include
from . import views



urlpatterns =[

    # path('', views.member, name='members'),
    path('', views.MemberCreateView.as_view(), name='members'),
    path('edit/<int:id>', views.MemberEditView.as_view(), name='memberedit'),
    path('delete/<int:id>', views.MemberDeleteView.as_view(), name='memberdelete'),
  
 
]