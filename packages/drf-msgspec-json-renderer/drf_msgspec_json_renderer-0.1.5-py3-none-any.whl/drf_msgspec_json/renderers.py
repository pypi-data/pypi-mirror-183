import uuid
from decimal import Decimal
from typing import Any

import msgspec
from django.utils.functional import Promise
from rest_framework.renderers import BaseRenderer


__all__ = ['MsgspecJSONRenderer', ]

from rest_framework.settings import api_settings


class MsgspecJSONRenderer(BaseRenderer):
    media_type = 'application/json'
    format = 'json'
    ensure_ascii = True
    charset = None

    @staticmethod
    def default(obj: Any) -> Any:
        """
        When orjson doesn't recognize an object type for encode it passes
        that object to this function which then converts the object to its
        native Python equivalent.
        :param obj: Object of any type to be converted.
        :return: native python object
        """

        if isinstance(obj, dict):
            return dict(obj)
        elif isinstance(obj, list):
            return list(obj)
        elif isinstance(obj, Decimal):
            if api_settings.COERCE_DECIMAL_TO_STRING:
                return str(obj)
            else:
                return float(obj)
        elif isinstance(obj, (str, uuid.UUID, Promise)):
            return str(obj)
        elif hasattr(obj, "tolist"):
            return obj.tolist()
        elif hasattr(obj, "__iter__"):
            return list(item for item in obj)

    def render(self, data: Any, *args, **kwargs):
        if data is None:
            return bytes()
        return msgspec.json.encode(self.default(data))
