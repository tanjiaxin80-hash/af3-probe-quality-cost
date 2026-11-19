# Numerical data and analysis code

Companion to *Quality and computational cost trade-offs in probe-guided inference for single-chain AlphaFold 3* by Tinglong Tang, Jiaxin Tan, Xinqiong Liu and Lu Wang.

Run the following command after extracting the archive, using Python 3 and its standard library.

    python verify_headline_results.py

The input tables are frozen numerical records carried forward from the study archive. The script reports the break-even threshold, audit cost ratios, held-out coverage, loss count and TM-score summaries. The Clopper–Pearson limit assumes independent binomial outcomes. The timing audit and held-out assessment concern different cohorts. A blank table value is missing or inapplicable as defined by the manuscript.

## Table guide

| Display or endpoint | Files under figure_data |
| --- | --- |
| Main Figure 1, profile comparison | main/figure1.csv |
| Main Figure 2, cost waterfall panel | main/figure3.csv |
| Main Figure 3, break-even analysis | main/figure4_actual.csv, main/figure4_curves.csv, main/figure4_replay.csv |
| Main Figure 4, post hoc allocations | main/figure2.csv |
| Supplementary Figures S1–S3 | supplement/ |
| Coverage and losses across all study methods | all12_frozen_method_context.csv |

The numerical archive supports headline arithmetic and the numerical figure panels. It relies on the archived structure scores and timings. The separate review archive contains the structure overlay sources for Figure 2, detailed attempt records and extended reanalysis scripts. Running AF3 requires additional inputs and an appropriate AF3 runtime. This numerical companion is prepared for public access. No reuse license is assigned in this release. AF3 source, model weights and the separate structural review archive are not distributed here.

## Reproduction and integrity

Python 3 and its standard library are sufficient for the commands below. Run
them from this repository's root directory.

```sh
python verify_checksums.py
python verify_headline_results.py
```

`SHA256SUMS` covers the public files, and `expected_headline_results.json`
records the checked output. `DATA_DICTIONARY.md` lists every CSV and its columns.
`REPRODUCIBILITY.md` explains the boundary between numerical checks and a full
AF3 rerun. Data are copied without editing the accepted CSV values.

## Study interpretation

The measured probe-guided strategy was more costly than direct fixed-P3
inference in the timing audit. The analysis quantifies its break-even probe
budget and the quality-loss frequency in a separate held-out cohort. It does
not establish a net efficiency gain or general structural equivalence.

The data are from a single-chain AlphaFold 3 study. The manuscript was prepared
for the Journal of Computational Science; this repository does not imply
publication or acceptance. Funding: grant 2025YGKF1-08.
