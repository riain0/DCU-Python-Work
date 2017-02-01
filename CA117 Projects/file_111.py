class File(object):

    FILE_PERMISSIONS = "rwx"

    def __init__(self, name, owner, size=0, perm=""):
        self.name = name
        self.owner = owner
        self.perm = perm
        self.size = size

    def has_access(self, user, permission):
        if user == self.owner:
            return "Access granted"

        if permission in self.perm:
            return "Access granted"

        else:
            return "Access denied"

    def enable_permission(self, user, mode):
        if mode not in self.FILE_PERMISSIONS:
            return

        if user != self.owner:
            print("Access denied")
            return

        if mode not in self.perm:
            self.perm += mode

    def disable_permission(self, user, mode):
        if mode not in self.FILE_PERMISSIONS:
            return

        if user != self.owner:
            print("Access denied")
            return

        if mode in self.perm:
            self.perm = self.perm.replace(mode, "")

    def __str__(self):
        return "File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner, self.perm, self.size)

    def get_permissions(self):
        if not self.perm:
            return "null"
        return "".join(sorted(self.perm))
