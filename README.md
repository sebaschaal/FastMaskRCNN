# Fast Mask RCNN
Mask RCNN in TensorFlow  
This repo attempts to reporduce this amazing work by Kaiming He.
[Mask RCNN](https://arxiv.org/abs/1703.06870).

## Known Problems
- [x] Allocate-Zero-Memory Error, solved by @santisy
- [ ] Allowing larger initial learning rate. 
- [ ] Chooseing proper initial weights.
## How-to
1. `git clone https://github.com/CharlesShang/FastMaskRCNN.git`
2. `cd FastMaskRCNN/libs && make`
3. `cd datasets/pycocotools && make`
4. `cd ../../.. && mkdir train && mkdir train/maskrcnn`
4. `nano download_and_convert_data.py`
    Rename all appearances of dataset_name and dataset_dir
5. Download coco dataset, place it into `./data`, then run `python download_and_convert_data.py` to build tf-record. It takes a while.
6. Download pretrained resnet50 model, `wget http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz`, unzip it, place it into `./data/pretrained_models/`
7. run `python test/resnet50_test.py` for training 
8. There are certainly some bugs, please report them back, and let's solve them togather.
## Timeline
- [x] ROIAlign
- [x] COCO Data Provider
- [x] Resnet50
- [x] Feature Pyramid Network
- [x] Anchor and ROI layer
- [x] Mask layer
- [x] Speedup anchor layer with cython
- [x] Combining all modules together. 
- [x] Testing and debugging (in progress)
- [ ] Training / evaluation on COCO
- [ ] Data queue
- [ ] Data agument
- [ ] Other backbone networks
- [ ] Training >2 images

## Call for contribution
- Anything helps this repo, including **discussion**, **testing**, **promotion** and of course **your awesome code**. 
