#Caesar cipher hacker

# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import paperclip

# The string to be decrypted

message = '7uv6Jv6Jz!J6rp5r7Jzr66ntr'

# Every possible symbol that can be decrypted

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key

for key in range(len(SYMBOLS)):
    translated = ''

    # Decrypt each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without decrypting
            translated = translated + symbol

    # Display the key being tested, along with the decrypted text
    print('Key #%s: %s' % (key, translated))
    paperclip.copy(translated)