import argparse

parser = argparse.ArgumentParser(description="This program decodes Caesar \
ciphers.")

parser.add_argument("--file")
parser.add_argument("--key")

args = parser.parse_args()


filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened

s = encoded_text
n = int(args.key)


def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


decode_Caesar_cipher(s, n)


parser = argparse.ArgumentParser(description="This program calculates \
consisting of the ingredients you provide.")
