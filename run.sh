#!/bin/bash
echo "Starting Sparkcard Backend..."

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

# Usa el uvicorn del entorno virtual explícitamente
$SCRIPT_DIR/venv/Scripts/python.exe -m uvicorn backend.src.main:app --host 0.0.0.0 --port 8000 --reload
