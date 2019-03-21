import numpy as np

# P001_cnn_file = open("cnn_pred/P001_cnn.lst")
# P002_cnn_file = open("cnn_pred/P002_cnn.lst")
# P003_cnn_file = open("cnn_pred/P003_cnn.lst")
# P001_surf_file = open("surf_pred/P001_surf.lst")
# P002_surf_file = open("surf_pred/P002_surf.lst")
# P003_surf_file = open("surf_pred/P003_surf.lst")
P001_resnet_file = open("resnet_pred/P001_resnet.lst")
P002_resnet_file = open("resnet_pred/P002_resnet.lst")
P003_resnet_file = open("resnet_pred/P003_resnet.lst")
NULL_resnet_file = open("resnet_pred/NULL_resnet.lst")
# P001_early_file = open("early_mfcc_resnet_pred/P001_EF.lst")
# P002_early_file = open("early_mfcc_resnet_pred/P002_EF.lst")
# P003_early_file = open("early_mfcc_resnet_pred/P003_EF.lst")
# NULL_early_file = open("early_mfcc_resnet_pred/NULL_EF.lst")
test_video_file = open("list/test.video")
# test video
test_video = []
for v in test_video_file:
    tmp = v.strip()
    test_video.append(tmp)
'''
# surf
surf_label = []
surf = []
P001_surf = []
P002_surf = []
P003_surf = []
output_surf_file = open("surf_kaggle_prediction.csv", 'w')
for a in P001_surf_file:
    tmp = float(a.strip())
    P001_surf.append(tmp)
for b in P002_surf_file:
    tmp = float(b.strip())
    P002_surf.append(tmp)
for c in P003_surf_file:
    tmp = float(c.strip())
    P003_surf.append(tmp)
surf = np.array([P001_surf, P002_surf, P003_surf])
surf = surf.T
# print surf
output_surf_file.write("VideoID,Label\n")
for i in range(len(surf)):
    tmp_video = test_video[i]
    tmp = tmp_video + ',' + str(np.argmax(surf[i]) + 1) + '\n'
    surf_label.append(tmp)
    output_surf_file.write(tmp)
output_surf_file.close()
'''
'''
# cnn
cnn_label = []
cnn = []
P001_cnn = []
P002_cnn = []
P003_cnn = []
output_cnn_file = open("cnn_kaggle_prediction.csv", 'w')
for a in P001_cnn_file:
    tmp = float(a.strip())
    P001_cnn.append(tmp)
for b in P002_cnn_file:
    tmp = float(b.strip())
    P002_cnn.append(tmp)
for c in P003_cnn_file:
    tmp = float(c.strip())
    P003_cnn.append(tmp)
cnn = np.array([P001_cnn, P002_cnn, P003_cnn])
cnn = cnn.T
# print cnn
output_cnn_file.write("VideoID,Label\n")
for i in range(len(cnn)):
    tmp_video = test_video[i]
    tmp = tmp_video + ',' + str(np.argmax(cnn[i]) + 1) + '\n'
    cnn_label.append(tmp)
    output_cnn_file.write(tmp)
output_cnn_file.close()
'''

# resnet
resnet_label = []
resnet = []
P001_resnet = []
P002_resnet = []
P003_resnet = []
NULL_resnet = []
output_resnet_file = open("resnet_kaggle_prediction.csv", 'w')
for a in P001_resnet_file:
    tmp = float(a.strip())
    P001_resnet.append(tmp)
for b in P002_resnet_file:
    tmp = float(b.strip())
    P002_resnet.append(tmp)
for c in P003_resnet_file:
    tmp = float(c.strip())
    P003_resnet.append(tmp)
for d in NULL_resnet_file:
    tmp = float(d.strip()) - 1
    NULL_resnet.append(tmp)
resnet = np.array([NULL_resnet, P001_resnet, P002_resnet, P003_resnet])
resnet = resnet.T
# print resnet
output_resnet_file.write("VideoID,Label\n")
for i in range(len(resnet)):
    tmp_video = test_video[i]
    tmp = tmp_video + ',' + str(np.argmax(resnet[i])) + '\n'
    resnet_label.append(tmp)
    output_resnet_file.write(tmp)
output_resnet_file.close()

'''
# early mfcc + resnet
early_label = []
early = []
P001_early = []
P002_early = []
P003_early = []
NULL_early = []
output_early_file = open("early_kaggle_prediction.csv", 'w')
for a in P001_early_file:
    tmp = float(a.strip())
    P001_early.append(tmp)
for b in P002_early_file:
    tmp = float(b.strip())
    P002_early.append(tmp)
for c in P003_early_file:
    tmp = float(c.strip())
    P003_early.append(tmp)
for d in NULL_early_file:
    tmp = float(d.strip())
    NULL_early.append(tmp)
early = np.array([NULL_early, P001_early, P002_early, P003_early])
early = early.T
# print early
output_early_file.write("VideoID,Label\n")
for i in range(len(early)):
    tmp_video = test_video[i]
    tmp = tmp_video + ',' + str(np.argmax(early[i])) + '\n'
    early_label.append(tmp)
    output_early_file.write(tmp)
output_early_file.close()
'''