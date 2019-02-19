from django.contrib import admin
from .models import Movimiento

class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('id','created_by', )
    def save_model(self, request, obj, form, change):
        if obj.created_by is None:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'categoria':
            print(db_field.choices)
            print(self)
        return super().formfield_for_choice_field(db_field, request, **kwargs)

admin.site.register(Movimiento, MovimientoAdmin)
