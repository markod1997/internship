import csv
import re

# Function to annotate entities in generated texts
def annotate_entities(people_csv, countries_csv, organizations_csv, generated_texts_csv, output_file):
    # Load people's names from the people.csv file
    with open(people_csv, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        people_names = set()
        for row in reader:
            first_name = row['first_name']
            last_name = row['last_name']
            people_names.add((first_name, last_name))

    # Load country names from the Places_list.csv file
    with open(countries_csv, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        place_names = set()
        for row in reader:
            place_name = row['0']
            place_names.add(place_name)

    # Load organization names from Organizations_list.csv file
    with open(organizations_csv, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        organization_names = set()
        for row in reader:
            organization_name = row['0']
            organization_names.add(organization_name)

    # Process the Generated_texts.csv file and annotate names, countries, and organizations
    with open(generated_texts_csv, 'r') as textfile:
        texts = textfile.readlines()

    annotated_texts = []
    for text in texts:
        # Annotate people's names
        for first_name, last_name in people_names:
            pattern = re.compile(fr"\b({re.escape(first_name)}\s{re.escape(last_name)}|{re.escape(last_name)}\s{re.escape(first_name)})\b", re.IGNORECASE)
            text = re.sub(pattern, r'<PERSON>\g<0></PERSON>', text)

        # Annotate place names
        for place_name in place_names:
            pattern = re.compile(fr"\b{re.escape(place_name)}\b")
            matches = pattern.finditer(text)
            matches = sorted(matches, key=lambda x: x.start(), reverse=True)
            for match in matches:
                start_index = match.start()
                end_index = match.end()
                if not any(tag in range(start_index, end_index) for tag in ['<PLACE>', '</PLACE>']):
                    text = text[:start_index] + f"<PLACE>{match.group()}</PLACE>" + text[end_index:]

        # Get rid of nested tags
        text = re.sub(r"<PLACE>(.*?)<PLACE>", r"<PLACE>\1", text)
        text = re.sub(r"</PLACE>(.*?)</PLACE>", r"</PLACE>\1", text)

        # Annotate organization names
        for organization_name in organization_names:
            pattern = re.compile(fr"\b{re.escape(organization_name)}\b")
            text = re.sub(pattern, r'<ORGANIZATION>\g<0></ORGANIZATION>', text)

        annotated_texts.append(text)

    # Save annotated texts to the output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(annotated_texts)

# Call the annotate_entities function with the provided CSV files
annotate_entities('People_list.csv', 'Places_list.csv', 'Organizations_list.csv', 'Generated_texts.csv', 'Annotated_texts.csv')

