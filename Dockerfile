# Imagen base
FROM python:3.8.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la carpeta actual al directorio de trabajo
COPY . .

# Establece el comando por defecto para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "chatbot_v1_1.py"]  # Reemplaza "main.py" con el nombre de tu archivo principal

