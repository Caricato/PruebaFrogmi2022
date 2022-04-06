# Tiendas e Incidentes

Desarrollado en Python, y se usarán las siguientes clases:

- Store
- Incident

## Especificación de Store:

Atributos:
- incidents: Lista de objetos de tipo Incidente

Métodos:

incident_status (init_date, end_date):

Método que devuelve el estado actual de incidentes en un rango de fechas válido.

Parámetros:
- init_date: Cadena de texto en formato "dd/mm/YYYY" que describa una fecha de inicio válida.
- end_date: Cadena de texto en formato "dd/mm/YYYY" que describa una fecha de fin válida. Debe ser mayor que init_date

Excepciones:

ValueError -- Si se envía una fecha con formato distinto a "dd/mm/YYYY" como alguno de los parámetros

InvalidDateRange -- Si el rango de fechas no es un rango válido

## Especificación de Incident:
Atributos:
- description: Descripción del incidente ocurrido
- action_to_solve: Descripción de la acción a realizar para resolver el incidente
- open_date: Fecha en la cual se registró el incidente, en formato "dd/mm/YYYY"
- state: Estado actual del incidente, puede ser "open" o "solved"
- solved_date = Fecha en la cual se resolvió el incidente

Métodos:

solve_incident (solved_date):

Método que soluciona un incidente abierto.

Parámetros:
- solved_date: Cadena de texto en formato "dd/mm/YYYY" que describa una fecha de inicio válida.

Excepciones:

ValueError -- Si se envía una fecha con formato distinto a "dd/mm/YYYY" como alguno de los parámetros

InvalidDateRange -- Si solved_date es menor a open_date