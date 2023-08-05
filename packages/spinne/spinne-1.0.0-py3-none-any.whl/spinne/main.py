main = """from spinne import Spinne, page_not_found

# import views:
import index

app = Spinne("site")

@app.render
def main(route):
    if route == "index" or "": # you can use any route you'd like
        return index.index()
    else:
        return pageNotFound()

app.run()"""