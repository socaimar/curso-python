import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4,5]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1> Hola soy la pagina de LRP"</h1>
        <p>Soy el parrafo de la LRP</p>             
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()