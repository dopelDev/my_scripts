#!/bin/bash

# Este script genera un string aleatorio complejo o simple.
# Puedes especificar la longitud deseada como primer argumento al script.
# Usa el segundo argumento "simple" para excluir símbolos especiales.

# Longitud predeterminada del string, si no se especifica ninguna.
DEFAULT_LENGTH=72

# Utiliza el primer argumento como longitud, o usa el valor predeterminado.
LENGTH=${1:-$DEFAULT_LENGTH}

# Determina si se deben usar símbolos especiales.
USE_SYMBOLS=${2:-true}

# Caracteres que se incluirán en el string aleatorio.
CHARS='A-Za-z0-9!@#$%^&*()_+{}|:<>?='
CHARS_SIMPLE='A-Za-z0-9'

# Selecciona el conjunto de caracteres adecuado.
if [ "$USE_SYMBOLS" = "simple" ]; then
  CHARS=$CHARS_SIMPLE
fi

# Genera el string aleatorio.
tr -dc "$CHARS" < /dev/urandom | head -c $LENGTH ; echo ''

