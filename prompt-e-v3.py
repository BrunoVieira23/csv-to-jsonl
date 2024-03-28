import csv
import json
import os  # Import os to work with file paths

def get_bottle_details_from_csv(csv_filepath):
    with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        try:
            for row in reader:
                yield row
        except StopIteration:
            print("The CSV file seems to be empty or not formatted correctly.")

def generate_template(bottle):
    return {
        "messages": [
            {
                "role": "system",
                "content": "Als Experte für Spirituosen sind Sie aufgefordert, Produktdetails basierend auf dem angegebenen Flaschennamen zu generieren. Beachten Sie, dass wenn im Flaschennamen die Abkürzung 'y.o.' (für 'years old') verwendet wird, diese in 'Jahre' umgewandelt werden sollte, um der lokalen Konvention zu entsprechen. Für die folgenden Felder verwenden Sie klare und spezifische Informationen, wo immer möglich, und ziehen Sie Ihre Expertise heran, um gebildete Vermutungen zu machen, wenn direkte Informationen nicht verfügbar oder unsicher sind. Bitte lassen Sie jedes Feld leer, wenn die Informationen nicht abgeleitet werden können: Flaschenname (Hier den umgewandelten Flaschennamen einfügen, 'y.o.' durch 'Jahre' ersetzt, wenn zutreffend), Flaschengröße, Fassstärke (antworten Sie mit 'Ja' oder 'Nein'), Nicht kühlgefiltert (antworten Sie mit 'Ja' oder 'Nein'), Allergene, Region, Marke, Abfüller, Serie, Produktkategorie, Produkttyp, Maische. Geben Sie den Flaschennamen [Flaschenname hier einfügen] an und füllen Sie jedes Feld nach bestem Wissen und Gewissen aus, auch durch informierte Vermutungen, um einen umfassenden Überblick über das Produkt zu bieten. Achten Sie darauf, 'y.o.' in 'Jahre' umzuwandeln, um die Angabe dem deutschen Kontext anzupassen."
            },
            {
                "role": "user",
                "content": bottle.get("name", "N/A")
            },
            {
                "role": "assistant",
                "content": (f"- Bottle name: {bottle.get('name', 'N/A')}\n"
                            f"- Bottle size: {bottle.get('Bottle_Size-de_DE-ecommerce', 'N/A')}\n"
                            f"- Cask strength: {bottle.get('Cask_Strength', 'N/A')}\n"
                            f"- Volume: {bottle.get('Volume_fixed', 'N/A')}\n"
                            f"- Not chill-filtered: {bottle.get('Non_Chill_Filtered', 'N/A')}\n"
                            f"- Allergens: {bottle.get('Allergens-de_DE', 'N/A')}\n"
                            f"- Region: {bottle.get('Region-de_DE', 'N/A')}\n"
                            f"- Brand: {bottle.get('Brand-de_DE-ecommerce', 'N/A')}\n"
                            f"- Bottler: {bottle.get('Bottler-de_DE-ecommerce', 'N/A')}\n"
                            f"- Series: {bottle.get('Series', 'N/A')}\n"
                            f"- Product category: {bottle.get('Product_Category-de_DE', 'N/A')}\n"
                            f"- Product type: {bottle.get('Product_Type-de_DE', 'N/A')}\n"
                            f"- Mash Bill: {bottle.get('Mash_Bill-de_DE-ecommerce', 'N/A')}")
            }
        ]
    }

def main():
    csv_filepath = input("Enter the CSV file path: ")
    base, _ = os.path.splitext(csv_filepath)
    output_jsonl_filepath = base + '.jsonl'  # Append '.jsonl' to the input file's base name

    with open(output_jsonl_filepath, 'w', encoding='utf-8') as jsonlfile:
        for bottle_details in get_bottle_details_from_csv(csv_filepath):
            template = generate_template(bottle_details)
            jsonlfile.write(json.dumps(template, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    main()
