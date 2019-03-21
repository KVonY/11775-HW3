#!/usr/bin/env python3

import os
import sys
import threading
import cv2
import numpy as np
import yaml
import pickle
import pdb
from keras.applications import ResNet50
from keras.models import Model
from keras.applications.imagenet_utils import preprocess_input
# import torch
# import torch.nn as nn
# from torchvision import transforms
# import torchvision.models as models
from scipy.misc import imresize


def get_cnn_features_from_video(downsampled_video_filename, cnn_feat_video_filename, keyframe_interval):
    "Receives filename of downsampled video and of output path for features. Extracts features in the given keyframe_interval. Saves features in pickled file."
    # TODO
    resnet50 = ResNet50(weights='imagenet')
    model = Model(inputs=resnet50.input, outputs=resnet50.layers[-1].output)
    # modules=list(resnet101.children())
    # resnet101 = nn.Sequential(*modules)
    feature = []
    for frame in get_keyframes(downsampled_video_filename, keyframe_interval):
        frame = imresize(frame, (224, 224))
        frame = np.expand_dims(frame, axis=0)
        frame = preprocess_input(frame)
        output = model.predict(frame)
        # print(np.array(h_x.flatten()).shape)
        feature.append(np.array(output))
    np.save(cnn_feat_video_filename, np.array(feature))


def get_keyframes(downsampled_video_filename, keyframe_interval):
    "Generator function which returns the next keyframe."

    # Create video capture object
    video_cap = cv2.VideoCapture(downsampled_video_filename)
    frame = 0
    while True:
        frame += 1
        ret, img = video_cap.read()
        if ret is False:
            break
        if frame % keyframe_interval == 0:
            yield img
    video_cap.release()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {0} video_list config_file".format(sys.argv[0]))
        print("video_list -- file containing video names")
        print("config_file -- yaml filepath containing all parameters")
        exit(1)

    all_video_names = sys.argv[1]
    config_file = sys.argv[2]
    my_params = yaml.load(open(config_file))

    # Get parameters from config file
    keyframe_interval = my_params.get('keyframe_interval')
    hessian_threshold = my_params.get('hessian_threshold')
    cnn_features_folderpath = my_params.get('cnn_features_keras')
    downsampled_videos = my_params.get('downsampled_videos')

    # TODO: Create CNN object

    # Check if folder for CNN features exists
    if not os.path.exists(cnn_features_folderpath):
        os.mkdir(cnn_features_folderpath)

    # Loop over all videos (training, val, testing)
    # TODO: get CNN features for all videos but only from keyframes

    fread = open(all_video_names, "r")
    count = 0
    for line in fread.readlines():
        video_name = line.replace('\n', '')
        downsampled_video_filename = os.path.join(downsampled_videos, video_name + '.ds.mp4')
        cnn_feat_video_filename = os.path.join(cnn_features_folderpath, video_name + '.cnn')

        if not os.path.isfile(downsampled_video_filename):
            continue

        count += 1
        # Get CNN features for one video
        keyframe_interval = 20
        get_cnn_features_from_video(downsampled_video_filename,
                                     cnn_feat_video_filename, keyframe_interval)
        print "done " + str(count)
