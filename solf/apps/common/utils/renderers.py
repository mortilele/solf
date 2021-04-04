from rest_framework.renderers import JSONRenderer


class JSONResponseRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = data
        if isinstance(data, dict):
            if data.get("code"):
                response_data = {
                    "code": data.pop("code"),
                    "message": data.pop("message", data),
                }

        response = super(JSONResponseRenderer, self).render(
            response_data, accepted_media_type, renderer_context
        )
        return response
