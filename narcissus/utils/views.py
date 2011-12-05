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


class AjaxFormMixin(AjaxMixin):
    """Appropriately handle forms for Ajax-only views."""

    def form_valid(self, form):
        """Add any form errors, and flag success or failure."""
        context = self.get_context_data()
        success = True
        if form.errors:
            context['errors'] = form.errors
            success = False
        return super(AjaxFormMixin, self).render_to_response(context,
                                                             success=success)
