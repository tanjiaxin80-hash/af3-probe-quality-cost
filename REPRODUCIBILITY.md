# Reproducibility scope

This release contains 12 accepted CSV tables and two standard-library Python
scripts. It checks headline arithmetic from archived scores and timings; it
does not independently recompute structural scores or regenerate structures.

`verify_headline_results.py` computes the aggregate probe break-even allowance,
timing cost ratios, held-out coverage and loss counts, and the reported
TM-score summary from the supplied records. The one-sided Clopper–Pearson
upper limit assumes independent binomial outcomes. The Student t interval
uses the stated 74 degrees of freedom for the 75 evaluable paired records.
These are checks of the reported calculations, not additional experiments.

The ten-target timing audit and the held-out quality assessment are different
cohorts. Keep their denominators separate. All 78 held-out groups remain in the
method summary; only 75 are P3-evaluable, so the other three do not acquire
invented paired quality values. Main Figure 4 is a post hoc allocation analysis.

The original CSV filenames are retained. Main figure order changed during
manuscript editing; the README table guide maps the filenames to the final
figure numbers. `main/figure3.csv` supplies the cost panel of final Figure 2,
and `main/figure2.csv` supplies final Figure 4.

The separate journal review archive contains extended attempt records,
numerical reanalysis scripts, coordinates, mappings, and available source and
scoring files. Those materials are not included in this bounded public release.
A full AF3 rerun additionally requires processed MSA and template inputs,
authorized model weights, and a compatible runtime. The exact upstream AF3
revision and per-attempt runtime environment remain unverified.

Publication of these numerical records grants no permission to redistribute
AF3 weights or third-party source materials. No license file is assigned to
this release; public accessibility alone does not grant a general reuse license.
