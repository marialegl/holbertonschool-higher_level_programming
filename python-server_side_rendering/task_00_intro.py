import os

def generate_invitations(template, attendees):
    # Verificar tipos de entrada
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Verificar si la plantilla está vacía
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    
    # Verificar si la lista de asistentes está vacía
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Procesar cada asistente
    for idx, attendee in enumerate(attendees, start=1):
        output = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, "N/A") if attendee.get(key) is not None else "N/A"
            output = output.replace(f'{{{key}}}', value)

        # Escribir el archivo de salida
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as file:
            file.write(output)

        print(f"Generated {output_filename}")
