def get_bottle_details():
    """Prompts user for bottle details and returns a dictionary."""
    print("Please enter the bottle details:")
    name = input("Name: ")
    size = input("Size (e.g., 500ml): ")
    cask_strength = input("Cask Strength (Ja/Nein): ")
    chill_filtered = input("Chill Filtered (Ja/Nein): ")
    allergens = input("Allergens: ")
    region = input("Region: ")
    brand = input("Brand: ")
    bottler = input("Bottler: ")
    series = input("Series: ")
    category = input("Product Category (e.g., Whisky): ")
    type = input("Product Type (e.g., Single Malt): ")
    mash_bill = input("Mash Bill: ")
    
    return {
        "name": name,
        "size": size,
        "cask_strength": cask_strength,
        "chill_filtered": chill_filtered,
        "allergens": allergens,
        "region": region,
        "brand": brand,
        "bottler": bottler,
        "series": series,
        "category": category,
        "type": type,
        "mash_bill": mash_bill
    }

def generate_template(bottle):
    """Generates and prints the template for a single bottle."""
    template = {
        "messages": [
            {
                "role": "system",
                "content": ("Als Experte für Spirituosen sind Sie aufgefordert, Produktdetails basierend auf dem angegebenen Flaschennamen zu generieren. "
                            "Beachten Sie, dass wenn im Flaschennamen die Abkürzung 'y.o.' (für 'years old') verwendet wird, diese in 'Jahre' umgewandelt werden sollte, "
                            "um der lokalen Konvention zu entsprechen. Für die folgenden Felder verwenden Sie klare und spezifische Informationen, wo immer möglich, und "
                            "ziehen Sie Ihre Expertise heran, um gebildete Vermutungen zu machen, wenn direkte Informationen nicht verfügbar oder unsicher sind. "
                            "Bitte lassen Sie jedes Feld leer, wenn die Informationen nicht abgeleitet werden können: Flaschenname (Hier den umgewandelten Flaschennamen "
                            "einfügen, 'y.o.' durch 'Jahre' ersetzt, wenn zutreffend), Flaschengröße, Fassstärke (antworten Sie mit 'Ja' oder 'Nein'), Nicht kühlgefiltert "
                            "(antworten Sie mit 'Ja' oder 'Nein'), Allergene, Region, Marke, Abfüller, Serie, Produktkategorie, Produkttyp, Maische. Geben Sie den Flaschennamen "
                            "[Flaschenname hier einfügen] an und füllen Sie jedes Feld nach bestem Wissen und Gewissen aus, auch durch informierte Vermutungen, um einen "
                            "umfassenden Überblick über das Produkt zu bieten. Achten Sie darauf, 'y.o.' in 'Jahre' umzuwandeln, um die Angabe dem deutschen Kontext anzupassen.")
            },
            {
                "role": "user",
                "content": bottle["name"]
            },
            {
                "role": "assistant",
                "content": (f"- Bottle name: {bottle['name']}\n"
                            f"- Bottle size: {bottle['size']}\n"
                            f"- Cask strength: {bottle['cask_strength']}\n"
                            f"- Not chill-filtered: {bottle['chill_filtered']}\n"
                            f"- Allergens: {bottle['allergens']}\n"
                            f"- Region: {bottle['region']}\n"
                            f"- Brand: {bottle['brand']}\n"
                            f"- Bottler: {bottle['bottler']}\n"
                            f"- Series: {bottle['series']}\n"
                            f"- Product category: {bottle['category']}\n"
                            f"- Product type: {bottle['type']}\n"
                            f"- Mash Bill: {bottle['mash_bill']}")
            }
        ]
    }
    print(template)

# Main loop to continuously get bottle details and generate templates.
while True:
    bottle_details = get_bottle_details()
    generate_template(bottle_details)
cd 