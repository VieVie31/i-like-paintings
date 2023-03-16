from .predictor import load_predictor, VALID_MODELS, VALID_DATASETS

__version_info__ = (0, 0, 1)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "Nicolas BIZZOZZERO (NicolasBizzozzero)\nIhab BENDIDI (IhabBendidi)\nOlivier RISSER-MAROIX (VieVie31)"

__all__ = ["load_predictor", "VALID_MODELS", "VALID_DATASETS"]

