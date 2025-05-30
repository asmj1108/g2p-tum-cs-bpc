# Baseline 2020 / 2021

This model is an ensembled neural transition system based on the imitation learning paradigm introduced by Makarov &
Clematide (2020) and made available during SIGMORPHON shared task in year 2022.

## How to use

1. The model requires Python 3.7. If your system does not use Python 3.7 by
   default (i.e., see `python --version` for your default Python), create and
   activate either:

    - a [3.7 virtualenv](https://virtualenv.pypa.io/en/latest/):

    ```bash
    virtualenv --python=python3.7 g2p-transducer
    source g2p-transducer/bin/activate
    ```

    - or
      a [3.7 Conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html#installing-a-different-version-of-python):

    ```bash
    conda create --name=g2p-transducer python=3.7
    conda activate g2p-transducer
    ```

2. Install the requirements and the library itself:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install .
    ```

3. Train and evaluate the ensemble models for all languages:

    ```bash
   ./sweep
    ```

## License

The baseline model is originally made available under the [Apache 2.0](LICENSE.txt) license.

## References

Makarov, P., and Clematide, S. 2020. [CLUZH at SIGMORPHON 2020 shared task on
multilingual grapheme-to-phoneme
conversion](https://www.aclweb.org/anthology/2020.sigmorphon-1.19/). In
*Proceedings of the 17th SIGMORPHON Workshopon Computational Research in
Phonetics, Phonology, and Morphology*, pages 171-176. [Repository](https://github.com/sigmorphon/2022G2PST)
