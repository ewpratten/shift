import shcrypt
import argparse
import os
import sys

def main():
    # Load args
    parser = argparse.ArgumentParser(description="Keyed text encoding")
    parser.add_argument("file", help="Input file")
    parser.add_argument("key", help="encode/decode key")
    parser.add_argument("-d", "--decode", help="switch to decoding mode", action="store_true", default=False)
    args = parser.parse_args()
    
    # Convert the key to something easier to work with
    shifts = shcrypt.key2shifts(args.key)

    # Load the file, and convert to b64
    if not os.path.exists(args.file):
        print("File not found", file=sys.stderr)
        exit(1)

    with open(args.file, "r") as fp:
        file = fp.read()
        fp.close()

    # Pass file through correct modifier
    if not args.decode:
        output = shcrypt.encode(file, shifts)
    else:
        output = shcrypt.decode(file, shifts)

    # Print out the output for piping
    print(output)

if __name__ == "__main__":
    main()
