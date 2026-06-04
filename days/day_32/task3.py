from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        users = args[0]
        if users.get("role") != "admin":
            return "Access Denied"
        else:
            return func(*args, **kwargs)
    return wrapped
@require_admin
def delete_database(user):
    return "Database deleted"
print(delete_database({'name': 'Gleb', 'role': 'user'}))
print(delete_database({'name': 'Root', 'role': 'admin'}))
