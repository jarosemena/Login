import os

def read_files_in_directory(directory):
    # Crear o abrir el archivo markdown
    with open('Context.md', 'w', encoding='utf-8') as md_file:
        # Recorrer el directorio
        for root, dirs, files in os.walk(directory):
            # Escribir el título de la carpeta
            folder_name = os.path.basename(root)
            md_file.write(f"# {folder_name}\n\n")

            # Leer y escribir el contenido de los archivos de texto
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                     content = f.read()
                     md_file.write(f"## {file}\n\n")
                     md_file.write(content + "\n\n")
            md_file.write("\n---\n\n")  # Separador entre carpetas

if __name__ == "__main__":
    directory_to_scan = input("Introduce el directorio que deseas escanear: ")
    read_files_in_directory(directory_to_scan)
    print("El archivo Context.md ha sido creado.")