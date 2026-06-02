def update_user_profile(user_id, **fields):
    allowed_fields = {"email", "status", "role"}

    for field in fields:
        if field not in allowed_fields:
            print(f"Ошибка: Изменение поля {field} запрещено!")
            return
    updates = [f"{k} на {v}" for k, v in fields.items()]
    print(f"Пользователь {user_id} обновлен: " + ", ".join(updates))