from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator

from narcissus.utils.http import JSONResponse


class LoginRequiredMixin(object):
    """A simple mixin that just applies the login_required decorator"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AjaxMixin(object):
    """
    A mixin that can be used for Ajax-only views.  It checks to make sure that
    the request is Ajax and returns a JSON response.
    """
    http_method_names = ['post']

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


class AjaxDeletionMixin(AjaxMixin):
    """Appropriately handle delete requests for Ajax-only views."""
    http_method_names = ['post', 'delete']

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return self.render_to_response({}, success=True)
