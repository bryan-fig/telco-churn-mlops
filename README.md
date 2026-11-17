Práctica 1 — Git: control de versiones para un proyecto de Machine Learning

**Proyecto:** Telco Customer Churn  
**Entorno:** Windows + Visual Studio Code + Git  
**Objetivo:** aprender Git de forma local, sin GitHub todavía.

## 1. Preparar el entorno

1. Instala Git para Windows si aún no está instalado.
2. Abre esta carpeta en Visual Studio Code.
3. Abre una terminal CMD y comprueba:

```bat
git --version
```

## 2. Configurar la identidad (solo la primera vez en cada equipo)

```bat
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@example.com"
```

Usa el correo que quieras asociar a tus commits.

## 3. Inicializar el repositorio

```bat
git init -b main
git status
```

Explica qué significa que la carpeta ahora sea un repositorio Git.

## 4. Preparar el primer commit

```bat
git add README.md data/telco_sample.csv src/summary.py
git status
git commit -m "Agregar estructura inicial del proyecto"
git log --oneline
```

Observa qué archivos quedaron registrados en el primer commit.

## 5. Modificar un archivo

Abre `README.md`, agrega tu nombre en la sección de observaciones y guarda.

```bat
git status
git diff
```

Describe la diferencia entre `git status` y `git diff`.

Después registra el cambio:

```bat
git add README.md
git commit -m "Actualizar observaciones del proyecto"
git log --oneline
```

## 6. Crear una versión nueva del análisis

Abre `src/summary.py` y modifica el texto de salida o agrega un comentario que explique qué calcula el programa.

Ejecuta:

```bat
python src/summary.py
```

Después registra el cambio con un nuevo commit.

## 7. Consultar versiones anteriores

```bat
git log --oneline
git show
```

Identifica qué commit corresponde a cada cambio. No es necesario usar `reset` ni borrar commits en esta práctica.

## 8. Crear una rama

```bat
git switch -c prueba-nueva-metrica
```

En `src/summary.py`, agrega una línea que calcule el porcentaje de clientes de muestra con `Churn = Yes`.

Ejecuta el programa y registra el cambio:

```bat
git add src/summary.py
git commit -m "Agregar porcentaje de abandono"
```

Regresa a la rama principal:

```bat
git switch main
```

Comprueba que el cambio de la rama de prueba no aparece en `main`.

Integra la rama:

```bat
git merge prueba-nueva-metrica
```

Comprueba el historial:

```bat
git log --oneline --graph --all
```

## 9. Entregable

Entrega un PDF con capturas y respuestas:

1. `git --version`.
2. Repositorio inicializado y `git status`.
3. Primer commit y `git log --oneline`.
4. Diferencias observadas con `git diff`.
5. Rama creada y cambio registrado.
6. Merge realizado y gráfico del historial.
7. Explicación breve: ¿por qué Git es útil en proyectos de Machine Learning?

## Nota sobre los datos

`data/telco_sample.csv` es un conjunto pequeño y didáctico de datos ficticios, incluido únicamente para practicar el flujo de trabajo. No representa clientes reales ni es un dataset válido para conclusiones de negocio.

Modelo principal: SVM


## Evaluación de modelos

Para evaluar el rendimiento de los modelos de clasificación utilizaremos las métricas Accuracy, F1 y ROC-AUC. 

## Modelo SVM

Support Vector Machine (SVM) es un algoritmo de aprendizaje supervisado que busca encontrar el hiperplano óptimo para separar las clases maximizando el margen entre ellas.
