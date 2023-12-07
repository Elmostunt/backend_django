Repositorio para codigo backend Django web app

1.- Esto hay que clonarlo con:
git clone <url>

2.- compilaremos nuestra imagen docker dentro de nuestra imagen 
docker build -t <name-tag>:<version> .

3.- Con esto ejecutamos la imagen docker
docker run <name-tag>:<version>

Troubleshooting

1.- No se ve el mensaje de servidor 
Hay que añadir PYTHONUNBUFFERED = 1 en dockerfile

2.-Servidor no corre
Hay que configurar en el Dockerfile el comando 
python manage.py runserver 0.0.0.0:8000
