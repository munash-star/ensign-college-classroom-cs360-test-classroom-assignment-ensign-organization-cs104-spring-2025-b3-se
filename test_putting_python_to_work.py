import subprocess
import math

# Command to execute your Python script
command = ["python", "putting_python_to_work.py"]
# Input data to be sent to the program
input_data = "5\n"

def test_diameter():
    # Execute the command and capture stdout and stderr
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send input data to the program
    stdout, stderr = process.communicate(input=input_data)

    # Calculate expected diameter
    radius = float(input_data.strip())
    expected_diameter = 2 * radius

    # Check if the printed output contains the correct diameter value
    assert f"{expected_diameter}" in stdout.strip()

def test_circumference():
    # Execute the command and capture stdout and stderr
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send input data to the program
    stdout, stderr = process.communicate(input=input_data)

    # Calculate expected circumference for both 3.14 and math.pi
    radius = float(input_data.strip())
    expected_circumference_314 = 2 * 3.14 * radius
    expected_circumference_math_pi = 2 * math.pi * radius

    # Check if the printed output contains the correct circumference value (either using 3.14 or math.pi)
    assert (f"{expected_circumference_314}" in stdout.strip() or f"{expected_circumference_math_pi}" in stdout.strip())

def test_area():
    # Execute the command and capture stdout and stderr
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send input data to the program
    stdout, stderr = process.communicate(input=input_data)

    # Calculate expected area for both 3.14 and math.pi
    radius = float(input_data.strip())
    expected_area_314 = 3.14 * radius**2
    expected_area_math_pi = math.pi * radius**2

    # Check if the printed output contains the correct area value (either using 3.14 or math.pi)
    assert (f"{expected_area_314}" in stdout.strip() or f"{expected_area_math_pi}" in stdout.strip())

def test_print_statement():
    # Execute the command and capture stdout and stderr
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send input data to the program
    stdout, stderr = process.communicate(input=input_data)

    # Convert stdout to lowercase for case-insensitive comparison
    stdout_lower = stdout.lower()

    # Check if the final printed message contains information about the diameter, circumference, and area
    assert "diameter" in stdout_lower.strip()
    assert "circumference" in stdout_lower.strip()
    assert "area" in stdout_lower.strip()
