#!/usr/bin/env bash
set -euo pipefail

tmpfile=$(mktemp)
python format.py ./src/haru.yml $tmpfile
mustache $tmpfile ./template/haru.html > ./dist/haru.html
mustache $tmpfile ./template/haru.itermcolors > ./dist/haru2.itermcolors
rm $tmpfile
