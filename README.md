# 📊 Dashboard de Ventas Interactivo

Dashboard de ventas profesional y completamente interactivo, construido con **Python**, **Streamlit** y **Plotly**. Diseñado como un MVP listo para producción para PYMEs que necesitan información clara y accionable de sus datos de ventas — sin la complejidad de las herramientas BI empresariales.

---

## ✨ Funcionalidades

### Filtros en el Sidebar
- **Selector de rango de fechas** — acotá cualquier período personalizado dentro del dataset
- **Multiselect de Región** — filtrá por una o varias regiones geográficas
- **Multiselect de Producto** — aislá líneas de productos específicas

Todos los filtros son dinámicos e interconectados: cada gráfico, KPI y tabla se actualiza al instante.

### Tarjetas KPI
Cuatro métricas resumen mostradas en la parte superior del dashboard:

| KPI | Descripción |
|---|---|
| 💰 Ventas Totales | Suma de todas las ventas (USD) del período seleccionado |
| 📈 Ganancia Neta | Ventas menos costos, con porcentaje de margen |
| 🛒 Total de Pedidos | Cantidad de transacciones individuales |
| 📦 Unidades Vendidas | Total de unidades en todos los pedidos, con promedio por pedido |

### Gráficos

| Gráfico | Tipo | Propósito |
|---|---|---|
| Ventas por Producto | Barras horizontales | Comparar ingresos (y opcionalmente ganancia) por producto — alternables desde la leyenda |
| Share por Región | Dona | Desglose visual de la contribución de ingresos por región |
| Tendencia Mensual | Líneas múltiples | Seguir la evolución de ingresos de cada producto mes a mes |
| Mapa de Calor | Grilla Región × Mes | Identificar patrones estacionales y picos regionales de un vistazo |

### Tabla de Datos
- Tabla con scroll que muestra todos los pedidos filtrados, ordenados por ingresos
- Columnas: Fecha, Producto, Región, Unidades, Ventas (USD), Costo (USD), Ganancia (USD)
- **Botón de descarga** — exporta el dataset filtrado como archivo `.csv` limpio (UTF-8 BOM, separado por punto y coma — se abre correctamente en Excel en cualquier configuración regional)

### Manejo de Errores
- Advertencia amigable cuando los filtros no arrojan resultados
- Mensaje informativo si el archivo de datos no existe o tiene columnas incorrectas
- Fallback al rango de fechas completo si el selector devuelve una selección incompleta

---

## 🗂️ Estructura del Proyecto

```
├── app.py               # Dashboard principal de Streamlit
├── generate_data.py     # Script para generar datos sintéticos de demo
├── ventas_demo.csv      # Dataset de demo autogenerado (ignorar en .gitignore para producción)
├── requirements.txt     # Dependencias de Python
└── README.md
```

---

## 🚀 Inicio Rápido

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sales-dashboard.git
cd sales-dashboard
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Generar el dataset de demo

```bash
python generate_data.py
```

Esto crea `ventas_demo.csv` con **1.200 pedidos sintéticos** a lo largo de un año calendario completo, con estacionalidad realista (pico en Q4, enero lento) y variación de precios.

### 4. Lanzar el dashboard

```bash
streamlit run app.py
```

La app se abre automáticamente en `http://localhost:8501`.

---

## 📦 Dependencias

```
streamlit>=1.35.0
pandas>=2.0.0
plotly>=5.20.0
numpy>=1.26.0
```

---

## 📁 Formato de Datos

El dashboard lee cualquier archivo CSV llamado `ventas_demo.csv` con las siguientes columnas:

| Columna | Tipo | Descripción |
|---|---|---|
| `Fecha` | date | Fecha de la transacción (`YYYY-MM-DD`) |
| `Producto` | string | Nombre del producto o servicio |
| `Región` | string | Región geográfica |
| `Ventas_USD` | float | Ingresos brutos en USD |
| `Unidades` | int | Unidades vendidas |
| `Costo_USD` | float | Costo de los bienes o servicios en USD |

> **Para usar tus propios datos:** reemplazá `ventas_demo.csv` con un archivo que siga este esquema. Los nombres de columnas deben coincidir exactamente.

---

## 🌐 Despliegue

### Streamlit Community Cloud (gratuito)

1. Subí tu repositorio a GitHub (asegurate de incluir `requirements.txt`)
2. Entrá a [share.streamlit.io](https://share.streamlit.io)
3. Conectá tu repositorio de GitHub y seleccioná `app.py` como punto de entrada
4. Hacé clic en **Deploy** — tu dashboard obtiene una URL pública en minutos

### Privado / Self-hosted

La app corre en cualquier máquina con Python 3.9+. Para entornos de producción, se recomienda correrla detrás de un proxy inverso (nginx) con middleware de autenticación.

---

## 🛠️ Personalización

| Qué cambiar | Dónde |
|---|---|
| Nombres y precios de productos | Diccionario `PRODUCTS` en `generate_data.py` |
| Regiones y su peso de ventas | Diccionario `REGIONS` en `generate_data.py` |
| Cantidad de pedidos de demo | `N_ROWS` en `generate_data.py` |
| Paleta de colores del dashboard | Constantes `PRIMARY`, `SECONDARY` en `app.py` |
| Umbral de margen KPI (verde/rojo) | Condición `margen_pct >= 30` en `app.py` |
| Separador y codificación del CSV descargado | Llamada a `to_csv()` en la sección 10 de `app.py` |

---

## 📸 Vista Previa

> Dashboard corriendo con datos de demo del año completo, sin filtros aplicados.

| Sección | Descripción |
|---|---|
| Barra superior | 4 tarjetas KPI con indicadores de tendencia |
| Fila 1 | Ventas por producto (barras) + share por región (dona) |
| Fila 2 | Líneas de tendencia mensual por producto |
| Fila 3 | Mapa de calor (región × mes) |
| Parte inferior | Tabla de datos filtrable + exportación CSV |

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Podés usarlo libremente como base para proyectos de clientes.

---

## 🤝 Construido con

- [Streamlit](https://streamlit.io) — Framework web en Python para apps de datos
- [Plotly](https://plotly.com/python/) — Librería de gráficos interactivos
- [Pandas](https://pandas.pydata.org) — Manipulación de datos
- [NumPy](https://numpy.org) — Generación de datos sintéticos