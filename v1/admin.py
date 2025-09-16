from django import forms
from django.contrib import admin
from django_jsonform.widgets import JSONFormWidget
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm

from v1.models import ContentTypeModel, ContentItemModel, MediaFileModel


class ContentItemAdminForm(TranslatableModelForm):
    class Meta:
        model = ContentItemModel
        fields = ("type", "slug", "status", "data")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        safe_fallback = {"type": "object", "properties": {}}
        ct = getattr(self.instance, "type", None)
        schema = getattr(ct, "json_schema", None) or safe_fallback
        if "data" in self.fields:
            self.fields["data"].widget = JSONFormWidget(schema=schema)


@admin.register(ContentItemModel)
class ContentItemAdmin(TranslatableAdmin):
    form = ContentItemAdminForm

    list_display = ("slug", "type", "status", "updated_at")
    list_filter = ("type", "status")
    search_fields = ("slug",)

    fieldsets = (
        ("Базовое", {"fields": ("type", "slug", "status")}),
        ("Контент (по языкам)", {"fields": ("data",)}),
    )


class ContentTypeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields["json_schema"].widget = forms.Textarea(attrs={"rows": 12})
            form.base_fields["ui_schema"].widget = forms.Textarea(attrs={"rows": 6})
            form.base_fields["json_schema"].initial = {
                "type": "object",
                "properties": {}
            }
            form.base_fields["ui_schema"].initial = {}
        return form


admin.site.register(ContentTypeModel, ContentTypeAdmin)


@admin.register(MediaFileModel)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "title", "uploaded_at")
    search_fields = ("title", "file")
