#!/bin/bash

# Set the directory for output and check if it exists. Create if no
dir="$PWD"
dir="${PWD}/pylint_result"
if [ ! -d "$dir" ]; then
    mkdir $dir
fi

lab2="lab2"
validation="validation"


# Check to see if lab 2's report exist. Create if no. Then perform pylint
lab2_py="$lab2.py"
lab2_report="$dir/${lab2}_pylint.txt"
echo "Adding pylint result for lab2.py - $lab2_report"
if [ ! -f "$lab2_report" ]; then
    touch $lab2_report
fi
pylint $lab2_py > $lab2_report


# Pylint validation.py and output to file
validation_py="$validation.py"
validation_result="$dir/${validation}_pylint.txt"
echo "Adding pylint result for validation.py - $validation_result"
if [ ! -f "$validation_result" ]; then
    touch $validation_result
fi
pylint $validation_py > $validation_result

# Pylint both lab2.py and validation.py and output to file
both="$dir/both_pylint.txt"
echo "Adding pylint result for botyh $lab2_py and $validation_py - $both"
if [ ! -f "$both" ]; then
    touch $both
fi
pylint $lab2_py $validation_py > $both

# Done doing stuff. Exit
echo "Done"