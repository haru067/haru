#!/usr/bin/env bash
set -euo pipefail

tmpfile=$(mktemp)
python format.py ./src/haru.yml $tmpfile
mustache $tmpfile ./template/haru.html > ./dist/web/haru.html
mustache $tmpfile ./template/haru.itermcolors > ./dist/iterm/haru.itermcolors
mustache $tmpfile ./template/haru067-color-themes.json > ./dist/vscode/themes/haru067-color-themes.json
rm $tmpfile
