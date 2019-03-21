import numpy as np
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: {0} event_name feat_dir feat_dim output_file".format(sys.argv[0])
        print "event_name -- name of the event (P001, P002 or P003 in Homework 1)"
        exit(1)
    event_name = sys.argv[1]
    output_path = 'late_mfcc_resnet_pred/{}_LF.lst'.format(event_name)
    # mfcc + resnet
    mfcc_path = 'mfcc_pred/{}_mfcc.lst'.format(event_name)
    mfcc_pred = open(mfcc_path, 'r')
    resnet_path = 'resnet_pred/{}_resnet.lst'.format(event_name)
    resnet_pred = open(resnet_path, 'r')
    mfcc_arr = []
    resnet_arr = []
    for a in mfcc_pred:
        tmp = float(a.strip())
        mfcc_arr.append(tmp)
    mfcc_arr = np.array(mfcc_arr)
    for b in resnet_pred:
        tmp = float(b.strip())
        resnet_arr.append(tmp)
    resnet_arr = np.array(resnet_arr)
    # print('mfcc len:', mfcc_arr.shape)
    # print('resnet len:', resnet_arr.shape)
    output_arr = (mfcc_arr + resnet_arr) / 2.0
    output = open(output_path, 'w')
    for i in output_arr:
        output.write(str(i)+'\n')
    output.close()