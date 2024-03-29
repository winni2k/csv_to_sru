import csv
from datetime import datetime
import click

# Simplified SRU file template for each record
SRU_TEMPLATE_1 = """#BLANKETT K4-2023P4
#IDENTITET {identity} {date} {time}
#NAMN {name}
#UPPGIFT 3100 {quantity}
#UPPGIFT 3101 {designation}
#UPPGIFT 3102 {sales_price}
#UPPGIFT 3103 {cost}
"""

SRU_TEMPLATE_2 = """#UPPGIFT 7014 {index}
#BLANKETTSLUT
"""


def convert_csv_to_sru(
    input_file, output_file, identity_number, name, date=None, time=None
):
    """
    Converts a given CSV file to an SRU format file with customizable parameters.

    Parameters:
    - input_file_name: The name of the input CSV file.
    - output_file: A file-like object where the SRU output will be written.
    - identity_number: The identity number to use in the SRU file.
    - name: The name to use in the SRU file.
    - date: The date to use in the SRU file, defaults to current date if None.
    - time: The time to use in the SRU file, defaults to current time if None.
    """
    # Default to current date and time if not provided
    if date is None:
        date = datetime.now().strftime("%Y%m%d")
    if time is None:
        time = datetime.now().strftime("%H%M%S")

    csv_reader = csv.DictReader(input_file)
    sru_records = []

    for index, row in enumerate(csv_reader, start=1):
        sru_record = SRU_TEMPLATE_1.format(
            identity=identity_number,
            date=date,
            time=time,
            name=name,
            quantity=row["Antal"],
            designation=row["Beteckning"],
            sales_price=row["Försjälningspris"],
            cost=row["Omkostnadsbelopp"],
        )
        profit_loss = int(row["Vinst/Förlust"])
        if profit_loss >= 0:
            sru_record += f"#UPPGIFT 3104 {profit_loss}\n"
        else:
            sru_record += f"#UPPGIFT 3105 {abs(profit_loss)}\n"
        sru_record += SRU_TEMPLATE_2.format(index=index)
        sru_records.append(sru_record)

    final_output = "".join(sru_records) + "#FIL_SLUT"

    output_file.write(final_output)


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
@click.option(
    "--identity", required=True, help="The identity number to use in the SRU file."
)
@click.option("--name", required=True, help="The name to use in the SRU file.")
def cli(input_file, output_file, identity, name):
    """
    Converts a CSV file to an SRU format file based on provided parameters.
    """
    current_date = datetime.now().strftime("%Y%m%d")
    current_time = datetime.now().strftime("%H%M%S")

    with open(input_file, "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as outfile:
        convert_csv_to_sru(
            infile, outfile, identity, name, date=current_date, time=current_time
        )

    click.echo(f"Conversion complete. Output saved to {output_file}")


if __name__ == "__main__":
    cli()
