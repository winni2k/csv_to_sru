import io
from csv_to_sru import convert_csv_to_sru


def test_conversion_with_sample_data():
    # Input data as a string
    input_data = "Beteckning,Antal,Försjälningspris,Omkostnadsbelopp,Vinst/Förlust\nPG,10,1000,10,990\nPG2,1,1000,1,999\n"
    # Use StringIO for both input and output
    input_file = io.StringIO(input_data)
    output_file = io.StringIO()

    # Expected output
    expected_output = """#BLANKETT K4-2023P4
#IDENTITET 123123123123 20240329 210540
#NAMN Jane Doe
#UPPGIFT 3100 10
#UPPGIFT 3101 PG
#UPPGIFT 3102 1000
#UPPGIFT 3103 10
#UPPGIFT 3104 990
#UPPGIFT 7014 1
#BLANKETTSLUT
#BLANKETT K4-2023P4
#IDENTITET 123123123123 20240329 210540
#NAMN Jane Doe
#UPPGIFT 3100 1
#UPPGIFT 3101 PG2
#UPPGIFT 3102 1000
#UPPGIFT 3103 1
#UPPGIFT 3104 999
#UPPGIFT 7014 2
#BLANKETTSLUT
#FIL_SLUT"""

    # Run the conversion with specific date and time for testing, using StringIO objects
    convert_csv_to_sru(
        input_file,
        output_file,
        "123123123123",
        "Jane Doe",
        date="20240329",
        time="210540",
    )

    # Retrieve the content of the output
    output_content = output_file.getvalue()
    assert expected_output.strip() == output_content.strip()


def test_output_file_creation():
    """Test if the output is created successfully with dummy data."""
    # Dummy input data
    input_data = "Beteckning,Antal,Försjälningspris,Omkostnadsbelopp,Vinst/Förlust\nTEST,1,100,10,90\n"
    identity_number = "000000000000"
    name = "Test Name"

    # Use StringIO for input and output to simulate file reading/writing
    input_file = io.StringIO(input_data)
    output_file = io.StringIO()

    # Run the conversion with fixed date and time for consistency in tests
    convert_csv_to_sru(
        input_file, output_file, identity_number, name, date="20200101", time="010101"
    )

    # Retrieve the output content
    content = output_file.getvalue()

    # Assert that the expected strings are in the content
    assert "#IDENTITET 000000000000 20200101 010101" in content
    assert "#NAMN Test Name" in content


def test_loss():
    """Test if the converter properly handles losses."""
    # Dummy input data
    input_data = "Beteckning,Antal,Försjälningspris,Omkostnadsbelopp,Vinst/Förlust\nTEST,1,100,120,-20\n"
    identity_number = "000000000000"
    name = "Test Name"

    # Use StringIO for input and output to simulate file reading/writing
    input_file = io.StringIO(input_data)
    output_file = io.StringIO()

    # Run the conversion with fixed date and time for consistency in tests
    convert_csv_to_sru(input_file, output_file, identity_number, name)

    # Retrieve the output content
    content = output_file.getvalue()

    # Assert that the expected strings are in the content
    assert "#UPPGIFT 3104" not in content
    assert "#UPPGIFT 3105 20" in content
