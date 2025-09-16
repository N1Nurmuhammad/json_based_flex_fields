from django.db import models


class ContentTypeModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    json_schema = models.JSONField(default=dict)
    ui_schema = models.JSONField(default=dict, blank=True)

    def save(self, *args, **kwargs):
        if not isinstance(self.json_schema, dict) or not self.json_schema:
            self.json_schema = {"type": "object", "properties": {}}
        # if self.json_schema.get("type") == "object" and not any(
        #         k in self.json_schema for k in ("properties", "oneOf", "anyOf", "allOf", "keys", "additionalProperties")
        # ):
        #     self.json_schema["properties"] = {}
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
