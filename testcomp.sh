#!/bin/bash
clear
./gen.py $1 
./tdatp3.py E data_aux.txt
echo -e "#################\n"
./tdatp3.py A data_aux.txt