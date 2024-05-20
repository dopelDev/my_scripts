#!/bin/bash

# Función para restaurar la configuración al recibir señal de interrupción (Ctrl+C)
trap restore_settings SIGINT

# Función para restaurar la configuración original
function restore_settings() {
  echo "Restaurando la configuración original..."
  xset s on
  xset +dpms
  exit
}

# Deshabilita el salvapantallas y la gestión de energía
echo "Deshabilitando el apagado de los monitores..."
xset s off
xset -dpms

# Mantén el script en ejecución hasta que reciba la señal de interrupción (Ctrl+C)
echo "Presiona Ctrl+C para restaurar la configuración original y salir."
while :; do
  sleep 60
done

