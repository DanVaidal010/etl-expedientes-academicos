# ETL de Expedientes Académicos con Cuadro de Mando

## Asignatura

Profundización en Programación, Algoritmos y Estructuras de Datos

## Autor

Dan Vidal Gojgarea

Curso académico 2025–2026

---

# Descripción del proyecto

Este proyecto implementa una aplicación completa para la gestión de expedientes académicos mediante un proceso ETL (Extracción, Transformación y Carga), utilizando Python, SQLite y Tkinter.

La aplicación permite almacenar, validar, transformar y visualizar información académica relacionada con estudiantes, asignaturas y calificaciones, incluyendo estadísticas y representaciones gráficas mediante un cuadro de mando académico.

El objetivo principal es desarrollar una solución modular, mantenible y eficiente que cumpla con los requisitos funcionales planteados en la asignatura.

---

# Funcionalidades implementadas

## Base de datos SQLite

Se ha diseñado una base de datos local que almacena:

* estudiantes
* asignaturas
* calificaciones

Incluye:

* claves primarias y foráneas
* restricciones de unicidad
* control de integridad

---

## Proceso ETL

Se implementan procesos de:

### Extracción

Carga inicial de datos mediante script independiente.

### Transformación

Validación y deppuración de datos:

* validación de nombres
* validación de emails
* validación de códigos de asignatura
* validación de créditos
* validación de notas
* normalización de datos
* control de duplicados
* tratamiento de errores

### Carga

Inserción segura en base de datos con control de excepciones y cierre robusto de conexiones SQLite.

---

## Interfaz gráfica (GUI)

Se implementan dos cuadros de mando diferenciados:

### Panel de introducción de datos

Permite:

* registrar estudiantes
* registrar asignaturas
* registrar calificaciones

### Dashboard académico

Permite visualizar:

* total de estudiantes
* total de asignaturas
* total de calificaciones
* media global
* número de aprobados

Además incluye:

* gráfico de barras de medias por estudiante
* histograma de distribución de calificaciones

---

# Estructura del proyecto

```text
/
├── src/
│   ├── database/
│   ├── gui/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── scripts/
│   └── load_initial_data.py
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Instalación de dependencias

## Crear entorno virtual (opcional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución del proyecto

## 1. Cargar datos iniciales

```bash
python -m scripts.load_initial_data
```

Esto genera datos de ejemplo para:

* estudiantes
* asignaturas
* calificaciones

---

## 2. Ejecutar la aplicación

```bash
python -m src.main
```

Esto abrirá la interfaz gráfica principal.

---

# Formato de entrada

La entrada de datos se realiza desde la GUI mediante formularios:

## Estudiantes

* nombre
* email

## Asignaturas

* nombre
* código
* créditos

## Calificaciones

* ID estudiante
* ID asignatura
* nota

---

# Formato de salida

La aplicación genera:

* almacenamiento persistente en SQLite
* estadísticas académicas
* dashboard visual
* gráficos de análisis académico

---

# Casos de prueba

Ejemplos de validación:

## Caso válido

Estudiante:

* Nombre: Pedro García
* Email: [pedro@email.com](mailto:pedro@email.com)

Resultado:

* inserción correcta

## Caso inválido

Estudiante:

* Nombre: vacío
* Email: incorrecto

Resultado:

* error de validación

---

# Resultados esperados

El sistema debe permitir:

* gestión académica completa
* consultas estadísticas eficientes mediante SQL
* visualización clara de métrtricas académicas
* funcionamiento robusto ante errores de inserción

---

# Tecnologías utilizadas

* Python 3
* SQLite
* Tkinter
* Matplotlib
* Pytest

---

# Repositorio GitHub

El código fuente se encuentra alojado en GitHub y será compartido con el usuario:

RubenViMuUCAV

Repositorio preparado para clonación y ejecución directa.
