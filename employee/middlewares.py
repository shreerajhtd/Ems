class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    # One time configuration and initialization

    def __call__(self, request):
        """
        code to be executed for each request before the view ( and later middleware) are called.
        """
        response = self.get_response(request)

        """
        Code to be executed for each request/response after the view is called.
        """
        return response

    # def process_view(self, request, view_func, *view_args, **view_kwargs):
    #     """
    #     called just before Django calls the view.
    #     Return either none or HttpResponse
    #     but if it return HttpResponse then next middleware will not be called and the view will not be executed
    #     """
        if request.user.is_authenticated:
            request.role = None
            groups = request.user.groups.all()
            if groups:
                request.role = groups[0].name

    # def process_exception(self, request, exception):
