import os
import importlib
import re

def extract_function(urls_content, url):
    # urls = ast.literal_eval(urls_content)
    match = re.search(r"urls = (\[.+\])", urls_content)
    if not match:
        return False

    urls = eval(match.group(1))
    print(urls)
    for u in urls:
        if u[0] == url:
            return u[1]
    return False

def get_view(url, project_name):
    print("Still no problem")
    views_path = os.path.join(project_name, "urls.py")
    if not os.path.exists(views_path):
        return False
    
    with open(views_path, "r") as f:
        contents = f.read()
    print("Still no problem")
    class_name = extract_function(contents, url)

    views_module = importlib.import_module("{}.views".format(project_name))
    view_func = getattr(views_module, class_name)
    
    return view_func()


def handle_request(project_name, path, method, form):
    # Handle the root route
    print("No problem")
    response_body = get_view(path, project_name)

    if not response_body:
        return "HTTP/1.1 404 Not Found\nContent-Type: text/plain\nContent-Length: 9\n\nNot Found"

    return "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n{}".format(len(response_body), response_body)

