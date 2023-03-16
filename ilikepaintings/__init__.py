from .predictor import load_predictor

__version_info__ = (0, 0, 1)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "Olivier RISSER-MAROIX (VieVie31)\nNicolas BIZZOZZERO (NicolasBizzozzero)"

__all__ = ["load_predictor", "VALID_MODELS", "VALID_DATASETS"]

