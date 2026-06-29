# PROMPT PARA APOLLO.IO: IMPORTACIÓN Y ENRIQUECIMIENTO DE LOS 10 ICPS PRIORIZADOS

## OBJETIVO
Importar los 10 contratistas priorizados (TIER 1) de Metro Vancouver en Apollo.io para enriquecer sus datos de contacto (nombre del dueño, LinkedIn, cargo, tamaño de empresa) y preparar la secuencia de outreach automatizado.

---

## PASO 1: IMPORTAR EL CSV EN APOLLO

1. Inicia sesión en **Apollo.io** → Ve a **People** o **Companies** → Haz clic en **Import**.
2. Selecciona **"Import from CSV"**.
3. Sube el archivo: `top-10-icps-apollo-import.csv`
4. Mapea las columnas de la siguiente manera:

| Columna del CSV | Campo de Apollo |
|:---|:---|
| `Company Name` | **Company Name** |
| `Website URL` | **Company Website** |
| `Phone Number` | **Company Phone** |
| `Email Address` | **Email** |
| `City / Location` | **City** |
| `Specialization` | **Tag** o **Custom Field** |
| `Google Maps Reviews` | **Custom Field** (crear campo "Google Reviews") |
| `Priority Tier` | **Tag** |

5. Haz clic en **Import** y espera a que Apollo procese los registros.

---

## PASO 2: ENRIQUECER CON APOLLO (ENCONTRAR AL DUEÑO)

Una vez importadas las empresas, Apollo intentará automáticamente vincular los dominios web con perfiles de LinkedIn y encontrar a los tomadores de decisiones.

1. Ve a la lista importada → Haz clic en cada empresa.
2. Busca los contactos vinculados con los siguientes cargos:
   - **Owner**
   - **Founder**
   - **President**
   - **General Manager**
   - **Operations Manager**
3. Agrega a los contactos encontrados a una **Sequence** (secuencia de outreach).

---

## PASO 3: BÚSQUEDA AVANZADA EN APOLLO (AMPLIAR EL PIPELINE)

Si quieres encontrar más contratistas similares a los 10 importados, usa estos filtros en Apollo Search:

### Filtros de Búsqueda:
- **Job Titles:** Owner, Founder, President, General Manager
- **Industry:** Construction, Plumbing, HVAC, Mechanical Contracting
- **Company Headcount:** 1-50 employees
- **Location:** Vancouver, BC, Canada (Radio: 50 km)
- **Keywords:** heating, plumbing, boiler, furnace, pool, irrigation, HVAC, sprinkler

### Filtros de Exclusión:
- Excluir empresas con más de 50 empleados (son demasiado grandes).
- Excluir cargos: Marketing Manager, Sales Rep (no son tomadores de decisiones).

---

## PASO 4: CREAR LA SECUENCIA DE OUTREACH

Una vez identificados los dueños, crear una secuencia de correo electrónico automatizada con el siguiente flujo:

### Email 1 (Día 1) — El Gancho de Dolor:
**Subject:** Your Google Maps ranking for "[keyword]" in [City]

> Hi [First Name],
>
> I noticed [Company Name] is currently on page 2 of Google Maps for "[boiler repair / pool service] in [City]." With winter approaching in just 60 days, that means potential emergency calls are going to your competitors first.
>
> We help local contractors in Metro Vancouver get into the Top 3 on Google Maps through organic SEO optimization and an automated review system that asks your customers for 5-star reviews via SMS right after you finish a job.
>
> Would you be open to a quick 10-minute call this week to see if this could work for [Company Name]?
>
> Best,
> Luis Gabriel Niño
> KASI — Kroma AI Systems Inc.

### Email 2 (Día 3) — Follow-up con Dato Duro:
**Subject:** Re: Your Google Maps ranking

> Hi [First Name],
>
> Just following up. I ran a quick speed test on your website — it loads in [X] seconds on mobile. In our experience with contractors in BC, sites that load over 3 seconds lose about 40% of emergency callers before the page even finishes loading.
>
> Happy to show you a quick prototype of what a faster landing page would look like for [Company Name]. No cost, no obligation.
>
> Luis

### Email 3 (Día 7) — Breakup Email:
**Subject:** Should I close your file?

> Hi [First Name],
>
> I haven't heard back, so I don't want to keep bothering you. If optimizing your Google Maps visibility isn't a priority right now, totally understood — I'll close your file on my end.
>
> If things change before the heating season kicks in, feel free to reach out anytime.
>
> All the best,
> Luis
