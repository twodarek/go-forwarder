import models

class Permissions:


    @staticmethod
    def canWrite(user):
        user_perms = Permissions._getPermissions(user)
        try:
            return user_perms.auth_write
        except AttributeError:
            return False

    @staticmethod
    def canRead(user):
        user_perms = Permissions._getPermissions(user)
        try:
            return user_perms.auth_read
        except AttributeError:
            return False

    @staticmethod
    def canAdmin(user):
        user_perms = Permissions._getPermissions(user)
        try:
            return user_perms.auth_admin
        except AttributeError:
            return False

    @staticmethod
    def canAny(user):
        user_perms = Permissions._getPermissions(user)
        try:
            return (user_perms.auth_admin and user_perms.auth_write and user_perms.auth_read)
        except AttributeError:
            return False

    @staticmethod
    def canWriteOrAdmin(user):
        user_perms = Permissions._getPermissions(user)
        try:
            return (user_perms.auth_admin and user_perms.auth_write)
        except AttributeError:
            return False


    @staticmethod
    def _getPermissions(user):
        return models.Authorized_User.query(models.Authorized_User.user == user).get()

