class CheckPermissionClass:

    action_without_login = {
        'POST': False,
        'GET': True,
        'DELETE': False
    }

    def __init__(self, request, method):
        self.method = method
        self.request = request

    def has_permission(self):
        if self.action_without_login[self.method] is False:
            if self.request.user.id is None:
                return False
        return True
