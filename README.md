# Random Movie Microservicio

## Descripción

**Random Movie** es un componente de la arquitectura de microservicios de la aplicación web **DCICFLIX**, desarrollada en **React**. Su función principal es ofrecer a los usuarios una selección aleatoria de películas, enriqueciendo su experiencia al explorar contenido.

Este microservicio fue desarrollado como parte del curso **Tópicos Avanzados de Desarrollo Web** de la **Universidad Nacional del Sur**, con el objetivo de integrarse eficientemente en una arquitectura de microservicios. Gracias a esta integración, **DCICFLIX** permite a los usuarios acceder de manera ágil y sencilla a información sobre películas, mejorando la usabilidad y rendimiento de la plataforma.


## Funcionalidades

- **Consumo de Base de Datos**: Este microservicio consume la base de datos **[The Movie Database](https://www.themoviedb.org/)** para obtener información detallada sobre las películas.
- **Integración con Microservicios**:
  - **Likes**: Obtiene información sobre las personas a las que les gustó una película.
  - **Precio**: Proporciona el precio y la moneda de una película.

## Despliegue

Este microservicio está desplegado en Render y se puede acceder a través del siguiente enlace: [Random Movie en Render](https://random-movie-1vcv.onrender.com)


## Tecnologías utilizadas

- Python 3.*+
- FastAPI
- Requests
- Uvicorn
- Docker

## Instalación y ejecución

1. Clona el repositorio:
    ```bash
    git clone "https://github.com/francoleon08/random-movie.git"
    cd random-movie
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python3 -m venv venv    
    ```

3. Activa el entorno virtual:

    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Ejecución de la aplicación:
    ```bash
    uvicorn main:app --reload
    ```

## Instalación y ejecución con Docker

1. Construye la imagen de Docker:
    ```bash
    docker build -t random-movie .
    ```
2. Ejecuta el contenedor de Docker:
    ```bash
    docker run -d -p 80:80 random-movie
    ```
3. Accede al microservicio en `http://localhost:80`.


## Autores

- [Franco Leon]("https://github.com/francoleon08")
- [Manuel Lagos]("https://github.com/lagosmanuel")
