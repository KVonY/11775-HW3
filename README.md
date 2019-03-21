# 11775-HW3

## To run the whole pipeline
bash run.pipeline.sh -p true -f true -m true -k true -y filepath

## To run only the SVM part
./test.sh

## To perform early fusion
uncomment early fusion in test.sh
./test.sh

## To perform late fusion
./late_fusion.sh

## To perform double fusion
./double_fusion.sh
