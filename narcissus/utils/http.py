from django.conf import settings
from django.http import HttpResponse
from django.utils import simplejson as json


class JSONResponse(HttpResponse):
    """Return a JSON encoded HTTP response."""

    def __init__(self, context='', success=True, exception=None):
        """Encode the content as JSON using the context and details provided"""
        content_type = "application/json; charset=%s" % settings.DEFAULT_CHARSET
        self.success = success
        self.exception = exception
        super(JSONResponse, self).__init__(self.encode_context(context),
                                           content_type=content_type)

    def encode_context(self, context):
        """
        Add success and exception attributes as needed, and encode them along
        with the context as JSON.
        """
        context['success'] = self.success

        if self.exception is not None:
            context['success'] = False

            if hasattr(self.exception, 'message'):
                # If there is a 'message' attribute, format the exception.
                context['exception'] = '%s: %s' % (type(self.exception),
                                                   self.exception.message)
            else:
                # Otherwise, treat it as a string.
                context['exception'] = 'Error: %s' % self.exception

        # If in DEBUG mode, indent the JSON for readability.
        indent = settings.DEBUG and 2 or None
        return json.JSONEncoder(indent=indent).encode(context)
