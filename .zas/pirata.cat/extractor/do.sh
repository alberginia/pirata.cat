#!/bin/bash

find . \( ! -regex '.*/\..*' \) -type f -name "*.html" -exec ./.zas/pirata.cat/extractor/extractor {} \;

