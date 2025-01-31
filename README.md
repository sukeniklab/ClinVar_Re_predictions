A companion repo for 
# Single-point mutations in disordered proteins: Linking sequence, ensemble, and function
## by Eduardo Flores, Nirbhik Acharya, Carlos A. Castañeda, and Shahar Sukenik.

This repo contains all the code required to plot figures in the paper, as well as some extra analysis. 
The full dataset is available at https://doi.org/10.5281/zenodo.14074113
The main jupyter notebook with panels for Fig 2 is [here](./analysis/plotClinvarAll.ipynb)

Contents:

* ./data - all input files:
    * ./data/all_id_mappings.tsv - uniprot and gene number for all human proteins
    *    ./data/allClinvarMissense.csv - analysis of all clinvar SNP missense variants
    *    ./data/clinvar_20240917.vcf - clinvar export (Sep 17 2024)
    *    ./uniprotkb_proteome_UP000005640_2024_08_16.tsv - uniprot human proteome export

* ./analysis - all analysis files:
    * ./analysis/plotClinvarAll.ipynb - panels from Fig. 2B,C of the paper
    *    ./analysis/GO_analysis - all gene onthology files
    *        ./analysis/GO_analysis/all.txt - all uniprot IDs for proteins with missense variants for GO enrichment background
    *        ./analysis/GO_analysis/expand.txt - all uniprot IDs for proteins with expanding missense variants
    *        ./analysis/GO_analysis/compact.txt - all uniprot IDs for proteins with compacting missense variants
    *        ./analysis/GO_analysis/plotClinvar_GO.py - plotting for Fig. 2D
    *        ./analysis/GO_analysis/gProfiler_hsapiens_11-7-2024_compact.csv - g:Profiler output from compact.txt
    *        ./analysis/GO_analysis/gProfiler_hsapiens_11-7-2024_expand.csv - g:Profiler output from expand.txt
