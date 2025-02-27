import os
import json
import re
import fitz  # PyMuPDF
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def extract_abstract(text):
    """ Extrae el abstract buscando palabras clave "Abstract" o "Resumen"."""
    match = re.search(r'(Abstract|ABSTRACT|Resumen|RESUMEN)[:\s]*(.+?)(\n\n|\r\n\r\n|Introduction|Introducción)', text, re.DOTALL)
    if match:
        return match.group(2).strip()
    else:
        words = text.split()
        return " ".join(words[:200])

def count_images(doc):
    """ Cuenta el número de imágenes en todas las páginas del PDF. """
    return sum(len(page.get_images(full=True)) for page in doc)

def extract_links(text):
    """ Extrae URLs usando regex. """
    return re.findall(r'https?://\S+', text)

def process_pdf(pdf_path):
    """ Procesa un PDF y extrae abstract, figuras y enlaces. """
    data = {"filename": os.path.basename(pdf_path)}
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error al abrir {pdf_path}: {e}")
        return None

    text_abstract = " ".join(page.get_text() for page in doc[:2])
    data["abstract"] = extract_abstract(text_abstract)
    data["figures_count"] = count_images(doc)
    data["links"] = list(set(extract_links(" ".join(page.get_text() for page in doc))))
    doc.close()
    return data

def generate_wordcloud(text, output_file):
    """ Genera una nube de palabras a partir del texto. """
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Nube de Palabras basada en Abstracts")
    plt.savefig(output_file)
    plt.close()

def generate_figures_chart(data, output_file):
    """ Genera un gráfico de barras con la cantidad de figuras por artículo. """
    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values(), color='skyblue')
    plt.xlabel("Artículos")
    plt.ylabel("Número de Figuras")
    plt.title("Número de Figuras por Artículo")
    plt.xticks(rotation=45, ha='right')
    plt.savefig(output_file)
    plt.close()

def extract_and_print_links(all_data):
    """ Muestra en pantalla los enlaces extraídos de cada artículo. """
    for item in all_data:
        print(f"Artículo: {item['filename']}")
        print("Enlaces encontrados:")
        for link in item["links"]:
            print(f" - {link}")
        print("-" * 50)

def main():
    pdf_dir = "data"
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    all_data = []
    
    for filename in os.listdir(pdf_dir):
        if filename.lower().endswith(".pdf"):
            print(f"Procesando {filename}...")
            pdf_path = os.path.join(pdf_dir, filename)
            data = process_pdf(pdf_path)
            if data:
                all_data.append(data)
    
    with open(os.path.join(results_dir, "data.json"), "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    
    abstracts_text = " ".join(item["abstract"] for item in all_data if "abstract" in item)
    generate_wordcloud(abstracts_text, os.path.join(results_dir, "wordcloud.png"))
    
    figures_data = {item["filename"]: item["figures_count"] for item in all_data}
    generate_figures_chart(figures_data, os.path.join(results_dir, "figures_count.png"))
    
    extract_and_print_links(all_data)
    
    print("Procesamiento completado. Resultados guardados en la carpeta 'results'.")
    
if __name__ == "__main__":
    main()
