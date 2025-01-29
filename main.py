import logic

def main():
    input_filename = input("Input file: ")
    output_filename = input("Output file: ")
    key = input("Key: ")

    logic.encrypt_decrypt_file(input_filename, output_filename, key)

if __name__ == "__main__":
    main()