from django.http import Http404

from narcissus.utils.http import JSONResponse


class AjaxMixin(object):
    """
    A mixin that can be used for Ajax-only views.  It checks to make sure that
    the request is Ajax and returns a JSON response.
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        else:
            return super(AjaxMixin, self).dispatch(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return JSONResponse(context, **response_kwargs)


class AjaxModelFormMixin(AjaxMixin):
    """
    Appropriately handle forms for Ajax-only views.  Designed to be used along
    with the ModelFormMixin, or views like BaseCreateView.
    """

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response({}, success=True)

    def form_invalid(self, form):
        return self.render_to_response({'errors': form.errors}, success=False)
