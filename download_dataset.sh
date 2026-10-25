#!/usr/bin/env bash
set -euo pipefail

RAW="${RAW:-$(dirname "$0")/data/raw}"
mkdir -p "$RAW"

fetch() {
  local out="$1" url="$2"
  [ -f "$out" ] && return 0
  curl -fsSL -o "$out.part" "$url"
  mv "$out.part" "$out"
}

XENA_GDC=https://gdc-hub.s3.us-east-1.amazonaws.com/download
for f in TCGA-BRCA.star_counts.tsv.gz TCGA-BRCA.clinical.tsv.gz gencode.v36.annotation.gtf.gene.probemap; do
  fetch "$RAW/$f" "$XENA_GDC/$f"
done
fetch "$RAW/BRCA_clinicalMatrix.tsv" \
  "https://tcga-xena-hub.s3.us-east-1.amazonaws.com/download/TCGA.BRCA.sampleMap%2FBRCA_clinicalMatrix"
