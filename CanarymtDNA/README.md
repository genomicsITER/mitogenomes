<!-- ------------------ SECTION ------------------ -->

# About #

This repository contains materials used for the manuscript entitled: "Digging into the admixture strata of current-day Canary Islanders based on mitogenomes".

<hr>
<!-- ------------------ SECTION ------------------ -->

# Digging into the admixture strata of current-day Canary Islanders based on mitogenomes (2022) #

The European conquest of the Canary Islands began at the beginning of the fifteenth century and culminated in 1496 with the surrender of the aborigines. The collapse of the aboriginal population during the conquest and the arrival of continental settlers caused a drastic change in the demographic composition of the archipelago. To delve into this historical process, we analyze the complete mitochondrial genome of the contemporary Canarian population.

The mitogenome of 896 unrelated canaries was sequenced by means of next-generation sequencing (NGS), obtaining the largest and most comprehensive maternal genetic characterization of the Canarian population to date.

<p align="center">
  <img src="https://github.com/genomicsITER/mitogenomes/blob/main/CanarymtDNA/images/CanarymtDNA_workflow-overview.png" title="Overview of the processing workflow" style="width: 75%;"/>
</p>
<p align="center">
<b>Figure 1.</b> Overview of the bioinformatics workflow.
  
<p align="center">
  <img src="https://github.com/genomicsITER/..." title="Overview of the population analyses" style="width: 75%;"/>
</p>
<p align="center">
<b>Figure 2.</b> Overview of the population analyses.
  
</p>

<hr>
<!-- ------------------ SECTION ------------------ -->

# Contents #

The `scripts` folder contains code to generate data used in the paper. As a general requirement, in order to run the following scripts, `python3` must be installed on the system. Here is a description of each script:

| File | Description |
| --- | --- |
| bootstrap_rho.py | Generate bootstrapped mtDNA alignments from a sequence aligned in `PHYLIP` format (.phy extension). |

