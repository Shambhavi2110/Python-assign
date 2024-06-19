def starts_with_prefix(string, prefix):
    return string.startswith(prefix)

def ends_with_suffix(string, suffix):
    return string.endswith(suffix)

def main():
    input_string = input("Enter a string: ")
    prefix = input("Enter a prefix to check (press Enter to skip): ")
    suffix = input("Enter a suffix to check (press Enter to skip): ")

    if prefix:
        if starts_with_prefix(input_string, prefix):
            print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
        else:
            print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")

    if suffix:
        if ends_with_suffix(input_string, suffix):
            print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
        else:
            print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")

    if not prefix and not suffix:
        print("No prefix or suffix provided to check.")

if __name__ == "__main__":
    main()