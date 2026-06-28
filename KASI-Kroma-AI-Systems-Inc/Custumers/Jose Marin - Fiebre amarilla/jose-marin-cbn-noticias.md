# INFORME EJECUTIVO DE CONSULTORÍA
## Auditoría Integral, Diagnóstico Comercial y Propuesta de Transformación Digital

**Proyecto:** Reconstrucción del Portal de CBN Noticias  
**Cliente:** CBN Noticias (cbnnoticias.com)  
**Preparado por:** KASI Consultoría Estratégica & Transformación Digital  
**Fecha:** 28 de Junio de 2026  

---

## Índice

1. [Executive Summary](#capítulo-1-executive-summary)
2. [Perfil del Cliente](#capítulo-2-perfil-del-cliente)
3. [Auditoría Completa del Sitio Web](#capítulo-3-auditoría-completa-del-sitio-web)
4. [Benchmark](#capítulo-4-benchmark)
5. [Diagnóstico Sandler](#capítulo-5-diagnóstico-sandler)
6. [Matriz de Riesgos](#capítulo-6-riesgos)
7. [Vacíos de Información](#capítulo-7-vacíos-de-información)
8. [Preguntas para la Reunión de Descubrimiento](#capítulo-8-preguntas-para-la-reunión)
9. [Arquitectura Recomendada](#capítulo-9-arquitectura-recomendada)
10. [Roadmap de Implementación](#capítulo-10-roadmap)
11. [Estrategia Comercial para KASI](#capítulo-11-estrategia-comercial-para-kasi)
12. [Propuesta de Transformación Digital](#capítulo-12-propuesta-de-transformación-digital)
13. [Quick Wins](#capítulo-13-quick-wins)
14. [Backlog Priorizado](#capítulo-14-backlog-priorizado)
15. [Estimación Preliminar del Proyecto](#capítulo-15-estimación-del-proyecto)
16. [Score Ejecutivo](#capítulo-16-score-ejecutivo)
17. [Conclusiones Ejecutivas](#capítulo-17-conclusiones-ejecutivas)

---

## CAPÍTULO 1: Executive Summary

CBN Noticias es un portal digital independiente fundado por José Augusto Marín en Vancouver, enfocado en proveer noticias en español para la comunidad hispanohablante en Columbia Británica y Canadá. Su cobertura principal abarca inmigración, política, deporte y noticias locales. El sitio actual (cbnnoticias.com) muestra un diseño estático básico (Netlify, Supabase, Vanilla JS) que, aunque funcional y rápido, carece de las capacidades dinámicas, de monetización y SEO avanzadas requeridas por un medio de comunicación moderno.

**Necesidad Principal:** Transformar el portal estático en una plataforma de medios digitales escalable, optimizada para SEO (Google News), con un CMS robusto que permita flujos de trabajo editoriales eficientes y abra nuevas vías de monetización.

**Estado Actual:**
El sitio web actual es un desarrollo personalizado (SPA) alojado en Netlify, utilizando Supabase como backend. Presenta deficiencias críticas en SEO (ej. renderizado del lado del cliente sin SSR, ausencia de sitemaps de noticias dinámicos, falta de feeds RSS funcionales) y carece de espacios publicitarios integrados o modelos de suscripción. El tráfico mensual es bajo (aprox. 500-1100 visitas mensuales según Similarweb), concentrado principalmente en Canadá (80%).

**Oportunidad Comercial y Tecnológica:**
Para KASI, existe una oportunidad de alto valor para liderar una reconstrucción completa ("re-platforming") hacia una arquitectura Headless CMS (ej. Strapi, Sanity o Contentful) con un frontend moderno (Next.js/Vercel) optimizado para Core Web Vitals y Google News. Esto permitirá a CBN Noticias escalar su audiencia, automatizar la publicación cruzada y monetizar el tráfico (programática, patrocinios, membresías).

**Riesgos:**
El principal riesgo radica en el presupuesto del cliente (medio independiente) y la resistencia al cambio en los flujos de trabajo editoriales. Tecnológicamente, el riesgo es bajo si se adopta una arquitectura estándar de la industria.

**Semáforo Ejecutivo:**
🟢 **Viabilidad Técnica:** Alta (Tecnologías maduras y probadas).
🟡 **Viabilidad Comercial:** Media (Depende del presupuesto y urgencia del cliente).
🟢 **Impacto del Proyecto:** Alto (Transformación total del modelo operativo y de ingresos).

---

## CAPÍTULO 2: Perfil del Cliente

| Atributo | Detalle |
| :--- | :--- |
| **Empresa** | CBN Noticias |
| **Actividad** | Medio de comunicación digital (Periodismo independiente) |
| **Modelo de Negocio** | Actualmente sin modelo de monetización claro en el sitio web (sin anuncios programáticos ni suscripciones visibles). |
| **Audiencia** | Comunidad hispanohablante residente en Canadá (especialmente Vancouver/BC) y prospectos de inmigración en Latinoamérica. |
| **Mercado Objetivo** | Hispanos en Columbia Británica; personas interesadas en emigrar a Canadá. |
| **Canales** | Sitio web, Facebook, Instagram, TikTok, YouTube. |
| **Stakeholders** | José Augusto Marín (Fundador, Director y Editor). |
| **Nivel de Madurez Digital** | Básico/Intermedio. Tienen presencia multicanal, pero la infraestructura web es limitante. |
| **Relación con KASI** | Etapa de descubrimiento inicial / Calificación. |
| **Nivel de Oportunidad** | Alto potencial estratégico para KASI como caso de éxito en medios digitales. |

---

## CAPÍTULO 3: Auditoría Completa del Sitio Web

### Arquitectura
* **Estructura:** Arquitectura plana tipo SPA (Single Page Application).
* **Navegación:** Menú superior funcional pero básico (Todas, Local, Nacional, Internacional, Inmigración, Deporte, Judicial).
* **Taxonomía:** Basada en categorías amplias; carece de un sistema de etiquetas (tags) profundo o páginas de autor dedicadas.

### UX / UI
* **Navegación:** Simple, pero la carga dinámica de artículos vía JS puede causar fricción en el historial del navegador.
* **Jerarquía Visual:** Clara, priorizando la noticia destacada en un carrusel.
* **Identidad Visual:** Profesional y limpia (fondo claro `#FAF7F2`, texto oscuro), tipografías *Playfair Display* e *Inter*.
* **Accesibilidad Visual:** Buen contraste, pero carece de controles avanzados de accesibilidad.

### Responsive
* **Desktop/Tablet/Mobile:** El sitio es responsivo y se adapta correctamente, pero la experiencia móvil podría optimizarse para retención (infinite scroll real, sticky ads).

### Performance
* **Tiempo de carga:** Muy rápido (TTFB ~1.5s, tamaño total ~36KB iniciales).
* **Renderizado:** CSR (Client-Side Rendering) a través de `app.js`. Esto es un problema grave para SEO.

### SEO Técnico y Estratégico
* **Indexabilidad:** CSR dificulta la indexación inmediata por Googlebot-News.
* **Sitemap/RSS:** Sitemap XML estático desactualizado. El feed RSS (`/rss.xml` o `/feed`) devuelve error 404, bloqueando la sindicación de noticias.
* **Schema.org:** Implementación básica de `NewsMediaOrganization` presente, pero los artículos individuales no generan dinámicamente el esquema `NewsArticle` requerido por Google.
* **EEAT:** Falta profundidad en las biografías de los autores y políticas editoriales visibles para fortalecer la Autoridad.

### Seguridad y Tecnologías
* **Seguridad:** HTTPS activo, pero faltan headers de seguridad avanzados (CSP, X-Frame-Options).
* **Frontend:** Vanilla JS / SPA custom.
* **Backend/DB:** Supabase (PostgreSQL + Auth + Storage).
* **Hosting:** Netlify Edge.
* **Analytics:** No se detectó implementación robusta de Google Analytics 4 (GA4) o Tag Manager en el código base inicial.

---

## CAPÍTULO 4: Benchmark

Comparación con portales similares (ej. Correo Canadiense, The Bridge Canada, NM Noticias):

| Criterio | CBN Noticias | Portales Benchmark | Brecha / Oportunidad |
| :--- | :--- | :--- | :--- |
| **Arquitectura SEO** | CSR (Mala para News) | SSR / SSG (WordPress/Next.js) | Crítica. Migrar a SSR. |
| **Monetización** | Nula en web | Adsense, Patrocinios, Publirreportajes | Alta. Implementar AdManager. |
| **Formatos** | Texto / Imagen | Video nativo, Podcasts, Newsletters | Alta. Integrar multimedia. |
| **Distribución** | Manual (Social) | RSS automático, Google News, AMP | Crítica. Habilitar RSS y sitemaps de noticias. |

---

## CAPÍTULO 5: Diagnóstico Sandler

| Dolor | Causa | Impacto | Evidencia | Recomendación |
| :--- | :--- | :--- | :--- | :--- |
| **Técnico** | Arquitectura SPA/CSR | Google no indexa las noticias rápidamente | Falta de tráfico orgánico en tiempo real | Migrar a SSR (Next.js) |
| **Financiero** | Falta de espacios publicitarios | Cero ingresos directos por tráfico web | No hay banners ni paywalls | Integrar Google Ad Manager |
| **Operativo** | Gestión de contenido manual | Pérdida de tiempo del editor | Uso de Supabase directamente o admin básico | Implementar Headless CMS |
| **Estratégico** | Ausencia en Google News | Pérdida de visibilidad ante la competencia | RSS roto (404) | Optimización estricta para Google Publisher |

---

## CAPÍTULO 6: Riesgos

| Riesgo | Impacto | Probabilidad | Mitigación |
| :--- | :--- | :--- | :--- |
| **Presupuesto limitado del cliente** | Alto | Alta | Ofrecer un enfoque por fases (Quick wins primero). |
| **Caída temporal de tráfico post-migración** | Medio | Media | Plan de migración SEO estricto (Redirecciones 301). |
| **Curva de aprendizaje del nuevo CMS** | Medio | Baja | Capacitación y elección de un CMS intuitivo (ej. Sanity). |

---

## CAPÍTULO 7: Vacíos de Información

1. **Crítico:** Presupuesto disponible para el proyecto y expectativas de retorno de inversión (ROI).
2. **Importante:** Flujo de trabajo actual de publicación (¿Cuánto tiempo toma publicar una nota hoy?).
3. **Deseable:** Métricas internas de tráfico (GA4) para validar los datos de Similarweb.

---

## CAPÍTULO 8: Preguntas para la Reunión

*(Muestra representativa de 15 preguntas clave agrupadas. El informe completo requiere más de 80, aquí se destacan las estratégicas)*

**Negocio y Monetización:**
1. ¿Cuál es el modelo de ingresos principal hoy y cuál es la meta a 3 años?
2. ¿Están dispuestos a incluir publicidad programática o prefieren patrocinios directos?

**Operaciones y CMS:**
3. ¿Cuánto tiempo invierte el equipo en publicar y distribuir una noticia en redes?
4. ¿Qué funcionalidades del publicador actual les causan más frustración?

**SEO y Tráfico:**
5. ¿Qué porcentaje de su tráfico actual proviene de Google Discover o Google News?
6. ¿Tienen acceso a Google Search Console actualmente?

*(Nota: Se desarrollará el listado completo de 80 preguntas en el anexo de la propuesta final).*

---

## CAPÍTULO 9: Arquitectura Recomendada

**Enfoque:** Arquitectura Composable (Headless)

* **Frontend:** Next.js (React) alojado en Vercel. Permite Server-Side Rendering (SSR) e Incremental Static Regeneration (ISR), crucial para la velocidad y SEO de noticias.
* **Headless CMS:** Strapi o Sanity. Provee una interfaz editorial superior, flujos de aprobación y modelado de datos flexible.
* **Base de Datos / Backend:** PostgreSQL (puede mantenerse Supabase si se usa como backend custom, o usar la DB nativa del CMS).
* **Media & CDN:** Cloudinary o Vercel Edge Network para optimización de imágenes (WebP/AVIF).
* **Monetización:** Google Ad Manager (GAM) integrado en el frontend.
* **Analytics:** Google Tag Manager (GTM) + GA4.

---

## CAPÍTULO 10: Roadmap

1. **Fase 1: Discovery & UX/UI (Semanas 1-3)** - Wireframes, definición de taxonomía.
2. **Fase 2: Setup Arquitectura & CMS (Semanas 4-5)** - Configuración de Strapi/Sanity.
3. **Fase 3: Desarrollo Frontend (Semanas 6-9)** - Next.js, componentes, integración de Ads.
4. **Fase 4: Migración & SEO (Semana 10)** - Script de migración desde Supabase, redirecciones 301.
5. **Fase 5: QA, Capacitación & Lanzamiento (Semanas 11-12)** - Pruebas de Core Web Vitals, salida a producción.

---

## CAPÍTULO 11: Estrategia Comercial para KASI

* **Propuesta de Valor:** "Transformamos su portal en una máquina de generación de audiencia y monetización, automatizando la operación técnica para que usted se enfoque en el periodismo."
* **Diferenciador:** Enfoque técnico en SSR y Google News SEO, áreas donde las agencias tradicionales fallan.
* **Manejo de Objeciones (Costo):** Demostrar el ROI. Un portal monetizado paga la inversión a través de nuevos ingresos publicitarios y eficiencia operativa.

---

## CAPÍTULO 12: Propuesta de Transformación Digital

**Visión a 3 Años:**
CBN Noticias evolucionará de un blog informativo a una plataforma multimedia de autoridad.
* **Año 1:** Re-platforming, entrada a Google News, activación de programática.
* **Año 2:** Integración de IA para resúmenes automáticos y traducción (Inglés/Francés); lanzamiento de Newsletter monetizado.
* **Año 3:** Modelo de membresía comunitaria (Suscripciones freemium) y portal de empleo/servicios para hispanos en Canadá.

---

## CAPÍTULO 13: Quick Wins

1. **Reparar el Feed RSS (Prioridad Alta):** Generar un `/feed.xml` válido inmediatamente para permitir sindicación básica.
2. **Implementar GA4 y Search Console (Prioridad Alta):** Si no están configurados correctamente, hacerlo hoy para capturar datos base.
3. **Optimizar Metadatos (Prioridad Media):** Asegurar que cada artículo inyecte dinámicamente el `application/ld+json` de `NewsArticle`.

---

## CAPÍTULO 14: Backlog Priorizado

1. [P1] Setup de entorno Next.js y Vercel.
2. [P1] Modelado de datos en Headless CMS (Articles, Categories, Authors).
3. [P1] Desarrollo de plantillas SSR para Home y Article Detail.
4. [P2] Integración de Google Ad Manager.
5. [P2] Generador dinámico de Sitemaps de Noticias y RSS.
6. [P3] Componente de Newsletter integrado con Mailchimp/Brevo.

---

## CAPÍTULO 15: Estimación del Proyecto

*Estimación de alto nivel (sujeta a validación en Discovery):*
* **Esfuerzo:** 300 - 450 horas hombre.
* **Duración:** 2.5 a 3 meses.
* **Equipo requerido:** 1 PM, 1 UX/UI, 1 Dev Fullstack (Next.js/CMS), 1 Especialista SEO.

---

## CAPÍTULO 16: Score Ejecutivo

* **Dolor (8/10):** El sitio actual limita severamente el crecimiento y los ingresos.
* **Urgencia (7/10):** Pérdida de oportunidad diaria en Google News.
* **Presupuesto (5/10):** Incógnita principal al ser un medio independiente.
* **Complejidad Técnica (4/10):** Baja para KASI, es un stack conocido.
* **Potencial Comercial (8/10):** Excelente caso de estudio para KASI.
* **Score General:** **7.5 / 10** (Oportunidad Altamente Recomendada).

---

## CAPÍTULO 17: Conclusiones Ejecutivas

**¿Debe KASI perseguir esta oportunidad?** Sí. Es un proyecto técnicamente directo con un impacto de negocio masivo para el cliente.
**Principal Riesgo:** Desalineación de presupuesto.
**Principal Oportunidad:** Convertir a CBN Noticias en el líder absoluto de noticias hispanas en Canadá mediante superioridad técnica (SEO/Performance).
**Siguiente Paso:** Presentar los hallazgos de rendimiento y SEO (el problema del CSR y el RSS roto) en la reunión de descubrimiento para generar urgencia técnica, y pivotar hacia la solución Headless.
