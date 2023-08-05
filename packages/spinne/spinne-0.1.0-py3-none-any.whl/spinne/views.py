def render_html(fp: str):
    try:
        with open(fp, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {fp} does not exist")

def page_not_found():
    return "<h1>404</h1><br /><h2>the page you requested does not exist</h2>"