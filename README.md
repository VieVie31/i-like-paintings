# I Like Paintings

I Like Paintings is a Python package that can predict the painting appreciation (if people like or not the painting) from the image using a linear regressor trained on top of a frozen CLIP features extractor model on two paintings appreciation datasets. The package contains pre-trained weights for nine models on two datasets (VAPS-999 and Sidhu's one).
All linear predictors in this package assume that their input embeddings are L2 normalized.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VieVie31/i-like-paintings/blob/master/demo.ipynb)
[![PyPI version](https://badge.fury.io/py/ilikepaintings.svg)](https://badge.fury.io/py/ilikepaintings)


## Installation

You can install I Like Paintings via pip:

```bash
pip install ilikepaintings
```


## Usage
To use the package, you need to load the weights of the linear regressor. Here is an example code snippet:

```python
from ilikepaintings import load_predictor, VALID_MODELS, VALID_DATASETS

# Choose a model and dataset
clip_model_name = VALID_MODELS[0]
dataset_name = VALID_DATASETS[0]

# Load the predictor
predictor = load_predictor(clip_model_name, dataset_name)
```

For a fully working example on a real painting, look at `demo.ipynb` or try on [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VieVie31/i-like-paintings/blob/master/demo.ipynb) !



## Benchmark

The following table shows the cross-validation scores (`k=5`) of the linear model with the best hyper-parameters, measured using the Pearson correlation coefficient. 
These scores were obtained for each CLIP model backend and dataset. The final released models were retrained using the same hyper-parameters and fitted on the whole dataset.
All embeddings are L2 normalized. 


| CLIP | VAPS-999 | Sidhu |
| --- | --- | --- |
| RN50 | _0.6785_ | _0.8039_ 🥉 |
| RN50x4 | _0.7063_ | _0.7858_ | 
| RN50x16 | _0.7307_ 🥉 | _0.8150_ 🥈 | 
| RN50x64 | _0.7335_ 🥈 | **0.8199** 🥇 | 
| RN101 | _0.6904_ | _0.7964_ | 
| ViT-B/16 | _0.6925_ | _0.7863_ | 
| ViT-B/32 | _0.6907_ | _0.7823_ | 
| ViT-L/14 | _0.7265_ | _0.7941_ | 
| ViT-L-14@336px | **0.7382** 🥇 | _0.7985_ | 





## License

The license associated with this package is the Creative Commons Attribution 4.0 International License [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/), **WITH** the following additional conditions:

Before using any part or whole of this package, you must star :star: this repository.

If you use any file associated with this package, including the provided weights or results, you must cite the package using the following BibTeX citation:
```bibtex
@software{ilikepaintings,
  author = {BIZZOZZERO, Nicolas and BENDIDI, Ihab and RISSER-MAROIX, Olivier},
  title = {I Like Paintings},
  url = {https://github.com/VieVie31/i-like-paintings},
  version = {0.0.1},
  date = {2023-03-16},
}
```

The package authors make no representations or warranties of any kind concerning the code or the information contained herein. They disclaim all liability and responsibility for any errors or omissions in the code, or for any loss, injury, or damage resulting from the use of this package, including but not limited to indirect or consequential damages. 



