import serial

# Configure the serial port
ser = serial.Serial('COM3', 115200, timeout=1)  # Replace 'COM3' with your Arduino's port

def display_sensor_status(sensor_states):
    """
    Display which sensor is ON (LOW state).
    """
    for i, state in enumerate(sensor_states, start=1):
        if state == '1':  # Sensor is ON (LOW state)
            print(f"Sensor {i} is ON")
        else:  # Sensor is OFF (HIGH state)
            print(f"Sensor {i} is OFF")
    print("-" * 20)  # Separator for readability

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()  # Read a line from the serial port
            if line.startswith('<') and line.endswith('>'):  # Check for start and end markers
                data = line[1:-1]  # Remove markers
                sensor_states = data.split(',')  # Split into individual sensor states
                display_sensor_status(sensor_states)  # Display which sensor is ON
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    ser.close()  # Close the serial port