import pdfplumber
import csv

def process(input_pdf, output_csv, password=None):
    pdf = pdfplumber.open(input_pdf, password=password)
    pages = pdf.pages

    total_amount = 0.0
    indian = []
    foreign = []

    for page in pages:
        text = page.extract_text()
        if "Domestic Transactions" in text:
            print("Domestic")

            for index, row in enumerate(page.extract_table()):
                if index == 0 or not row[0]:
                    continue

                amount_index = len(row) - 2
                amount_value = row[amount_index].replace("Cr", "").replace(",", "").strip()

                indian.append({
                    "date": row[0].replace("null", ""),
                    "description": row[1],
                    "currency": "INR",
                    "forex_amount": "",
                    "forex_rate": "",
                    "amount": amount_value,
                    "type": "Cr" if "Cr" in row[amount_index] else "Dr"
                })
        
                total_amount += float(amount_value) if "Dr" in row[amount_index] else -float(amount_value)

        elif "International Transactions" in text:
            print("Foreign")

            table_settings = {
                "explicit_vertical_lines": [380]  # Adjust based on PDF structure
            }

            for index, row in enumerate(page.extract_table(table_settings=table_settings)):
                if index == 0 or not row[0]:
                    continue
                
                amount_index = len(row) - 2
                forex_amount = row[2][4:].replace(",", "")
                amount_value = row[amount_index].replace("Cr", "").replace(",", "").strip()

                foreign.append({
                    "date": row[0].replace("null", ""),
                    "description": row[1],
                    "currency": row[2][:3],
                    "forex_amount": forex_amount,
                    "forex_rate": '%.2f' % (float(amount_value) / float(forex_amount) if forex_amount else 1),
                    "amount": amount_value,
                    "type": "Cr" if "Cr" in row[amount_index] else "Dr"
                })

                total_amount += float(amount_value) if "Dr" in row[amount_index] else -float(amount_value)

    print("Processed " + input_pdf + ". Total due should be " + str(total_amount))

    # Output to CSV
    combined = indian + foreign

    fields = ["date", "currency", "description", "forex_amount", "forex_rate", "amount", "type"]
    with open(output_csv, 'w') as file:
        writer = csv.DictWriter(file, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL, fieldnames=fields)
        writer.writeheader()

        for row in combined:
            writer.writerow({key: row[key] for key in fields})

if __name__ == '__main__':
    # File paths
    input_pdf = "input.pdf"
    output_csv = "output.csv"
    password = None  # Add password if required

    # Call process function
    process(input_pdf, output_csv, password)
