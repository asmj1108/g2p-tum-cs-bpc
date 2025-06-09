Pair n-gram baseline
====================

This directory contains a pair n-gram baseline, similar to that used by
Lee et al. (in press).

To run:

1.  Create and enable the Conda environment using
    ```bash
    conda env create -f environment.yml
    conda activate g2p-fst
    ```
2.  Run [`sweep`](sweep).

Results are stored in the [`checkpoints`](checkpoints) directory.
