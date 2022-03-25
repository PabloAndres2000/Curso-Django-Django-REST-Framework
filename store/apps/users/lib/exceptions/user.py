class CantCreateUser(BaseException):
    pass


class CantUpdateUser(BaseException):
    pass


class CantUpdateUserStatus(CantUpdateUser):
    pass
