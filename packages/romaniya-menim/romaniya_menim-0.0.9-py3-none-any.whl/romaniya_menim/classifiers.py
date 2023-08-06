import pandas as pd
import numpy as np
import sklearn
import os
from importlib import resources
from utils import transform_labels, read_all_datasets, prepare_data
import torch
from torch.utils.data import DataLoader, TensorDataset




def Classifier(datasets_dict, dataset_names, classifier_names):

    for dataset_name in dataset_names:
        for classifier_name in classifier_names:
            print('Classifier Type: ', classifier_name)   
            trainloader, valloader, input_shape, nb_classes = prepare_data(datasets_dict, dataset_name)
            
            if classifier_name == 'fcn':
                from classifiers import fcn
                print('Everything is ok and now FCN is calling')
                return fcn.create_FCN(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'cnn':
                from classifiers import cnn
                print('Everything is ok and now CNN is calling')
                return cnn.create_CNN(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'mlp':
                from classifiers import mlp
                print('Everything is ok and now MLP is calling')
                return mlp.create_MLP(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'resnet':
                from classifiers import resnet
                print('Everything is ok and now RESNET is calling')
                return resnet.create_RESNET(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'inception':
                from classifiers import inception
                print('Everything is ok and now INCEPTION is calling')
                return inception.create_Inception(trainloader, valloader, input_shape, nb_classes)