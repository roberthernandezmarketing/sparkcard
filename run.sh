#!/bin/bash
# run.sh

echo "Starting Sparkcard Backend..."

# Obtener la ruta absoluta del directorio donde se encuentra este script (sparkcard/)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Añadir el directorio raíz del proyecto al PYTHONPATH
# Esto permite que Python encuentre el paquete 'sparkcard'
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

# Ejecutar uvicorn. Ahora debería encontrar 'sparkcard.backend.src.main'
uvicorn sparkcard.backend.src.main:app --host 0.0.0.0 --port 8000


# uvicorn sparkcard.backend.src.main:app --reload