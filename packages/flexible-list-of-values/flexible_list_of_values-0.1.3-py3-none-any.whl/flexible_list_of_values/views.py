import logging

logger = logging.getLogger("flexible_list_of_values")


class LOVValuesViewRequestMixin(object):
    """
    CBV mixin which puts the request into the form kwargs.
    """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        # Update the existing form kwargs dict with the request.
        kwargs.update({"request": self.request})
        return kwargs