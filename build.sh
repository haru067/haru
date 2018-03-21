#!/usr/bin/env bash
set -euo pipefail

python format.py ./src/haru.yml tmp
mustache tmp ./template/haru.html.mustache > ./build/haru.html