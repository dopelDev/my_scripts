#!/usr/bin/env python3

import os
import sys
import subprocess

def show_help():
    print("Uso: script.py [opciones]")
    print()
    print("Opciones:")
    print("  -h, --help       Mostrar esta ayuda y salir")
    print("  --trans          Convertir los archivos .ttf y .otf a .woff y .woff2")
    print("  --clean          Eliminar los archivos .ttf y .otf originales después de la conversión")
    print()
    print("Este script convierte todos los archivos .ttf y .otf en el directorio actual a los formatos .woff y .woff2 y puede eliminar los archivos originales si se especifica.")

def parse_args(args):
    trans = False
    clean = False

    for arg in args:
        if arg in ('-h', '--help'):
            show_help()
            sys.exit(0)
        elif arg == '--trans':
            trans = True
        elif arg == '--clean':
            clean = True
        else:
            print(f"Opción desconocida: {arg}")
            show_help()
            sys.exit(1)

    return trans, clean

def convert_fonts():
    font_files = [f for f in os.listdir('.') if f.endswith('.ttf') or f.endswith('.otf')]

    if not font_files:
        print("No se encontraron archivos .ttf o .otf en el directorio actual.")
        return

    for font in font_files:
        base_name, ext = os.path.splitext(font)
        print(f"Procesando {font} => {base_name}.woff2 y {base_name}.woff")

        # Convertir a WOFF2
        subprocess.run(['fonttools', 'ttLib.woff2', 'compress', font, '-o', f'{base_name}.woff2'])

        # Convertir a WOFF (si tienes woff2_compress instalado)
        subprocess.run(['woff2_compress', font])

def clean_fonts():
    font_files = [f for f in os.listdir('.') if f.endswith('.ttf') or f.endswith('.otf')]
    
    all_converted = True
    for font in font_files:
        base_name, ext = os.path.splitext(font)
        if not (os.path.exists(f'{base_name}.woff') and os.path.exists(f'{base_name}.woff2')):
            all_converted = False
            break
    
    if all_converted:
        for font in font_files:
            print(f"Eliminando archivo original: {font}")
            os.remove(font)
    else:
        print("No todos los archivos .ttf y .otf tienen sus equivalentes .woff y .woff2. No se eliminó ningún archivo.")

if __name__ == "__main__":
    trans, clean = parse_args(sys.argv[1:])

    if trans:
        convert_fonts()
    
    if clean:
        clean_fonts()

