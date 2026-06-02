def show_env_config(**kwargs):
    for p in kwargs:
        print(f"[CONFIG] {p} => {kwargs[p]}")

show_env_config(debug=True, database="PostgreSQL", version="1.4.2")