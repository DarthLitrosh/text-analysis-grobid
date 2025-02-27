# Análisis de Artículos Científicos en PDF

Este proyecto permite extraer información clave de artículos científicos en formato PDF utilizando Python. Analiza los documentos para obtener:

- **Abstracts (resúmenes)**
- **Cantidad de figuras en cada artículo**
- **Enlaces dentro del documento**
- **Nube de palabras basada en los abstracts**
- **Gráfico con el número de figuras por artículo**

## Instalación y Requisitos

### 1. Instalar Python
Este proyecto requiere **Python 3**. Para verificar si está instalado:

```bash
python3 --version
```

Si no está instalado, se puede obtener con Homebrew:

```bash
brew install python3
```

### 2. Instalar dependencias
Ejecutar el siguiente comando para instalar las librerías necesarias:

```bash
pip3 install pymupdf matplotlib wordcloud
```

## Estructura del Proyecto

```
OpenScience/
│── PdfAnalysis.py       # Script principal
│── README.md            # Documentación del proyecto
│── data/                # Carpeta donde colocar los PDFs
│── results/             # Carpeta donde se guardan los resultados
```

## Cómo Ejecutar el Análisis

### 1. Ubicarse en la carpeta del proyecto
Si el proyecto está en `~/OpenScience/`, abrir la terminal y ejecutar:

```bash
cd ~/OpenScience
```

### 2. Colocar los PDFs en `data/`
Asegurarse de que los archivos PDF estén dentro de la carpeta `data/`.
Si están en `Descargas/`, moverlos con:

```bash
mv ~/Descargas/*.pdf data/
```

### 3. Ejecutar el script
Para analizar los PDFs, ejecutar:

```bash
python3 PdfAnalysis.py
```

El script procesará los archivos y generará los resultados en `results/`.

## Resultados Generados

Después de ejecutar el script, revisar la carpeta `results/`:

### 1. `data.json`
Archivo JSON con la información extraída:

```json
[
  {
    "filename": "paper1.pdf",
    "abstract": "Resumen del artículo...",
    "figures_count": 3,
    "links": ["https://example.com"]
  }
]
```

### 2. `wordcloud.png`
Imagen con la nube de palabras generada a partir de los abstracts.
Abrir con:

```bash
open results/wordcloud.png
```

### 3. `figures_count.png`
Gráfico de barras con la cantidad de figuras por artículo.
Abrir con:

```bash
open results/figures_count.png
```

## Posibles Errores y Soluciones

🔹 **Error `ModuleNotFoundError`** (módulo no encontrado):

```bash
pip3 install pymupdf matplotlib wordcloud
```

🔹 **No se generan resultados en `results/`**:
- Verificar que hay PDFs en la carpeta `data/`.
- Ejecutar `ls data/` para confirmar.

🔹 **Errores inesperados**:
- Ejecutar nuevamente el script.
- Revisar el mensaje de error.

## Recursos Útiles

- [arXiv - Artículos Open Access](https://arxiv.org/)
- [PubMed Central - Medicina y Ciencias](https://www.ncbi.nlm.nih.gov/pmc/)
- [DOAJ - Journals de Acceso Abierto](https://www.doaj.org/)


Este proyecto facilita la extracción de información relevante en documentos científicos de forma automatizada.
