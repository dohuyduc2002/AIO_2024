import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def read_image_from_path(path, size):
    im = Image.open(path).convert('RGB').resize(size)
    return np.array(im)

def folder_to_images(folder, size):
    list_dir = [folder + '/' + name for name in os.listdir(folder)]
    images_np = np.zeros(shape=(len(list_dir), *size, 3))
    images_path = []
    for i, path in enumerate(list_dir):
        images_np[i] = read_image_from_path(path, size)
        images_path.append(path)
    images_path = np.array(images_path)
    return images_np, images_path

def plot_results(query_path, ls_path_score, reverse):
    fig = plt.figure(figsize=(15, 9))
    fig.add_subplot(2, 3, 1)
    plt.imshow(read_image_from_path(query_path, size=(448,448)))
    
    # Extract the class name for the query image
    query_class = query_path.split('/')[-2]
    plt.title(f"Query Image: {query_class}", fontsize=16)
    plt.axis("off")
    
    for i, (path, score) in enumerate(sorted(ls_path_score, key=lambda x: x[1], reverse=reverse)[:5], 2):
        fig.add_subplot(2, 3, i)
        plt.imshow(read_image_from_path(path, size=(448,448)))
        
        # Extract the class name for the result image
        result_class = path.split('/')[-2]
        plt.title(f"Top {i-1}: {result_class}", fontsize=16)
        plt.axis("off")
    
    plt.tight_layout()
    plt.show()