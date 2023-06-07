# Speckle targeting motif
This repository describes the algorithm used to identify speckle targeting motifs within proteins *de novo*. It accompanies the manuscript, Alexander et al., which is under preparation (as of 05/31/2023). It is based on observations from the p53 and HIF2A proteins, the two known transcrption factors that drive DNA-speckle association of their target genes. 

As additional insights are made about other factors that facilitate speckle targeting, I envision that this algorithm will be updated and refined. In its current version, the defined speckle targeting motif is highly enriched among DNA-binding transcription factors and chromatin-binding proteins. However, the extent that presence of a speckle targeting motif predicts factors' speckle targeting ability has yet to be empirically determined. The presence of a putative speckle targeting motif is meant to serve as a guide for which factors are candidates for further testing for speckle targeting abilities. 

# Requirements
Python 2.7 - The Python scripts herein are relatively simple. I expect they could easily be converted to [Python3](https://python2to3.com/), but have not tried this.

# Getting speckle targeting motifs
1. I used [Motif Search](https://www.genome.jp/tools/motif/MOTIF2.html) to download all the motifs in the human proteome that followed this rule: ```x(30)-[TSED]-P-x(30)```, which is a 62 amino acid sequence centered around TP, SP, EP, or DP with any 30 amino acids on both sides. These were stored in the file: "x(30)-[TSED]-P-x(30)_hsa.txt"
2. Speckle targeting motif rules were applied:
  * No more than 4 Prolines in a row
  * At least 3 spaced prolines of 7 possibilities spaced every 5 amino acids from central [TSED]P (Python indexes 11, 16, 21, 26, 36, 41, 46)
  * At least 5 of [EDST] to the right of the central [TSED]P
  * At least 7 [AMVFLIG] to the left of the central [TSED]P
  * Fewer than 16 total [RHK]
  ```python applyRulesAndFormat_fromMotifFinder_2.0.py x\(30\)-\[TSED\]-P-x\(30\)_hsa.txt > motifsWithRules_\[TSED\]P_2.0.txt```
  
  Here each motif is stored in file ```motifsWithRules_[TSED]P_2.0.txt```, and proteins with multiple motifs will be assigned "\_n"
3. A protein list of proteins that contain speckle targeting motifs was extracted:
```python python getGeneFromFasta.py motifsWithRules_\[TSED\]P_2.0.txt > genesWithRules_\[TSED\]P_2.0.txt```




