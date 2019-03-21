import numpy as np
import os
import cPickle
from sklearn.cluster.k_means_ import KMeans
import sys
import collections

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: {0} file_list".format(sys.argv[0])
        print "file_list -- the list of videos"
        exit(1)
    file_list = sys.argv[1]
    files = open(file_list)
    output_path = "resnetfeat/feature.vec"
    output = open(output_path, 'w')
    fea_dim = 2048
    for f in files:
        video_name = f.strip()
        cnn_path = "resnet50/{}.npy".format(video_name)
        if os.path.exists(cnn_path) != True:
            print "No CNN features"
            z = np.zeros(fea_dim)
            z.fill(1.0/fea_dim)
            zeros = map(str, z)
            zeros_feature = ';'.join(zeros)
            print zeros_feature
            output.write(video_name + ' ' + zeros_feature + '\n')
            continue
        arr = np.load(cnn_path)
        if len(arr.shape) == 1:
            cnn_vec = arr
        else:
            cnn_vec = np.zeros(fea_dim)
            cnn_vec.fill(1.0 / fea_dim)
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
        feature = ';'.join([str(i) for i in cnn_vec])
        output.write(video_name + ' ' + feature + '\n')
        print "{} done.".format(video_name)
    output.close()
    files.close()

    print "CNN features generated successfully!"
