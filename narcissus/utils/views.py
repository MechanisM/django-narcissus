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
    
    def render_to_response(self, context, **response_kwargs):
        """Remove the form from the context, and add any form errors"""
        form = context.pop('form')
        if form.errors:
            context['errors'] = form.errors
            response_kwargs['success'] = False
        return super(AjaxFormMixin, self).render_to_response(
            context, **response_kwargs)
