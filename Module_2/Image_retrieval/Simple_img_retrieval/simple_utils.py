import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sys import path
import streamlit as st

path.append('/Users/microwave/AIO_2024/Module_2/Image_retrieval/utils')
from query import read_image_from_path, folder_to_images

ROOT = '/Users/microwave/AIO_2024/Module_2/Image_retrieval/data'
CLASS_NAME = sorted(list(os.listdir(f'{ROOT}/train')))

#Image query with L1 distance
def absolute_difference(query,data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    return np.sum(np.abs(data - query),axis = axis_batch_size)


def get_l1_score(root_image_path,query_path,size):
    query = read_image_from_path(query_path,size)
    ls_path_score = []
    for folder in os.listdir(root_image_path):
        path = root_image_path + folder
        images_np,images_path = folder_to_images(path,size)
        rates = absolute_difference(query,images_np)
        ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score

#Image query with L2 distance
def mean_square_difference(query,data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    return np.mean((data - query) ** 2,axis = axis_batch_size)

def get_l2_score(root_img_path,query_path,size):
    query = read_image_from_path(query_path,size)
    ls_path_score = []
    for folder in CLASS_NAME:
        path = root_img_path + folder
        images_np, images_path = folder_to_images(path,size)
        rates = mean_square_difference(query,images_np)
        ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score


#Image query with Cosine similarity
def cosine_similarity(query,data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    query_norm = np.sqrt(np.sum(query ** 2))
    data_norm = np.sqrt(np.sum(data ** 2,axis = axis_batch_size))
    return np.sum(data * query, axis = axis_batch_size) / (query_norm * data_norm + np.finfo(float).eps)

def get_cosine_similarity_score(root_img_path,query_path,size):
    query = read_image_from_path(query_path,size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path,size)
            rates = cosine_similarity(query,images_np)
            ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score

#Image query with correlation coefficient score
def correlation_coefficient(query,data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    query_mean = query - np.mean(query)
    data_mean = data - np.mean(data,axis=axis_batch_size,keepdims=True)
    query_norm = np.sqrt(np.sum(query_mean ** 2))
    data_norm = np.sqrt(np.sum(data_mean ** 2,axis=axis_batch_size))
    return np.sum(data_mean * query_mean,axis=axis_batch_size) / (query_norm * data_norm + np.finfo(float).eps)

def get_correlation_coefficient_score(root_img_path,query_path,size):
    query = read_image_from_path(query_path,size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path,size)
            rates = correlation_coefficient(query,images_np)
            ls_path_score.extend(list(zip(images_path,rates)))
    return query,ls_path_score



 