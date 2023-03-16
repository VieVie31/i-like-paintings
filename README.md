# I Like Paintings

I Like Paintings is a Python package that can predict the painting appreciation (if people like or not the painting) from the image using a linear regressor trained on top of a frozen CLIP features extractor model on two paintings appreciation datasets. The package contains pre-trained weights for two models: ViT-B/32 and ViT-L/14 on two datasets: VAPS-999 and Sidhu's one.

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


## Citing

If you use this code, please consider citing it using the following BibTeX:

```bibtex
@software{ilikepaintings,
  author = {RISSER-MAROIX, Olivier and BIZZOZZERO, Nicolas},
  title = {I Like Paintings},
  url = {https://github.com/VieVie31/i-like-painings},
  version = {0.0.1},
  date = {2023-03-16},
}
```

Please also consider starring the repository if you find this package useful!

