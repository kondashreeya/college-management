from django.contrib import admin
from app1.models import Department,Teachers,Students
class dep_admin(admin.ModelAdmin):
    list_display=['dep_id','dep_name']
    ordering=['dep_id']
admin.site.register(Department,dep_admin)
class teach_admin(admin.ModelAdmin):
    list_display=['teacher_id','teacher_name','teacher_mobile','department']
    ordering=['teacher_id']
admin.site.register(Teachers,teach_admin)
class std_admin(admin.ModelAdmin):
    list_display=['std_id','std_name','department']
    ordering=['std_id']
admin.site.register(Students,std_admin)
# Register your models here.