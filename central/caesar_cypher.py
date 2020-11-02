ABC = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890. '


def process_text(text, shift, action):
    encrypted_text = ''
    for char in text:

        if action == 'ENCRYPT':
            new_shift = ABC.index(char) + shift
        elif action == 'DECRYPT':
            new_shift = ABC.index(char) - shift
        else:
            return

        if new_shift > (len(ABC) - 1):
            new_shift = new_shift % len(ABC)

        encrypted_text += ABC[new_shift]

    return encrypted_text
