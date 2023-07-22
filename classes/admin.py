from django.contrib import admin

from .models import Classes  # , Day


# class ChoiceInline(admin.StackedInline):
#     model = Day
#     extra = 3


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('class_pub_datetime',)
    fieldsets = [
        ('User', {'fields': ['user']},),
        (None, {'fields': ['class_name']},),
        (None, {'fields': ['class_faculty']},),
        (None, {'fields': ['class_url']},),
        (None, {'fields': ['class_time']},),
        ('Days', {'fields': ['Monday']},),
        (None, {'fields': ['Tuesday']},),
        (None, {'fields': ['Wednesday']},),
        (None, {'fields': ['Thursday']},),
        (None, {'fields': ['Friday']},),
        (None, {'fields': ['Saturday']},),
        (None, {'fields': ['Sunday']},),
        ('Published on', {'fields': [
         'class_pub_datetime']},),
    ]
    # inlines = [ChoiceInline]

    list_display = ('class_name', 'is_active', 'user', 'id')

    class Meta:
        verbose_name_plural = "classes"


admin.site.register(Classes, QuestionAdmin)
