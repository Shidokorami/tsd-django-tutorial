# Django ORM & DRF

## ORM

```python

# Single object (raises DoesNotExist if missing)
Model.objects.get(id=1)
Model.objects.get(last_name="Lucas")

# All rows
Model.objects.all()

# Filter
Model.objects.filter(num_field__gte=7.5)
Model.objects.filter(field__icontains="test")

# Exclude 
Model.objects.exclude(field=2017)

# Chaining
Model.objects.filter(rating__lt=8.0).exclude(release_year=2017)

# Ordering
# Descending
Model.objects.order_by("-field")
# Ascending
Model.objects.order_by("field")

# Limit
# Return only 3 first objects
Model.objects.order_by("-field")[:3]

# Count
Model.objects.all.count()

# Exists
Model.objects.filter(field="test").exists()
```

## Field lookups (`field__lookup`)

| Lookup | Meaning |
|--------|---------|
| `iexact` | case-insensitive equals |
| `contains` | substring |
| `icontains` | case-insensitive substring |
| `startswith` / `endswith` | prefix / suffix |
| `gt`, `gte`, `lt`, `lte` | comparisons |
| `in` | value in list |
| `range` | between |
| `isnull` | NULL check |
| `year`, `month`, `day` | on dates |

## Relations (ForeignKey)

```python
# Filter by related field
Model.objects.filter(parent_id=1)
Model.objects.filter(parent__field="Test")

## `select_related` vs `prefetch_related`

# select_related — JOIN for ForeignKey
rows = Model.objects.select_related("parent").all()
for row in rows:
    print(row.parent.last_name)

# prefetch_related — separate query for reverse FK / M2M
parents = ParentModel.objects.prefetch_related("models").all()
for p in parents:
    print(list(p.models.all()))
```

## `annotate`, `aggregate`, `distinct`

```python

ParentModel.objects.annotate(model_count=Count("models"))
ParentModel.objects.annotate(model_count=Count("models")).filter(model_count__gte=2)

Model.objects.aggregate(avg_rating=Avg("rating"))
Model.objects.filter(parent_id=1).aggregate(best=Max("rating"))

Model.objects.values("release_year").distinct()
```


---

## Django REST Framework

### Serializer (`ModelSerializer` base class)

```python
from rest_framework import serializers
from movies.models import Model


class ModelApiSerializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = Model
        fields = ["id", "name"]

    def get_custom_field(self, obj):
        return value
```

```python
serializer = ModelApiSerializer(row)
serializer = ModelApiSerializer(queryset, many=True)
serializer.data
```

### ViewSet

```python



class ModelApiViewSet(ViewSet):
    def list(self, request):
        queryset = Model.objects.all()
        serializer = ModelApiSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        row = get_object_or_404(Model, pk=pk)
        serializer = ModelApiSerializer(row)
        return Response(serializer.data)
```

| Method | HTTP | URL |
|--------|------|-----|
| `list` | GET | `/api/models/` |
| `retrieve` | GET | `/api/models/<pk>/` |

### Router

```python
from rest_framework.routers import DefaultRouter
from movies.views import ModelApiViewSet

router = DefaultRouter()
router.register("models", ModelApiViewSet, basename="model")
urlpatterns = router.urls
```


## Docker commands (this project)

```bash
docker compose up -d --build
docker compose run --rm app python manage.py migrate
docker compose run --rm app pytest movies/tests/test_task1.py -v
docker compose run --rm app python manage.py runserver 0.0.0.0:8000
```

**Codespaces:** run `python manage.py` / `pytest` directly (no `docker compose run --rm app` prefix).
