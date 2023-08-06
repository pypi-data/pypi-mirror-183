from typing import Type

from django.db.models import Model
from humps.main import decamelize
from nwon_baseline.typings import AnyDict
from rest_framework.serializers import Serializer


def dictionary_is_serialized_instance(
    instance: Model,
    serializer: Type[Serializer],
    response: AnyDict,
    decamelize_response: bool = True,
) -> bool:
    """
    Checks that a dictionary resembles the serialization of a model instance
    with a certain serializer.
    """

    compare_dict = decamelize(response) if decamelize_response else response
    return serializer(instance=instance).data == compare_dict


__all__ = ["dictionary_is_serialized_instance"]
