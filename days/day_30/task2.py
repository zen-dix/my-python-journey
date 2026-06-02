def sanitize_headers(**headers):
    ans = {}
    for head in headers:
        if headers[head] != None and headers[head] != "":
            ans[head] = headers[head]
    return ans
print(sanitize_headers(Content_Type="application/json", Authorization=None, X_Test_Token=""))