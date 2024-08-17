import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sys import path
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
import chromadb
from tqdm import tqdm
from io import BytesIO

path.append('/Users/microwave/AIO_2024/Module_2/Image_retrieval/utils')
path.append('/Users/microwave/AIO_2024/Module_2/Image_retrieval/Simple_img_retrieval')
from query import read_image_from_path, folder_to_images
from simple_utils import absolute_difference, mean_square_difference, cosine_similarity, correlation_coefficient

ROOT = '/Users/microwave/AIO_2024/Module_2/Image_retrieval/data'
CLASS_NAME = sorted(list(os.listdir(f'{ROOT}/train')))

embedding_function = OpenCLIPEmbeddingFunction()

def get_single_image_embedding(image):
    embedding = embedding_function._encode_image(np.array(image))
    return embedding


def get_l1_score(root_img_path,query_path,size):
    query = read_image_from_path(query_path,size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path,size)
            embedding_list = []
            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)
            rates = absolute_difference(query_embedding,np.stack(embedding_list))
            ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score

def get_l2_score(root_img_path,query_path,size):
    query = read_image_from_path(query_path,size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path,size)
            embedding_list = []
            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)
            rates = mean_square_difference(query_embedding,np.stack(embedding_list))
            ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score

def get_cosine_similarity_score(root_img_path,query_path,size):
    query = read_image_from_path(query_path,size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path,size)
            embedding_list = []
            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)
            rates = cosine_similarity(query_embedding,np.stack(embedding_list))
            ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score

def get_correlation_coefficient_score(root_img_path,query_path,size):
    query = read_image_from_path(query_path,size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path,size)
            embedding_list = []
            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)
            rates = correlation_coefficient(query_embedding,np.stack(embedding_list))
            ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score
