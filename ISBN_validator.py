def calculate_check_digit_10(digits: list[int]) -> str:
    digits_sum = sum(d * (10 - i) for i, d in enumerate(digits))
    remainder = digits_sum % 11
    result = (11 - remainder) % 11
    return 'X' if result == 10 else str(result)


def calculate_check_digit_13(digits: list[int]) -> str:
    digits_sum = sum(d * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    remainder = digits_sum % 10
    return str((10 - remainder) % 10)

def validate_isbn(isbn_raw: str, length: int | None = None) -> bool:
    cleaned = isbn_raw.replace("-", "").replace(" ", "").strip().upper()
    
    if length is None:
        if len(cleaned) in (10, 13):
            length = len(cleaned)
        else:
            return False

    if len(cleaned) != length or length not in (10, 13):
        return False

    body, given_check = cleaned[:-1], cleaned[-1]

    if not body.isdigit():
        return False

    body_digits = [int(ch) for ch in body]

    if length == 10:
        expected_check = calculate_check_digit_10(body_digits)
    else:
        expected_check = calculate_check_digit_13(body_digits)

    return given_check == expected_check

def main():
    user_input = input("Enter ISBN and optional length (e.g. '0-306-40615-2' or '0-306-40615-2, 10'): ").strip()
    if not user_input:
        print("No input provided.")
        return

    if "," in user_input:
        raw_isbn, raw_len = user_input.split(",", 1)
        try:
            target_len = int(raw_len.strip())
        except ValueError:
            print("Invalid length specified.")
            return
        is_valid = validate_isbn(raw_isbn, target_len)
    else:
        is_valid = validate_isbn(user_input)

    print("Valid ISBN Code." if is_valid else "Invalid ISBN Code.")


if __name__ == "__main__":
    main()