from django.urls import path

from . import views
    
urlpatterns = [
    path('student',views.stuList.as_view()),
      path('studentDel/<int:pk>',views.stuDel.as_view()),
      path('teacher',views.teachList.as_view()),
      path('teachdel/<int:pk>',views.teachDel.as_view()),
      path('employee',views.empList.as_view()),
      path('empdel/<int:pk>',views.empDel.as_view()),
]