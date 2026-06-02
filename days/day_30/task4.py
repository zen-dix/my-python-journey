def build_sql_query(table, *columns, **filters):
    ans = "SELECT "
    if columns != ():
        for column in columns:
            ans += column + ", "
    else:
        ans += "* "
    ans += "FROM " + table + " WHERE "
    for filter in filters:
        ans += f"{filter} = '{filters[filter]}' AND"
    return ans[:-4]

sql2 = build_sql_query("products", category="books")
print(sql2)
''' исправленное def build_sql_query(table, *columns, **filters):
    # Если колонки переданы — клеим их через запятую, иначе берём '*'
    columns_str = ", ".join(columns) if columns else "*"
    query = f"SELECT {columns_str} FROM {table}"
    
    if filters:
        where_clauses = [f"{k} = '{v}'" for k, v in filters.items()]
        query += " WHERE " + " AND ".join(where_clauses)
        
    return query'''