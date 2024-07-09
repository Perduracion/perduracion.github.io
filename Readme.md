## Manjares Cotidianos

**Proyectos Incluidos**

### API (JSON)

**Descripción:**

* Este directorio contiene el código para ejecutar la API que devuelve los JSon del contenido de la db.

**Estructura:**

```.
└── api_json
    ├── app
    │   ├── database.py
    │   ├── model.py
    │   └── view.py
    ├── Notebook
    │   └── test_request.ipynb
    ├── run.py
    └── src
        └── database
            └── manjar_psql.sql

```

**Detalles:**

* El directorio `src/database` contiene scripts para crear las bases de datos en PostgreSQL.
* El directorio `Notebook` contiene un Jupyter Notebook que utilizamos para registrar las respuestas de la API.

### API con Render Template

**Descripción:**

* Este directorio contiene el código para ejecutar la API que devuelve los renders de los templates, como lo planeamos originalmente.

**Estructura:**

```.
├── app  
│   ├── database.py  
│   ├── model.py  
│   └── view.py  
├── flask_app.py  
├── requirements.txt  
├── src  
│   ├── database  
│   │   ├── db_30-06-24.sql  
│   │   └── manjar.sql  
│   ├── requeriments.txt  
│   └── routes  
│       └── routes.py  
├── static  
│   ├── css  
│   │   ├── products.css  
│   │   └── style.css  
│   ├── img  
│   │   ├── bondiola.jpg  
│   │   ├── brownie.jpg  
│   │   ├── burguer.jpg  
│   │   ├── cafe.jpg  
│   │   ├── canelon.jpg  
│   │   ├── citric.jpg  
│   │   ├── coca-cola.jpg  
│   │   ├── ensalada.jpg  
│   │   ├── fanta.jpg  
│   │   ├── fatay.jpg  
│   │   ├── fruta.jpg  
│   │   ├── icons8-sombrero-de-chef-16.png  
│   │   ├── mila-frita.jpg  
│   │   ├── panq.jpg  
│   │   ├── panqueques.jpg  
│   │   ├── pasta.jpg  
│   │   ├── pizza.jpg  
│   │   ├── section.jpg  
│   │   ├── sorrentinos.jpg  
│   │   ├── speed.jpg  
│   │   ├── sprite.jpg  
│   │   ├── tacos.jpg  
│   │   ├── tarta.jpg  
│   │   ├── te.png  
│   │   └── torre.png  
│   ├── javascript  
│   │   ├── flash.js  
│   │   ├── index.js  
│   │   └── products.js  
│   └── swagger.json  
└── templates  
├── acerca.html  
├── cart.html  
├── contacto.html  
├── edit.html  
├── index.html  
├── login.html  
├── nuevo.html  
├── register.html  
└── sucursales.html  

```

**Detalles:**

* El directorio `src/database` contiene scripts para crear las bases de datos en PostgreSQL.
* El directorio `static` contiene archivos CSS, imágenes y JavaScript para los templates.
* El directorio `templates` contiene los HTML templates para la aplicación.
