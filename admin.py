from django.contrib import admin

# Register your models here.
from .models import Company, Nav, EmptyPage, Galery, Promotion, Question

class NavAdmin(admin.ModelAdmin):
    list_display = ("name", "page_id")

class EmptyPageAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

class PromotionPageAdmin(admin.ModelAdmin):
    list_display = ("name", "from_price", "to_price", 'id', 'in_nav')

class GaleryPageAdmin(admin.ModelAdmin):
    list_display = ("name", 'id', 'in_nav')

class QuestionPageAdmin(admin.ModelAdmin):
    list_display = ("question", 'id', 'in_nav')

admin.site.register(Company)
admin.site.register(Nav, NavAdmin)
admin.site.register(EmptyPage, EmptyPageAdmin)
admin.site.register(Galery, GaleryPageAdmin)
admin.site.register(Promotion, PromotionPageAdmin)
admin.site.register(Question, QuestionPageAdmin)