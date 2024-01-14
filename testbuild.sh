#!/bin/bash

cd apps/

echo $'+++++ TEST OF CSV +++++\n'

python3 testcsv.py

echo $'\n\n+++++ TEST OF ODE +++++\n'

python3 testode.py
