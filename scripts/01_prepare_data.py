def prepare_data(counts_path, clinical_path):
    """Load raw counts and clinical data, return cleaned tables."""
    pass


if __name__ == "__main__":
    prepare_data(
        "data/raw/TCGA-BRCA.star_counts.tsv.gz",
        "data/raw/BRCA_clinicalMatrix.tsv",
    )
