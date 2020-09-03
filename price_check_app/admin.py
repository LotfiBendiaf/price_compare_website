from django.contrib import admin

from .models import Search


admin.site.site_header = "My Price Check"
admin.site.site_title = "My Price Check"
admin.site.index_title = "My Price Check Admin"

# Register your models here.
admin.site.register(Search)