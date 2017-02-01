class Folder(object):
    def __init__(self):
        self.files = {}

    def add_file(self, f):
        if f.name not in self.files:
            self.files[f.name] = f
        else:
            print("File already exists")

    def del_file(self, user, fname):
        if fname not in self.files:
            print("No such file")
            return
        if user != self.files[fname].owner:
            print("Access denied")
            return
        del self.files[fname]

    def __str__(self):
        s = ""
        s_files = sorted(self.files.values(), key=lambda x: ord(x.name[0]))
        for f in s_files:
            s += str(f)
        fsize = sum([f.size for f in self.files.values()])
        return "Folder contents\n{}{}\nFolder size: {} bytes".format("="*15, s, fsize)


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
        FILE_PERMISSIONS = "rwx"
        if mode not in FILE_PERMISSIONS:
            return

        if user != self.owner:
            print("Access denied")
            return

        if mode not in self.perm:
            self.perm += mode

    def disable_permission(self, user, mode):
        FILE_PERMISSIONS = "rwx"
        if mode not in FILE_PERMISSIONS:
            return
        if user != self.owner:
            print("Access denied")
            return

        if mode in self.perm:
            self.perm = self.perm.replace(mode, "")

    def __str__(self):
        return "\nFile: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner, self.perm, self.size)

    def get_permissions(self):
        if not self.perm:
            return "null"
        return "".join(sorted(self.perm))
