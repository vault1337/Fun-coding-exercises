"""Mocking SpongeBob meme text generator.
Video: https://youtu.be/akp8JZXikLY
"""

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Don\'t forget the text to convert!")
    else:
        spongebob_text = ""
        capitalize = False
        for word in sys.argv[1:]:
            for c in word:
                if c.isalpha() == True:
                    if capitalize == True:
                        c = c.upper()
                    else:
                        c = c.lower()
                    capitalize = not capitalize
                spongebob_text += c
            spongebob_text += " "    
        print(spongebob_text)
