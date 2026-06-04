from functools import wraps
import random
def retry_on_fail(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception:
            print("Ошибка, пробуем еще раз...")
            for i in range(2):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    print("Ошибка, пробуем еще раз...")
                return "Сервер недоступен"
    return wrapped
@retry_on_fail
def connect_to_db():

    if random.randint(1,5) == 5:
        raise Exception("Connection timeout")
    else:
        return "Успешное подключение"
print(connect_to_db())