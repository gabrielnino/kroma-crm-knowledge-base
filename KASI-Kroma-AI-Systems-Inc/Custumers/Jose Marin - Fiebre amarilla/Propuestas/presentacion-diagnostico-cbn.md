# PROPUESTA DE PRESENTACIÓN ESTRATÉGICA: CBN NOTICIAS
**Cliente:** José Marín  
**Fecha:** Domingo 28 de Junio de 2026, 9:00 AM  
**Enfoque de Ventas:** Sandler (Suave con la persona, riguroso con el problema. Cero confrontación, alto valor percibido).  
**Formato sugerido para Luis:** Presentación en pantalla (compartiendo ventana) o resumen ejecutivo verbal.

---

# ESTRUCTURA DE LA PRESENTACIÓN (SLIDES EN MARKDOWN)

```carousel
## Diapositiva 1: Portada e Identidad
### CBN NOTICIAS: Maximizando la voz hispana en Canadá
* **El Reconocimiento Inicial:** CBN Noticias es el único medio digital en español que cubre noticias locales serias en Vancouver y British Columbia.
* **El Objetivo de hoy:** Analizar cómo la tecnología actual puede respaldar el éxito y liderazgo editorial que CBN ya tiene en la comunidad.
* **Enfoque Sandler:** Validar al cliente. Iniciar reconociendo su éxito y su estatus para desarmar cualquier actitud defensiva.
<!-- slide -->
## Diapositiva 2: El Concepto de "Fricción Invisible"
### ¿Por qué las buenas noticias a veces no llegan a todos?
* **El Fenómeno:** La calidad del contenido editorial de CBN es excelente, pero la plataforma técnica actual experimenta "fricción invisible" (lentitud en móviles, fallos de indexación).
* **El Enfoque Técnico Amigable:** No es un error de gestión, sino una limitación del sistema actual (WordPress tradicional), que fue diseñado para la web de hace una década y no para las exigencias de velocidad de hoy.
* **Enfoque Sandler:** "Despersonalizar el problema". El problema no es de José, es de la tecnología obsoleta que utiliza su CMS actual.
<!-- slide -->
## Diapositiva 3: Los Tres Pilares de Optimización
### 1. Velocidad de Conexión en Móviles (LCP)
* **La Realidad:** Google indica que los lectores móviles esperan que un sitio cargue en menos de 2 segundos. Actualmente, CBN Noticias toma alrededor de 3.8 segundos en teléfonos debido a la carga de scripts externos en el navegador (Client-Side Rendering).
* **La Oportunidad:** Mudar el procesamiento al servidor para que el lector móvil reciba la noticia de forma instantánea (< 1.0s), mejorando la retención de usuarios en redes de datos móviles.
<!-- slide -->
## Diapositiva 4: Los Tres Pilares de Optimización
### 2. Estabilidad Visual y Experiencia del Lector (CLS)
* **La Realidad:** Al cargar la página, el contenido a veces "salta" o se desplaza (CLS de 0.66). Esto ocurre comúnmente cuando los anuncios o imágenes no tienen espacios reservados de tamaño fijo en el diseño.
* **La Oportunidad:** Rediseñar la maquetación para dar estabilidad absoluta al texto. Esto evita clics accidentales y mejora la lectura de artículos largos, aumentando el tiempo de permanencia en la web.
<!-- slide -->
## Diapositiva 5: Los Tres Pilares de Optimización
### 3. Compartido Efectivo en Redes Sociales (Open Graph)
* **La Realidad:** Cuando un lector comparte un enlace de CBN Noticias por WhatsApp o Facebook, a menudo se muestra una imagen genérica del home en lugar de la foto específica de la noticia.
* **La Oportunidad:** Inyectar metadatos dinámicos automáticos. Al compartir, la vista previa mostrará la foto del suceso y el título exacto de la nota, incrementando los clics desde redes hasta en un 40%.
<!-- slide -->
## Diapositiva 6: Alineación con el Modelo de Negocio
### Mayor visibilidad = Mayor valor para los patrocinadores
* **Publicidad Eficiente:** Los banners de agencias de inmigración y escuelas de inglés cargarán de inmediato junto con la noticia. No habrá "cargas fantasma" donde el lector pasa de largo antes de ver la publicidad.
* **Posicionamiento Geocalizado:** Al superar a los medios nacionales lentos del este en velocidad móvil, CBN se posiciona como el canal premium exclusivo para marcas que buscan audiencias en Vancouver y BC.
<!-- slide -->
## Diapositiva 7: La Ruta Tecnológica Propuesta
### Arquitectura Moderna, Segura y Autogestionable
* **Desarrollo a la Medida (Astro + Supabase):** Una web ultrarrápida que pre-renderiza las noticias como páginas estáticas seguras. Las credenciales y bases de datos se ocultan de forma segura en el servidor.
* **Facilidad Editorial:** Mantener una interfaz sencilla para que los redactores publiquen noticias de última hora sin complicaciones técnicas.
<!-- slide -->
## Diapositiva 8: Preguntas de Acuerdo Mutuo (Cierre Sandler)
### ¿Cómo te gustaría proceder?
* *"José, basándonos en esto, si logramos que CBN cargue de forma instantánea y resuelva el problema de las imágenes en redes sociales, ¿crees que te ayudaría a capturar más anunciantes en Vancouver?"*
* *"¿Cómo te sientes respecto a la dependencia técnica que tienes hoy para hacer estos cambios en la página?"*
* *"Si decidimos avanzar en una propuesta, ¿qué tiempos o presupuestos tendríamos que respetar para que esto sea viable para ti?"*
```

---

# GUÍA DE COMUNICACIÓN PARA LUIS (TÉCNICA DE ENTRENAMIENTO SANDLER)

Para que José no se sienta atacado en su rol de director, Luis debe usar las siguientes **técnicas de suavizado lingüístico** durante la reunión:

### 1. El uso del "Tercer Personaje" (Storytelling)
En lugar de decirle: *"Tu página web es muy lenta y aleja a los lectores"*, se debe decir:  
> *"Nos pasa mucho con portales de noticias dinámicos en Vancouver. El software actual (WordPress/Supabase clásico) tiende a sobrecargarse de scripts con el tiempo y empieza a tardar en móviles. Los directores de medios se frustran porque escriben notas excelentes pero notan que el tráfico en móviles no sube al ritmo esperado. ¿Te pasa algo similar con CBN?"*

### 2. Validar antes de diagnosticar (El Rol de Consigliere)
Antes de mostrar las métricas de velocidad, Luis debe validar el esfuerzo de José:  
> *"José, felicidades por el posicionamiento de CBN. He visto que en temas locales de Vancouver eres el primero en cubrir sucesos de última hora. Se nota la dedicación y el valor que le das a la comunidad. Lo que queremos ver hoy es cómo hacer que tu plataforma tecnológica sea tan ágil como tu equipo editorial."*

### 3. Evitar la jerga técnica hostil
* En lugar de **"Client-Side Rendering ineficiente"**, decir: *"La página se construye en el teléfono del lector en lugar de venir ya lista desde el servidor, lo cual consume sus datos de navegación"*.
* En lugar de **"Error crítico de CLS"**, decir: *"El diseño tiene pequeños movimientos al cargar mientras acomoda la publicidad, y queremos estabilizarlo para que sea más cómodo de leer"*.
* En lugar de **"Supabase expuesto"**, decir: *"Queremos blindar la conexión de la base de datos para que ningún bot de la competencia intente descargar tus contenidos de forma automática"*.
