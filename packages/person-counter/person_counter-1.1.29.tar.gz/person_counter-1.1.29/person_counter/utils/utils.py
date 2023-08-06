import gdown
import os

def download_to_weights_folder(weights_dir: str, url:str, path: str):
    if not os.path.exists(weights_dir):
        os.mkdir(path)
        gdown.download(url, path, quiet=False) 
        
