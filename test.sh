#!/usr/bin/env bash

# Paths to different tools;
map_path=/home/ubuntu/tools/mAP
export PATH=$map_path:$PATH

# ================================================================================================

##echo "#######################################"
##echo "# MED with ResNet Features: MAP results  #"
##echo "#######################################"
##
#mkdir -p resnet_pred
## iterate over the events
#feat_dim_resnet=2048
#use=kaggle
#for event in P001 P002 P003 NULL; do
#  echo "=========  Event $event  ========="
#  # now train a svm model
#  python train_svm.py $event "resnetfeat/" $feat_dim_resnet resnet_pred/svm.$event.model $use;
#  # apply the svm model to *ALL* the testing videos;
#  # output the score of each testing video to a file ${event}_pred
#  python test_svm.py resnet_pred/svm.$event.model "resnetfeat/" $feat_dim_resnet resnet_pred/${event}_resnet.lst $use;
#  # compute the average precision by calling the mAP package
#  ap list/${event}_val_label resnet_pred/${event}_resnet.lst
#done
# ================================================================================================


# python kaggle.py


# ================================================================================================
#echo "########################################"
#echo "# MED with MFCC Features: MAP results  #"
#echo "########################################"
#
#mkdir -p mfcc_pred
## iterate over the events
#feat_dim_mfcc=200
#use=kaggle
#for event in P001 P002 P003 NULL; do
#  echo "=========  Event $event  ========="
#  # now train a svm model
#  python train_svm.py $event "mfccfeat/" $feat_dim_mfcc mfcc_pred/svm.$event.model $use;
#  # apply the svm model to *ALL* the testing videos;
#  # output the score of each testing video to a file ${event}_pred
#  python test_svm.py mfcc_pred/svm.$event.model "mfccfeat/" $feat_dim_mfcc mfcc_pred/${event}_mfcc.lst $use;
#  # compute the average precision by calling the mAP package
#  ap list/${event}_val_label mfcc_pred/${event}_mfcc.lst
#done
# ================================================================================================

# ================================================================================================
echo "#################################################"
echo "# MED with Early ResNet & MFCC Features: MAP results  #"
echo "#################################################"

mkdir -p early_mfcc_resnet_pred
# iterate over the events
feat_dim_mfcc_resnet=2248
use=kaggle
for event in P001 P002 P003 NULL; do
  echo "=========  Event $event  ========="
  # now train a svm model
  python train_svm.py $event "earlyfusion/mfcc_resnet/" $feat_dim_mfcc_resnet early_mfcc_resnet_pred/svm.$event.model $use;
  # apply the svm model to *ALL* the testing videos;
  # output the score of each testing video to a file ${event}_pred
  python test_svm.py early_mfcc_resnet_pred/svm.$event.model "earlyfusion/mfcc_resnet/" $feat_dim_mfcc_resnet early_mfcc_resnet_pred/${event}_EF.lst $use;
  # compute the average precision by calling the mAP package
  ap list/${event}_val_label early_mfcc_resnet_pred/${event}_EF.lst
done
# ================================================================================================


# ================================================================================================
#
#echo "#################################################"
#echo "# MED with Early ResNet & MFCC Features: MAP results  #"
#echo "#################################################"
#
#mkdir -p early_mfcc_resnet_pred
## iterate over the events
#feat_dim_mfcc_resnet=2248
#use=map
#for event in P001 P002 P003 NULL; do
#  echo "=========  Event $event  ========="
#  # now train a svm model
#  python train_svm.py $event "earlyfusion/mfcc_resnet" $feat_dim_mfcc_resnet early_mfcc_resnet_pred/svm.$event.model $use;
#  # apply the svm model to *ALL* the testing videos;
#  # output the score of each testing video to a file ${event}_pred
#  python test_svm.py early_mfcc_resnet_pred/svm.$event.model "resnetfeat/" $feat_dim_mfcc_resnet early_mfcc_resnet_pred/${event}_EF.lst $use;
#  # compute the average precision by calling the mAP package
#  ap list/${event}_val_label early_mfcc_resnet_pred/${event}_EF.lst
#done
# ================================================================================================