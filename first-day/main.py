from text_processor import TextProcessor


def main():
    with open('data.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]
    procesador = TextProcessor(data)
    procesador.process_texts()
    results = procesador.get_results()
    print("Part 1:", results)
    procesador.process_texts_with_words()
    print("Part 2:", procesador.get_results())


def test_data():
    data = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    procesador = TextProcessor(data)
    procesador.process_texts()
    results = procesador.get_results()
    print("Test Part 1:", results)
    procesador.process_texts_with_words()
    print("Test Part 2:", procesador.get_results())
def test_data_second():
    data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    procesador = TextProcessor(data)
    procesador.process_texts()
    results = procesador.get_results()
    print("Test 2 Part 1:", results)
    procesador.process_texts_with_words()
    print("Test 2 Part 2:", procesador.get_results())

if __name__ == "__main__":
    main()
    # test_data()
    # test_data_second()

