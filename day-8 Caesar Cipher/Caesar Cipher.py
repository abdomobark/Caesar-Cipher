# List of alphabets for Caesar cipher
alphabets  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']

# Function to return the index of a character in a list
def index(value, lst):
    x = 0
    while x < len(lst):
        if value == lst[x]:
            return x
        x += 1
    return None


# Caesar cipher function for encryption and decryption
def cesar(value, encrypt_code, e_or_d):
    final_message = ""
    for i in value:
        if i in alphabets:
            x = index(i, alphabets)
            if e_or_d == "e":   # Encrypt
                x = (x + encrypt_code) % len(alphabets)
            elif e_or_d == "d": # Decrypt
                x = (x - encrypt_code) % len(alphabets)
            else:
                print("❌ Invalid choice (use 'e' to encrypt or 'd' to decrypt)")

            final_message += alphabets[x]
        else:
            final_message += i  # Keep spaces/punctuation as they are
    print(final_message)


# Main program loop
should_continue = True
while should_continue:
    user_type = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    user_input = input("Enter the message: ").lower()
    shift_input = int(input("Enter the shift key: "))
    cesar(user_input, shift_input, user_type)

    do_you_want = input("Do you want to continue? (yes/no): ").lower()
    if do_you_want == "no":
        should_continue = False
