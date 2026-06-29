Actúa como un Diseñador de Producto Digital (UX/UI Lead) de nivel Sénior, experto en arquitectura de la información, desarrollo frontend estático y optimización de plataformas de medios digitales.

Tu tarea es generar el código fuente HTML y CSS (en un único archivo completamente autónomo y listo para producción) que renderice una presentación interactiva de 10 diapositivas orientada a José Augusto Marín (Director de CBN Noticias), tomando como base única y absoluta el archivo adjunto "documento-maestro-estrategico-v2.pdf".

Esta presentación está diseñada exclusivamente para la visualización directa del cliente durante la reunión ejecutiva, por lo que debe omitirse cualquier tipo de nota para el orador, guion interno o metadato de venta. El código debe estructurar componentes visuales de alto impacto.

Debes seguir estrictamente los siguientes lineamientos de desarrollo, diseño y enfoque de negocio:

---

### 1. ARQUITECTURA DEL CÓDIGO Y FORMATO DE SALIDA
*   **Entregable único**: Un solo bloque de código HTML que incluya los estilos en una etiqueta `<style>` interna. Sin dependencias externas, frameworks pesados de JS (como Reveal.js) ni fuentes/imágenes externas (usa fuentes nativas del sistema y gráficos vectoriales SVG puros inline).
*   **Layout y Proporciones**: Relación de aspecto corporativa fija de 16:9 (Apaisado) para cada contenedor de diapositiva. Usa `display: block` con técnicas de centrado semántico o estructuras de tablas HTML puras para asegurar la compatibilidad y consistencia visual en la exportación o renderizado.
*   **Densidad de la Información**: Un único concepto estratégico central por pantalla. Reemplaza bloques de texto extensos por estructuras de datos escaneables, KPI highlights, tablas y diagramas vectoriales.

---

### 2. SISTEMA DE DISEÑO VISUAL (UI TOKENS EN CSS)
*   **Paleta de Colores**:
    *   Fondo de Diapositiva (`background-color`): Gris Pizarra Oscuro Mate (`#1E2229`) para proyectar prestigio editorial.
    *   Texto Principal y Contornos (`color`, `border`): Blanco Puro (`#FFFFFF`) para títulos y Gris Tenue (`#A0AAB2`) para descripciones secundarias.
    *   Color de Énfasis (`Accent`): Azul Celeste Corporativo (`#00A8E8`), aplicado exclusivamente a métricas críticas de éxito, porcentajes o bordes activos de componentes.
*   **Tipografía**: Familia tipográfica Sans-Serif limpia del sistema (`font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`). Jerarquía estricta: Títulos de sección compactos y números de impacto masivos.
*   **Geometría**: Contenedores basados en cajas estructuradas con bordes redondeados sutiles (`border-radius: 6px`) y bordes delgados (`1px solid #313742`) para mantener la seriedad corporativa.
*   **Visualización de Datos**: Gráficos, líneas de tiempo y diagramas construidos exclusivamente con HTML y elementos SVG inline estilizados con los colores de la paleta.

---

### 3. CONTENIDO ESTRUCTURADO POR DIAPOSITIVA (A extraer del PDF)
Genera el HTML semántico completo (las 10 diapositivas contenidas de forma lineal o secuencial) asegurando que cada una renderice el componente visual exacto sin anotaciones de desarrollo:

*   **Slide 1 (Portada)**: Encabezado premium con Co-branding simétrico entre CBN Noticias y Kroma AI Systems (incorporando marcadores de posición visuales o el logo de LN en SVG).
*   **Slide 2 (Acuerdo Base)**: Estructura visual en "Pantalla Dividida" (Split-Screen) que presente las reglas de juego equilibradas, otorgando explícitamente el poder del "NO" inmediato al cliente para eliminar fricción.
*   **Slide 3 (Diagnóstico)**: Cuadrícula limpia de 2x2 que resalte con el color de énfasis (`#00A8E8`) los indicadores críticos: "0" tráfico en Meta, "2 horas" de procesamiento manual y "$2,000 USD" de techo histórico.
*   **Slide 4 (Infraestructura)**: Gráfico comparativo de barras horizontales hecho con divs CSS que ilustre los tiempos de carga en entornos móviles (WordPress 3.8s vs Astro <1.0s).
*   **Slide 5 (Mercado)**: Estructura de dos columnas asimétricas que valide matemáticamente el crecimiento demográfico del +49.5%, citando explícitamente la fuente "Statistics Canada".
*   **Slide 6 (SEO)**: Tabla HTML (`<table>`) pulida de crecimiento predictivo a 12 meses que correlacione de forma limpia el volumen de artículos indexados con el tráfico mensual acumulado.
*   **Slide 7 (Finanzas)**: Gráfico vectorial SVG minimalista que ilustre la división del revenue share 70/30, destacando con tipografía pesada el concepto del multiplicador "x4 de ingresos libres de costo".
*   **Slide 8 (Setup Fee)**: Línea de tiempo horizontal compuesta por 3 nodos circulares numerados en CSS que grafique la relación Hito/Desembolso de la inversión fraccionada.
*   **Slide 9 (Garantías)**: Un icono central de escudo de seguridad en SVG rodeado por tres bloques independientes que sinteticen las salvaguardas contractuales (Riesgo Cero, Propiedad Intacta, Soberanía de Datos).
*   **Slide 10 (Semana 1)**: Un check-list visual de estilo "Call to Action" corporativo con el Paso 1 activado y destacado con el color de énfasis para guiar el cierre natural del acuerdo.

Procesa la información con rigurosidad técnica, exactitud de datos y una estética premium de consultoría de negocios. No utilices texto simulado (Lorem Ipsum); extrae los datos reales del PDF y entrega el archivo HTML completo y cerrado, listo para ser visualizado por el cliente.