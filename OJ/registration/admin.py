from django.contrib import admin
from registration.models import Problem,Submission,TestCase,Result
 
# Register your models here.
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(TestCase)
admin.site.register(Result)