Transformer baseline
==================================================

This directory contains a Transformer baseline, similar to that used by Vaswani et al. (in press).

To run:

1.  Create and enable the Conda environment using
    ```bash
    conda env create -f environment.yml
    conda activate g2p-transformer-fairseq
    ```
2.  Run [`preprocess`](preprocess).
3.  Run [`sweep`](sweep).

Results are stored in the [`checkpoints`](checkpoints) directory.
