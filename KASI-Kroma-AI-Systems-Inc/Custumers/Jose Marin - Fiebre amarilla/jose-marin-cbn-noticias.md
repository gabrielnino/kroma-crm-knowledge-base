# CASO DE ESTUDIO: JOSÉ MARÍN (CBN NOTICIAS)
**Tipo:** Desarrollo Web & Reconstrucción de Portal de Noticias  
**Propietario de la Cuenta:** Luis Gabriel Niño (KASI)  
**Contacto del Cliente:** José Augusto Marín (Propietario de CBN Noticias / cbnnoticias@gmail.com)  
**Fase del Pipeline:** Calificación Completada -> Diseño de Propuesta Técnica  
**Última Actualización:** 2026-06-28 (Post-Reunión de Calificación)

---

## 1. RESUMEN DE LA REUNIÓN DE CALIFICACIÓN (2026-06-28)

La reunión formal de 30 minutos se llevó a cabo el domingo 28 de junio a las 9:00 AM (PDT). Se resolvieron las dificultades iniciales de conexión y uso compartido de pantalla, logrando una sesión de diagnóstico profunda de 48 minutos. Se aplicó la metodología Sandler para calificar los dolores, la toma de decisiones y el presupuesto, revelando el verdadero estado comercial y técnico de la cuenta.

---

## 2. MATRIZ DE CALIFICACIÓN SANDLER (VERIFICADA)

### A. DOLOR (PAIN) - Altamente Calificado
1. **Pérdida del Historial de Búsquedas (El "Efecto Chorrera" y Artículos Huérfanos):** 
   * *El Dolor:* El desarrollador anterior configuró una plantilla básica de WordPress que muestra los artículos en un scroll infinito. Esto destruyó la estructura de URLs individuales indexables. Además, en la reciente migración a Netlify/Supabase, **solo se migraron 147 artículos de un total de más de 1,100 artículos publicados históricos**, dejando el resto huérfanos y rotos.
   * *El Impacto:* Los usuarios no pueden encontrar notas históricas en Google, lo que destruyó la autoridad SEO acumulada durante los más de 8 años de antigüedad del dominio.
2. **Pérdida de Accesos Administrativos por Enrutamiento de Netlify:**
   * *El Dolor:* El apuntamiento del dominio principal de Netlify rompió las rutas de WordPress y del servidor, impidiendo que José pueda entrar a `wp-admin` para editar noticias o a `cpanel` para monitorear el comportamiento de la página.
3. **El Bloqueo de Meta en Canadá (Ley C-18 / Online News Act):**
   * *El Dolor:* Las restricciones de distribución de noticias en Facebook e Instagram en todo Canadá eliminaron un canal que antes le otorgaba a CBN **de 10,000 a 15,000 visualizaciones por nota** en pocas horas.
4. **Distribución Manual Ineficiente:**
   * *El Dolor:* José gasta **de 1 a 2 horas diarias** compartiendo enlaces de 5 en 5 contactos en WhatsApp para alcanzar de forma manual a apenas 300 o 400 lectores.
5. **Frustración con Desarrolladores Previos:**
   * *El Dolor:* Freelancers anteriores le cobraban extra por cambios sencillos y le entregaban plantillas mal configuradas.

### B. DECISIÓN (DECISION) - Calificada
* **Tomador de Decisiones Único:** José Augusto Marín es el propietario exclusivo y quien toma todas las decisiones financieras y editoriales de CBN Noticias.
* **Tiempos:** Requiere una reconstrucción prioritaria del portal para detener el desgaste operativo del envío manual por WhatsApp.

### C. PRESUPUESTO (BUDGET) - Calificado (Bajo pero con Oportunidad de Sociedad)
* **Realidad Financiera Actual:** CBN Noticias ha operado principalmente como un "servicio comunitario" no comercial. 
* **Ingresos Anuales:** El portal generó únicamente **$2,000 USD en el último año** a través de 3 o 4 clientes inbound (reels en Instagram, pautas sencillas).
* **Posición de Honestidad del Cliente:** José es sumamente ético; no busca activamente anunciantes porque se niega a vender espacios publicitarios sin poder mostrar analíticas de tráfico transparentes y estables (las cuales perdió debido al rediseño fallido y al bloqueo de Meta).
* **Oportunidad Comercial:** Luis Gabriel Niño propuso una estructura de negocio híbrida o propuesta integral que combine **Desarrollo Web moderno + Estrategia de Contenido y Marketing**, enfocando el sitio hacia la rentabilidad (SEO orgánico para capturar tráfico de fuera y dentro de Canadá, eludiendo el bloqueo de Facebook/Instagram).

---

## 3. ESPECIFICACIONES TÉCNICAS REQUERIDAS

El nuevo sitio web debe cumplir con los siguientes requerimientos levantados en la sesión:
* **Estructura Dinámica de Secciones (6 a 7 categorías fundamentales):**
  1. Noticias Locales (Vancouver / BC)
  2. Noticias Nacionales (Canadá)
  3. Internacionales
  4. Inmigración (Foco de alto tráfico SEO)
  5. Judicial
  6. Deportes
* **Interactividad Multimedia:** Integración fluida de videos de YouTube y reproductores de audio para programas de entrevistas semanales (José planea lanzar un programa de actualidad semanal de 30 minutos con entrevistas).
* **Políticas de IA:** José utiliza IA para la generación de imágenes de cabecera de las noticias para evitar infracciones de derechos de autor, manteniendo un fuerte filtro de veracidad e integridad periodística para evitar "fake news".

---

## 4. ANÁLISIS DE RIESGOS KASI

* **Riesgo de Presupuesto Tradicional:** El cliente no dispone de un flujo de caja alto en CBN ($2,000/año actuales). Intentar venderle un desarrollo de software corporativo estándar de $5,000 USD de pago único resultará en una pérdida de la oportunidad.
* **Mitigación de Riesgo (La Alternativa KASI):** Estructurar una propuesta de **Desarrollo + Alianza de Crecimiento** o una propuesta escalonada. Una opción viable es un costo base de desarrollo web ágil (utilizando la velocidad de Astro) combinado con un modelo de soporte o una estrategia de marketing conjunta donde KASI capture un porcentaje de los nuevos anunciantes que ingresen gracias al aumento verificado de tráfico mediante SEO.
* **Riesgo Tecnológico (Meta Block):** Depender de redes sociales tradicionales en Canadá para tráfico está descartado. El SEO de Google (búsqueda orgánica de inmigración y noticias locales) es el único canal viable para revivir el tráfico (apuntar a la proyección estimada de **27,600 visitas mensuales** en el escenario moderado al Mes 12).

---

## 5. PRÓXIMOS PASOS (PLAN DE ACCIÓN DE LUIS)

1. **Diseñar la Propuesta Técnica y Comercial:** Crear una oferta para una plataforma web ultrarrápida (Astro + Supabase) estructurada por secciones, con integración de audio/video.
2. **Definir el Modelo de Negocios Híbrido:** Elaborar las opciones de cotización (Pago de configuración inicial bajo + Soporte/Crecimiento de monetización SEO).
3. **Presentar Propuesta a José Marín:** Agendar una llamada de 20 minutos para la próxima semana (aprovechando la cercanía en el grupo *Fiebre Amarilla*) para revisar la propuesta.
