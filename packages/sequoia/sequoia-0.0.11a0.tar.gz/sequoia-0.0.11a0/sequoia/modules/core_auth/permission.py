from sequoia.libs.auth import PermissionCheck


class AUTH_ME(PermissionCheck):
    allow = ["admin", "customer"]
