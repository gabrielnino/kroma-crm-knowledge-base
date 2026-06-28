# NOTAS DE PREPARACIÓN: REUNIÓN CON JOSÉ MARÍN (CBN NOTICIAS)
Fecha de la Reunión: Domingo 28 de Junio de 2026, 9:00 AM (Google Meet)
Objetivo Principal: Calificar la cuenta (Sandler) y posicionar a KASI como Arquitecto Tecnológico.

---

## 1. EL GANCHO VISUAL (DEMOSTRACIÓN EN VIVO)
*   **La Acción:** Durante la llamada, pídele a José que comparta por WhatsApp el enlace de cualquier noticia específica de su portal actual (`cbnnoticias.com`).
*   **El Fallo:** El sistema mostrará la imagen general de CBN y el texto estático del home. No mostrará ni la foto ni el título de la noticia compartida.
*   **El Argumento Comercial:** *"Cada vez que tus lectores comparten una noticia en redes, estás perdiendo hasta un 40% de clics potenciales (CTR) porque WhatsApp/Facebook no pueden leer la información de la noticia individual. Nosotros vamos a resolver esto inyectando meta tags dinámicos desde el servidor."*

---

## 2. LOS TRES DILEMAS TÉCNICOS (EXPLICACIÓN SIMPLE)

### A. "Google no ve tus noticias al instante" (CSR vs. SSR)
*   **Explicación:** El sitio actual es una Single Page Application (SPA). Todo se carga con JavaScript en el navegador del usuario. Google prefiere páginas web que ya vengan escritas desde el servidor. Para un periódico digital, esto retrasa la aparición de notas de última hora en las búsquedas de Google.
*   **Solución KASI:** Migrar a un modelo híbrido (Astro o Next.js) que genere el código HTML en el servidor, cargando el portal en menos de 1 segundo y facilitando la indexación inmediata en Google News.

### B. "Tu base de datos está expuesta en la vitrina" (Seguridad)
*   **Explicación:** La conexión y estructura de la base de datos de Supabase se ejecuta directamente en el navegador de los lectores. Aunque está protegida, facilita que bots o competidores copien (scrapen) todo el historial de artículos de forma masiva.
*   **Solución KASI:** Mudar la lógica a una API segura en el servidor, ocultando las llaves y tablas al público.

### C. "Carga lenta en teléfonos móviles" (Caché y Web Vitals)
*   **Explicación:** El sitio tiene deshabilitado el caché para forzar la actualización de noticias. Esto obliga a los lectores móviles con datos lentos a descargar toda la página de nuevo en cada clic, ralentizando la experiencia.
*   **Solución KASI:** Implementar generación estática incremental (ISR) que actualice la caché en el servidor solo cuando se publique una noticia nueva.

---

## 3. PREGUNTAS CLAVE DE CALIFICACIÓN (METODOLOGÍA SANDLER)

### A. Calificación del Dolor (Pain)
*   *"José, ¿cuál es el principal cuello de botella que experimentas hoy al publicar noticias? ¿Es la velocidad, el diseño o la falta de tráfico orgánico en buscadores?"*

### B. Calificación de Infraestructura y Control (Decision)
*   *"¿Tienes los accesos directos al dominio, hosting actual y la consola de Supabase, o dependemos de Nodix Studio (el diseñador anterior) para hacer modificaciones?"*
*   *"¿Qué volumen de artículos históricos y base de datos de usuarios tenemos que migrar al nuevo sistema?"*

### C. Calificación de Presupuesto (Budget)
*   *"Una reconstrucción a nivel de arquitectura SEO y servidor tiene un costo de infraestructura y desarrollo. ¿CBN tiene un presupuesto anual asignado para soporte tecnológico o es una inversión que evaluarás según el retorno de tráfico?"*
