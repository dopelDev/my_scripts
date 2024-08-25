#!/bin/bash

prompt="$1"
url="http://localhost:11434/api/generate"

response=$(curl -s -X POST -H "Content-Type: application/json" -d "{\"model\":\"codellama:7b-code\",\"prompt\":\"$prompt\"}" $url)
echo "Respuesta: $response"

