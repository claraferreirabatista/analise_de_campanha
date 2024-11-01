import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from nbconvert import HTMLExporter
    import nbformat
except ImportError:
    print("Instalando bibliotecas necessárias...")
    install_package("nbconvert")
    install_package("nbformat")
    from nbconvert import HTMLExporter
    import nbformat

def convert_notebook_to_html(notebook_path):
    # Carrega o notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)
    
    # Configura o exportador para HTML
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = False  # Define para True se quiser excluir o código
    html_exporter.exclude_output_prompt = True  # Remove o prompt de saída

    # Converte o notebook para HTML
    body, _ = html_exporter.from_notebook_node(notebook_content)

    # Salva o HTML
    html_path = notebook_path.replace('.ipynb', '.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(body)
    
    print(f"Notebook convertido e salvo em {html_path}")

# Caminho para o notebook que deseja converter
notebook_path = 'analise_exploratoria_desde_janeiro.ipynb'
convert_notebook_to_html(notebook_path)
