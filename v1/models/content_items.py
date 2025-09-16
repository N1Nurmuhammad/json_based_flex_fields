from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from v1.models import ContentTypeModel


class ContentItemStatusChoices(models.IntegerChoices):
    DRAFT = 0, "Draft"
    PUBLISHED = 1, "Published"
    # scheduled = 2, "Scheduled"


class ContentItemLanguageChoices(models.TextChoices):
    UZ = "uz", "Uzbek"
    EN = "en", "English"
    RU = "ru", "Russian"


class ContentItemModel(TranslatableModel):
    type = models.ForeignKey(ContentTypeModel, on_delete=models.PROTECT, related_name="items")
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=ContentItemStatusChoices.choices, default=ContentItemStatusChoices.DRAFT)
    lang = models.CharField(max_length=2, choices=ContentItemLanguageChoices.choices,
                            default=ContentItemLanguageChoices.RU)
    # data = models.JSONField(default=dict, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    translations = TranslatedFields(
        data = models.JSONField(default=dict, blank=True, null=True)
    )
    # published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["type", "status", "lang", "updated_at"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return f"{self.type}:{self.slug}"
