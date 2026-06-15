#!/bin/bash

# Script para criar migrações de todos os apps do projeto Rudia

echo "Criando migrações para todos os apps..."
echo "========================================"

python manage.py makemigrations avaliacoes
python manage.py makemigrations localizacao
python manage.py makemigrations moderacao
python manage.py makemigrations servicos
python manage.py makemigrations viagem
python manage.py makemigrations usuarios

echo "========================================"
echo "Migrações criadas com sucesso!"