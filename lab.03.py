def get_calibration_number(text):
    digits = [c for c in text if c.isdigit()]
    return int(digits[0] + digits[-1]) if digits else 0

with open('input_3.txt') as file:
    total = sum(get_calibration_number(line.strip()) for line in file)

print(f"Загальна сума калібрувальних значень: {total}")
