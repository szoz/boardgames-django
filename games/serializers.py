from django.db.models import Model


def simple_model_serializer(instance: Model) -> dict:
    """Return dict with all `public` attributes of given model instance."""
    return {key: value for key, value in instance.__dict__.items() if not key.startswith("_")}
