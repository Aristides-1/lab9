# 🚀 Laboratorio 9 Django Relaciones, Envío de Correos y Generación de PDF

⭐ Curso: Desarrollo de Aplicaciones Web.


🎥 Video de funcionalidad : https://www.youtube.com/watch?v=pq4nVq8H7ss&feature=youtu.be



Proyecto desarrollado con **Django 6** para demostrar:

- 🔗 Relación **Uno a Muchos** (ForeignKey)
- 🔄 Relación **Muchos a Muchos** (ManyToManyField)
- 📧 Envío de correos electrónicos con Django
- 📄 Generación de documentos PDF utilizando **xhtml2pdf**

## 🛠️ Tecnologías Utilizadas

- Python 3.12
- Django 6.0.6
- SQLite3
- xhtml2pdf

## 📂 Aplicaciones del Proyecto

### 1️⃣ RelacionDeUnoAMuchos
Implementación de relaciones entre modelos:

- ForeignKey (Uno a Muchos)
- ManyToManyField (Muchos a Muchos)

Modelos principales:

- Language
- Framework
- Movie
- Character

### 2️⃣ EnvioEmails
Envío de correos electrónicos desde Django utilizando SMTP.

Funcionalidades:

- Configuración de servidor SMTP
- Envío automático de correos de prueba

### 3️⃣ GeneracionPDF
Generación dinámica de archivos PDF a partir de plantillas HTML.

Funcionalidades:

- Renderizado HTML → PDF
- Descarga o visualización en navegador
- Uso de plantillas Django

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd lab9
```

Crear entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install django
pip install xhtml2pdf
```

Ejecutar migraciones:

```bash
python manage.py migrate
```

Iniciar servidor:

```bash
python manage.py runserver
```

## 🌐 Rutas Principales

| Ruta | Descripción |
|--------|------------|
| `/` | Envío de correos |
| `/pdf/` | Generación de PDF |

