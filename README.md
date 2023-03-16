# I Like Paintings

I Like Paintings is a Python package that can predict the painting appreciation (if people like or not the painting) from the image using a linear regressor trained on top of a frozen CLIP features extractor model on two paintings appreciation datasets. The package contains pre-trained weights for nine models on two datasets (VAPS-999 and Sidhu's one).
All linear predictors in this package assume that their input embeddings are L2 normalized.



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



## License

The license associated with this package is the Creative Commons Attribution 4.0 International License [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/), WITH the following additional conditions:

Before using any part or whole of this package, you must star this repository.

If you use any file associated with this package, including the provided weights, you must cite the package using the following BibTeX citation:
```bibtex
@software{ilikepaintings,
  author = {BIZZOZZERO, Nicolas and RISSER-MAROIX, Olivier},
  title = {I Like Paintings},
  url = {https://github.com/VieVie31/i-like-paintings},
  version = {0.0.1},
  date = {2023-03-16},
}
```

The package authors make no representations or warranties of any kind concerning the code or the information contained herein. They disclaim all liability and responsibility for any errors or omissions in the code, or for any loss, injury, or damage resulting from the use of this package, including but not limited to indirect or consequential damages. 



