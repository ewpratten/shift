#! /bin/bash

echo "Encoding:"
python3 -m cProfile shift2/__main__.py ./example.txt ewpratten | grep seconds
echo "Decoding:"
python3 -m cProfile shift2/__main__.py -d ./example.txt.shift ewpratten | grep seconds