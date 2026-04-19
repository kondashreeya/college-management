from django.urls import path
from app1.views import teacher,teacher_update,teacher_delete,student_create,student_update,student_delete,reg,login1,home,department_delete,department_create,department_update
urlpatterns = [
    
   path("",reg,name='reg1'),
   path("log/",login1,name='LOG1'),
   path("home1/",home,name='HOME'),
   path("dep/", department_create.as_view(), name='Dep'),        # main page (form + list)
   path("edit/<int:id>/", department_update.as_view(), name='edit2'),
   path("del3/<int:id>/", department_delete.as_view(), name='delete2'), # delete
   path("Teach/", teacher.as_view(), name='TEACH'),
   path("up/<int:id>/", teacher_update.as_view(), name='update'),
   path("del/<int:id>/", teacher_delete.as_view(), name='delete'),
   path("stdu/", student_create.as_view(), name="STU"),
    path("up1/<int:id>/", student_update.as_view(), name='update1'),
    path("del1/<int:id>/", student_delete.as_view(), name='delete1'),
]