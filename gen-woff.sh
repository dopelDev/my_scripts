#!/bin/bash

for font in *.ttf; do
    # Nombre sin la extensión
    base_name=$(basename "$font" .ttf)

    # Convertir a WOFF
    fonttools ttLib.woff2 compress "$font" -o "$base_name.woff2"

    # Convertir a WOFF2 (si tienes woff2_compress instalado)
    woff2_compress "$font"
done

