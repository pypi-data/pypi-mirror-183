#!/bin/bash

if [ -z "$1" ]
  then
    echo "Script to automatically convert code (*.py and *.ipynb) from PyMC3 to 4.0. Use with care."
    echo "Usage: pymc3_to_4.sh <path>"
    exit 1
fi

declare -a replace_strings=(
    "s/from aesara import tensor as at/import pytensor.tensor as pt/g"
    "s/import aesara\.tensor as at/import pytensor.tensor as pt/g"
    "s/at\./pt./g"
    "s/aesara/pytensor/g"
    "s/Aesara/PyTensor/g"
    "s/https\:\/\/github.com\/aesara-devs\/aesara/https\:\/\/github.com\/pymc-devs\/pytensor/g"
    "s/expand_fn_at/expand_fn_pt/g"
)

for replace in "${replace_strings[@]}"; do
    find $1 -name "*.ipynb" -type f -exec sed -i -e "/png/!$replace" {} \;
    find $1 -name "*.py" -type f -exec sed -i -e "/png/!$replace" {} \;
    find $1 -name "*.md" -type f -exec sed -i -e "/png/!$replace" {} \;
done
