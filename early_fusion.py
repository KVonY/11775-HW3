# mfcc & cnn

import numpy as np
import os
import sys


# resnet50: 2048
# mfcc: 200
# soundnet: 1401

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: {0} file_list".format(sys.argv[0])
        print "file_list -- the list of videos"
        exit(1)
    file_list = sys.argv[1]
    files = open(file_list)
    mfcc_resnet_output_path = "earlyfusion/mfcc_resnet_feature.vec"
    soundnet_resnet_output_path = "earlyfusion/soundnet_resnet_feature.vec"
    mfcc_resnet_output = open(mfcc_resnet_output_path, 'w')
    soundnet_resnet_output = open(soundnet_resnet_output_path, 'w')
    resnet_dim = 2048
    mfcc_dim = 200
    soundnet_dim = 1401
    mfcc_resnet_fea_dim = 2048 + 200 # 2248
    soundnet_resnet_fea_dim = 1401 + 2048 # 3449
    for f in files:
        video_name = f.strip()
        resnet_path = "resnet50/{}.npy".format(video_name)  # 3444
        mfcc_path = "mfcc/{}_kmeans.npy".format(video_name)   # 2963
        soundnet_path = "soundnet/{}.feats".format(video_name)   # 2963
        if os.path.exists(resnet_path) != True:
            print "No ResNet features"
            z = np.zeros(resnet_dim)
            z.fill(1.0/resnet_dim)
            # zeros = map(str, z)
            # zeros_feature = ';'.join(zeros)
            # print zeros_feature
            resnet_arr = z
        else:
            resnet_arr = np.load(resnet_path)

        if os.path.exists(mfcc_path) != True:
            z = np.zeros(mfcc_dim)
            z.fill(1.0 / mfcc_dim)
            mfcc_arr = z
        else:
            mfcc_arr = np.load(mfcc_path)

        if os.path.exists(soundnet_path) != True:
            z = np.zeros(soundnet_dim)
            z.fill(1.0 / soundnet_dim)
            soundnet_arr = z
        else:
            soundnet_file = open(soundnet_path, 'r')
            for i in soundnet_file:
                tmp = i.strip().split(';')
                tmp = np.array(tmp)
            soundnet_arr = tmp

        # if len(resnet_arr.shape) == 1:
        #     resnet_vec = resnet_arr
        # else:
        #     cnn_vec = np.zeros(fea_dim)
        #     cnn_vec.fill(1.0 / fea_dim)
        # # bag-of-word vector representation
        # label_count = collections.Counter(labels) # dictionary
        # for i in range(fea_dim):
        #     bow[i] = label_count[i]
        # normalize
        # if np.sum(cnn_vec) == 0:
        #     vec = np.zeros(fea_dim)
        #     vec.fill(1.0/fea_dim)
        # #     print "WRONG bag-of-word vector representation\n"
        # else:
        #     vec = cnn_vec
        #     vec = vec / float(np.sum(cnn_vec))

        # output
        mfcc_resnet_arr = np.concatenate((mfcc_arr, resnet_arr))
        soundnet_resnet_arr = np.concatenate((soundnet_arr, resnet_arr))
        mfcc_resnet_feature = ';'.join([str(i) for i in mfcc_resnet_arr])
        soundnet_resnet_feature = ';'.join([str(i) for i in soundnet_resnet_arr])
        mfcc_resnet_output.write(video_name + ' ' + mfcc_resnet_feature + '\n')
        soundnet_resnet_output.write(video_name + ' ' + soundnet_resnet_feature + '\n')
        print "{} done.".format(video_name)
    mfcc_resnet_output.close()
    soundnet_resnet_output.close()
    files.close()

    print "CNN features generated successfully!"
