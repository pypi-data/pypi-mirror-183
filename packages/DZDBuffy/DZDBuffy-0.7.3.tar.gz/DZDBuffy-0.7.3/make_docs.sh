#!/bin/bash

cp README.md docs/index.md
cp logo.png docs/logo.png

# generate openapi.json REST API Doc
buffy-server-build-api-doc -t docs/openapi.json

mkdocs build --site-dir ./public --verbose
cp docs/DOCS_README.md ./public/README.md