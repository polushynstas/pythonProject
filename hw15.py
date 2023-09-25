def analyze_input(input_str):
    exit_phrases = ["вихід", "exit", "quit", "e", "q"]
    if input_str.lower() in exit_phrases:
        quit()

    input_str = input_str.strip()
    if not input_str:
        return "Ви ввели порожній рядок."

    if input_str.isdigit():
        return f'Ви ввели позитивне ціле число {input_str}.'

    if input_str[0] == '-' and input_str[1:].isdigit():
        return f"Ви ввели від'ємне ціле число:{input_str}"
    if '.' in input_str:
        parts = input_str.split('.')
        if len(parts) == 2 and (parts[0].isdigit() or (parts[0].startswith('-') and parts[0][1:].isdigit())) and parts[
            1].isdigit():
            if input_str.startswith('-'):
                return f"Ви ввели від'ємне дробове число: {input_str}"
            else:
                return f"Ви ввели дробове число: {input_str}"


    return 'Ви ввели не коректне число.'

while True:
    input_str = input('Введіть число: ')
    result = analyze_input(input_str)
    print(result)
