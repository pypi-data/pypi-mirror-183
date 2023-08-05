main = """from spinne import Spinne, pageNotFound
import index

app = Spinne("site")

@app.render
def main(route):
    print(route)
    if route == "test":
        return index.index()
    else:
        return pageNotFound()

app.run()"""