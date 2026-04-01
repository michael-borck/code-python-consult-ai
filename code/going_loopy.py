"""
Loops - Automating Repetitive Tasks

Extracted from the companion book.
"""

def process_temperature_data(celsius_readings):
    """
    Process a list of temperature readings in Celsius.

    Args:
        celsius_readings: List of temperature values in Celsius

    Returns:
        Dictionary containing:
        - 'valid_readings_c': List of valid Celsius readings
        - 'readings_f': List of Fahrenheit conversions
        - 'avg_c': Average temperature in Celsius
        - 'avg_f': Average temperature in Fahrenheit
        - 'min_c': Minimum valid temperature in Celsius
        - 'max_c': Maximum valid temperature in Celsius
        - 'min_f': Minimum temperature in Fahrenheit
        - 'max_f': Maximum temperature in Fahrenheit
        - 'invalid_count': Number of invalid readings
    """
    # Constants for validation
    ABSOLUTE_ZERO_C = -273.15
    MAX_VALID_TEMP_C = 100

    # Initialize result containers
    valid_readings_c = []
    readings_f = []
    invalid_count = 0

    # Process each reading
    for temp_c in celsius_readings:
        # Validate the reading
        try:
            temp_c = float(temp_c)  # Convert to float in case it's a string

            # Check if temperature is physically possible and reasonable
            if ABSOLUTE_ZERO_C <= temp_c <= MAX_VALID_TEMP_C:
                # Valid reading - store Celsius value
                valid_readings_c.append(temp_c)

                # Convert to Fahrenheit: F = (C × 9/5) + 32
                temp_f = (temp_c * 9/5) + 32
                readings_f.append(temp_f)
            else:
                # Invalid temperature
                invalid_count += 1

        except (ValueError, TypeError):
            # Handle non-numeric inputs
            invalid_count += 1
            continue

    # Calculate statistics if we have valid readings
    if valid_readings_c:
        avg_c = sum(valid_readings_c) / len(valid_readings_c)
        avg_f = sum(readings_f) / len(readings_f)
        min_c = min(valid_readings_c)
        max_c = max(valid_readings_c)
        min_f = min(readings_f)
        max_f = max(readings_f)
    else:
        # No valid readings
        avg_c = avg_f = min_c = max_c = min_f = max_f = None

    # Return all statistics and processed data
    return {
        'valid_readings_c': valid_readings_c,
        'readings_f': readings_f,
        'avg_c': avg_c,
        'avg_f': avg_f,
        'min_c': min_c,
        'max_c': max_c,
        'min_f': min_f,
        'max_f': max_f,
        'invalid_count': invalid_count
    }

# Example usage:
# temperatures = [20.5, -300, 15.0, 25.7, "error", 150, 10.3]
# result = process_temperature_data(temperatures)
# print(f"Average temperature: {result['avg_c']:.1f}°C ({result['avg_f']:.1f}°F)")
# print(f"Range: {result['min_c']:.1f}°C to {result['max_c']:.1f}°C")
# print(f"Invalid readings: {result['invalid_count']}")
