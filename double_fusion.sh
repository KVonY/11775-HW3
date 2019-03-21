#!/usr/bin/env bash

# Paths to different tools;
map_path=/home/ubuntu/tools/mAP
export PATH=$map_path:$PATH

# ================================================================================================

echo "#############################################################"
echo "# MED with Double Fusion MFCC & ResNet Features: MAP results  #"
echo "#############################################################"

mkdir -p double_mfcc_resnet_pred
# iterate over the events
for event in P001 P002 P003 NULL; do
  echo "=========  Event $event Double Fusion  ========="
  # now perform late fusion
  python double_fusion.py $event;
  # compute the average precision by calling the mAP package
  ap list/${event}_val_label double_mfcc_resnet_pred/${event}_DF.lst
done
#=======================================================