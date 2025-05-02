import requests
import json

# Obtener los datos desde la URL del JSON (usando la URL raw de GitHub)
url = "https://raw.githubusercontent.com/Te-k/telegram-transparency/main/dataset.json"
response = requests.get(url)
data = response.json()

# Diccionario de códigos de país Alfa-3 a nombres completos y sus respectivas banderas
country_codes = {
    "FRA": ("Francia", "🇫🇷"),
    "USA": ("Estados Unidos", "🇺🇸"),
    "NLD": ("Países Bajos", "🇳🇱"),
    "DEU": ("Alemania", "🇩🇪"),
    "ROU": ("Rumania", "🇷🇴"),
    "POL": ("Polonia", "🇵🇱"),
    "ITA": ("Italia", "🇮🇹"),
    "ESP": ("España", "🇪🇸"),
    "GBR": ("Reino Unido", "🇬🇧"),
    "SVK": ("Eslovaquia", "🇸🇰"),
    "CZE": ("República Checa", "🇨🇿"),
    "BEL": ("Bélgica", "🇧🇪"),
    "CAN": ("Canadá", "🇨🇦"),
    "UKR": ("Ucrania", "🇺🇦"),
    "COL": ("Colombia", "🇨🇴"),
    "URY": ("Uruguay", "🇺🇾"),
    "GEO": ("Georgia", "🇬🇪"),
    "EGY": ("Egipto", "🇪🇬"),
    "SWE": ("Suecia", "🇸🇪"),
    "CHE": ("Suiza", "🇨🇭"),
    "ARG": ("Argentina", "🇦🇷"),
    "AUT": ("Austria", "🇦🇹"),
    "ISR": ("Israel", "🇮🇱"),
    "IRL": ("Irlanda", "🇮🇪"),
    "SVN": ("Eslovenia", "🇸🇮"),
    "IND": ("India", "🇮🇳"),
    "CHL": ("Chile", "🇨🇱"),
    "NOR": ("Noruega", "🇳🇴"),
    "NZL": ("Nueva Zelanda", "🇳🇿"),
    "GTM": ("Guatemala", "🇬🇹"),
    "RUS": ("Rusia", "🇷🇺"),
    "PRT": ("Portugal", "🇵🇹"),
    "BGR": ("Bulgaria", "🇧🇬"),
    "DNK": ("Dinamarca", "🇩🇰"),
    "PHL": ("Filipinas", "🇵🇭"),
    "IDN": ("Indonesia", "🇮🇩"),
    "MYS": ("Malasia", "🇲🇾"),
    "MEX": ("México", "🇲🇽"),
    "CRI": ("Costa Rica", "🇨🇷"),
    "BRA": ("Brasil", "🇧🇷"),
    "ARE": ("Emiratos Árabes Unidos", "🇦🇪"),
    "UZB": ("Uzbekistán", "🇺🇿"),
    "EST": ("Estonia", "🇪🇪"),
    "NGA": ("Nigeria", "🇳🇬"),
    "SRB": ("Serbia", "🇷🇸"),
    "KAZ": ("Kazajistán", "🇰🇿"),
    "THA": ("Tailandia", "🇹🇭"),
    "LAO": ("Laos", "🇱🇦"),
    "ARM": ("Armenia", "🇦🇲"),
    "TUR": ("Turquía", "🇹🇷"),
    "MLT": ("Malta", "🇲🇹"),
    "BLR": ("Bielorrusia", "🇧🇾"),
    "LTU": ("Lituania", "🇱🇹"),
    "BIH": ("Bosnia y Herzegovina", "🇧🇦"),
    "LVA": ("Letonia", "🇱🇻"),
    "HRV": ("Croacia", "🇭🇷"),
    "KGZ": ("Kirguistán", "🇰🇬"),
    "AUS": ("Australia", "🇦🇺"),
    "FIN": ("Finlandia", "🇫🇮"),
    "HUN": ("Hungría", "🇭🇺"),
    "CYP": ("Chipre", "🇨🇾"),
    "MNE": ("Montenegro", "🇲🇪"),
    "JPN": ("Japón", "🇯🇵"),
    "GRC": ("Grecia", "🇬🇷"),
    "LBY": ("Libia", "🇱🇾"),
    "KOR": ("Corea del Sur", "🇰🇷"),
    "NER": ("Níger", "🇳🇪"),
    "GRL": ("Groenlandia", "🇬🇱"),
    "COK": ("Islas Cook", "🇨🇰"),
    "MRT": ("Mauritania", "🇲🇷"),
    "BGD": ("Bangladés", "🇧🇩"),
    "SLV": ("El Salvador", "🇸🇻"),
    "CHN": ("China", "🇨🇳"),
    "MDA": ("Moldavia", "🇲🇩"),
    "ISL": ("Islandia", "🇮🇸"),
    "SGP": ("Singapur", "🇸🇬"),
    "ETH": ("Etiopía", "🇪🇹")
}

# Función para formatear los datos de un país en un mensaje legible
def format_country_data(country_code, country_data):
    country_name, flag = country_codes.get(country_code, (country_code, "🏳️"))  # Obtener nombre y bandera
    message = f"Transparency Report for {country_name} {flag}\n\n"
    
    for entry in country_data:
        date_range = f"{entry['from']} to {entry['to']}"
        requests_count = entry['requests']
        users_count = entry['users']
        
        message += f"Period: {date_range}\n"
        message += f"Requests: {requests_count}\n"
        message += f"Users: {users_count}\n"
        message += "----------------------------------------\n"
    
    return message

# Función para mostrar los datos en consola
def show_country_report():
    first_time = True  # Variable para saber si es la primera vez que se muestra el listado de países
    while True:
        if first_time:
            print("Selecciona un país para ver su reporte:")
            
            # Listar todos los países disponibles
            for idx, country_code in enumerate(data.keys()):
                country_name, flag = country_codes.get(country_code, (country_code, "🏳️"))  # Obtener nombre y bandera
                print(f"{idx + 1}. {country_name} {flag}")
            
            first_time = False  # Después de la primera vez, cambia el estado
        else:
            print("\nAhora selecciona un país por número para ver su reporte (o 0 para salir):")
        
        # Solicitar al usuario seleccionar un país
        try:
            choice = int(input("Escribe el número del país (o 0 para salir): ")) - 1
            if choice == -1:
                print("Saliendo del programa...")
                break
            
            country_code = list(data.keys())[choice]
            
            # Obtener los datos del país seleccionado
            country_data = data.get(country_code, [])
            
            if country_data:
                # Formatear los datos del país
                formatted_message = format_country_data(country_code, country_data)
                print(formatted_message)
            else:
                print(f"No hay datos disponibles para {country_code}.")
        
        except (ValueError, IndexError):
            print("Opción no válida. Por favor, elige un número válido.")

# Función principal
def main():
    show_country_report()

if __name__ == "__main__":
    main()

