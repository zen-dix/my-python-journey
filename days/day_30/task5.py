def process_api_request(method, endpoint, *tags, **payloads):
    ans = ""
    if tags != ():
        ans = "("
        for tag in tags:
            ans += tag + "/"
        ans += ") "
    ans += method + endpoint
    if payloads != {}:
        ans += f" | Body: {payloads}"
    return ans
print(process_api_request("POST", "/v1/register", "auth", "user", email="gffsdaf@dev.io", age=28))
''' исправленное
def process_api_request(method, endpoint, *tags, **payloads):
   
    tags_str = f"({'/'.join(tags)}) " if tags else ""
    
    log = f"{tags_str}{method} {endpoint}"
    
    if payloads:
        log += f" | Body: {payloads}"
        
    return log'''