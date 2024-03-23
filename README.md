# makeGenePairs

## 1. Construct the gene pairs matrix

In recent years, several studies (including [Li B, 2017](https://pubmed.ncbi.nlm.nih.gov/28687838/) , [Kog W, 2022](https://pubmed.ncbi.nlm.nih.gov/35945345/) and our work [Wu P, 2024](https://pubmed.ncbi.nlm.nih.gov/38460724/)) have reported the predictive value of gene pair signatures based on bulk gene expression profiles for tumor diagnosis and prognosis. Specifically, a gene pair is a pairing between two genes in a given sample (for example: geneA|gene B). When the expression of gene A is greater than that of gene B in a given sample, this gene pair is assigned a value of 1 (or 0); conversely, when the expression of gene A is less than or equal to that of gene B, this gene pair is assigned a value of 0 (or 1). Compared to traditional gene expression which requires proper data normalization and pre-processing, this gene expression rank-based approach avoids the above processes, thus it could be a potentially clinically usable biomarker. 

Therefore, first purpose of our Python program is a script for constructing the gene pairs. By using the ``makePairs.py`` script, the user can quickly get the 0-1 matrix of the gene pairs by simply entering an expression profile matrix.  

The following is an example of usage.

```shell
usage: python makePairs.py [-h] --expr EXPR [--output OUTPUT]

To make a gene-gene pair matrix

optional arguments:
  -h, --help            show this help message and exit
  --expr EXPR, -e EXPR  Input an expression file name, with genes in row and samples in column.
  --output OUTPUT, -o OUTPUT
                        Set a output file name. Default: "pair.txt"
```

---

## 2. Filter the constant gene pairs

In addition, if certain gene pairs were consistently 0 or consistently 1 in the majority of tumor samples, such gene pairs were also considered to be meaningless for subsequent analysis. Therefore, we also provide a Python script ``pairsFilter.py`` for filtering constant gene pairs. Users can accomplish this by setting the filtering threshold (i.e., the proportion of samples with gene pairs having values of 0 or 1 over all samples), with a default threshold of 0.8.

The following is an example of usage.

```shell
usage: python pairsFilter.py [-h] --input INPUT [--threshold THRESHOLD] [--output OUTPUT]

To filter the constant values of gene-gene pairs

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input a gene-gene pair matrix file name.
  --threshold THRESHOLD, -t THRESHOLD
                        Set a filter threshold [0-1]. When this threshold is exceeded, these gene-gene pairs are considered meaningless for subsequent analysis and need to be filtered.
                        Default: 0.8
  --output OUTPUT, -o OUTPUT
                        Set a output file name. Default: "pair_filtered.txt"
```



