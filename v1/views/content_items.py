from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response

from v1.models import ContentItemModel, ContentItemStatusChoices
from v1.serializers.content_items import ContentItemSerializer

LANG_CODES = {
    "uz": 0,
    "en": 1,
    "ru": 2,
}


@api_view(['GET'])
@cache_page(300)
def get_public_items(request, lang):
    public_items = ContentItemModel.objects.filter(status=ContentItemStatusChoices.PUBLISHED,
                                                   lang=LANG_CODES.get(lang, "ru"))
    serializer = ContentItemSerializer(public_items, many=True)
    return Response(serializer.data)

# class ItemFilter(filters.FilterSet):
#     type_name = filters.CharFilter(method="filter_type")
#     locale = filters.CharFilter(field_name="locale")
#
#     class Meta:
#         model = ContentItem
#         fields = ["locale", "status"]
#
#     def filter_type(self, qs, name, value):
#         return qs.filter(type__name=value)
#
#
# class PublicItems(viewsets.ReadOnlyModelViewSet):
#     serializer_class = ContentItemSerializer
#     permission_classes = [permissions.AllowAny]
#     filterset_class = ItemFilter
#
#     def get_queryset(self):
#         now = timezone.now().isoformat()
#         return (ContentItem.objects
#                 .select_related("type")
#                 .filter(Q(status="published") | Q(status="scheduled", data__published_at__lte=now))
#                 .order_by("-data__published_at", "-updated_at"))
#
#
# class ContentTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContentType
#         fields = ("id", "name", "json_schema", "ui_schema")
#
#
# class PublicTypes(viewsets.ReadOnlyModelViewSet):
#     queryset = ContentType.objects.all()
#     serializer_class = ContentTypeSerializer
#     permission_classes = [permissions.AllowAny]
