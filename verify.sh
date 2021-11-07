#!/bin/bash

python3 cmdGenerate.py
echo "CMD files generated"

python3 logVerify.py
echo "Verification complete"
echo "Ending procedure"