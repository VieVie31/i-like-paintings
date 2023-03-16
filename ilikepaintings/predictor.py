import pkg_resources
import torch
import io

VALID_MODELS = ["ViT-B/32", "ViT-B/14"]
VALID_DATASETS = ["VAPS999", "sidhu"]

def load_predictor(clip_model_name, dataset_name="VAPS999"):
    # Check if clip_model_name is valid
    if clip_model_name not in VALID_MODELS:
        raise ValueError(f"Invalid CLIP model name: {clip_model_name}. "
                         f"Valid models are: {', '.join(VALID_MODELS)}")
    
    # Check if dataset_name is valid
    if dataset_name not in VALID_DATASETS:
        raise ValueError(f"Invalid dataset name: {dataset_name}. "
                         f"Valid datasets are: {', '.join(VALID_DATASETS)}")
    
    # Replace any "/" in the clip_model_name with "-"
    clip_model_name = clip_model_name.replace("/", "-")
    
    # Construct the resource path to the weight file
    resource_path = f"ilikepaintings/weights/{dataset_name}/{clip_model_name}_linear.pth"
    
    # Load the contents of the resource file
    weight_bytes = pkg_resources.resource_string(__name__, resource_path)
    
    # Load the weights using PyTorch
    state_dict = torch.load(io.BytesIO(weight_bytes))
    in_features = state_dict['weight'].shape[1]
    out_features = state_dict['weight'].shape[0]
    linear_layer = torch.nn.Linear(in_features=in_features, out_features=out_features)
    linear_layer.load_state_dict(state_dict)
    
    return linear_layer




