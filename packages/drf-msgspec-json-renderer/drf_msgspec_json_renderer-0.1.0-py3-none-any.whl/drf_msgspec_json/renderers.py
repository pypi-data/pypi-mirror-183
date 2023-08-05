import msgspec
from rest_framework.renderers import BaseRenderer


__all__ = ['MsgspecJSONRenderer', ]


class MsgspecJSONRenderer(BaseRenderer):
    media_type = 'application/json'
    format = 'json'
    ensure_ascii = True
    charset = None

    def render(self, data, *args, **kwargs):

        if data is None:
            return bytes()

        ret = msgspec.json.encode(data)
        return ret
