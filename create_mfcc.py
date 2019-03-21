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
    output_path = "mfccfeat/feature.vec"
    output = open(output_path, 'w')
    fea_dim = 200
    for f in files:
        video_name = f.strip()
        mfcc_path = "mfcc/{}_kmeans.npy".format(video_name)
        if os.path.exists(mfcc_path) != True:
            print "No MFCC features"
            z = np.zeros(fea_dim)
            z.fill(1.0/fea_dim)
            zeros = map(str, z)
            zeros_feature = ';'.join(zeros)
            print zeros_feature
            output.write(video_name + ' ' + zeros_feature + '\n')
            continue
        arr = np.load(mfcc_path)
        if len(arr.shape) == 1:
            mfcc_vec = arr
        else:
            mfcc_vec = np.zeros(fea_dim)
            mfcc_vec.fill(1.0 / fea_dim)
        feature = ';'.join([str(i) for i in mfcc_vec])
        output.write(video_name + ' ' + feature + '\n')
        print "{} done.".format(video_name)
    output.close()
    files.close()

    print "MFCC features generated successfully!"
