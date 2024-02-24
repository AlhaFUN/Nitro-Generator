import string
import random

def generate_random_string(length=18):
    # Generate a random alphanumeric string of given length
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    while True:
        code = generate_random_string()
        print(f"New gift code generated: {code}")

if __name__ == "__main__":
    main()
