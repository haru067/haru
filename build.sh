#!/usr/bin/env bash
set -euo pipefail

python format.py ./src/haru.yml tmp
mustache tmp ./template/haru.html > ./dist/haru.html
rm tmp