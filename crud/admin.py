from django.contrib import admin
from .models import Blog,Contacts
# Register your models here.
admin.site.site_header="Blog Application"
admin.site.site_title="Blog Admin"
admin.site.index_title="Blog Administration"

class BlogAdmin(admin.ModelAdmin):
    list_display = "__str__","title","subheading","description",
    fields = (("title","subheading",),"description",)
    list_editable = "title","subheading","description",
    search_fields = "title",
    


admin.site.register(Blog,BlogAdmin)
admin.site.register(Contacts)