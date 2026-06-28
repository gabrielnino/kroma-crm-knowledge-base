# REGLAS DE OPERACIÓN (WORKSPACE RULES)

## 1. Detección y Procesamiento de Nuevos Clientes
*   **Regla de Eficiencia de Escaneo:** Cuando el Estratega indique que hay un cliente nuevo en el espacio de trabajo, el agente **NO** debe recorrer ni escanear todas las carpetas y archivos de la base de datos de manera redundante.
*   **Consulta del Changelog:** El agente debe dirigirse de forma directa y exclusiva a los archivos `change-log.md` de cada cliente para identificar rápidamente las mutaciones, adiciones de nuevos documentos y cambios recientes en el pipeline, optimizando el procesamiento de tokens y el tiempo de respuesta.
