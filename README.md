# Instrument Detection
This repository houses code for detecting and tracking instruments in concert videos. This project was done with Prof. Serge Belongie and Debarun Dhar at Cornell in Fall 2017.
Original SSD code can be found at https://github.com/weiliu89/caffe/tree/ssd

## Installation
1. Get the code. We will call the directory that you cloned Caffe into `$CAFFE_ROOT`
  ```Shell
  git clone https://github.com/tsankar/instrument-detection
  cd instrument-detection
  ```

2. Build the code. Please follow [Caffe instruction](http://caffe.berkeleyvision.org/installation.html) to install all necessary packages and build it.
  ```Shell
  # Modify Makefile.config according to your Caffe installation.
  cp Makefile.config.example Makefile.config
  make -j8
  # Make sure to include $CAFFE_ROOT/python to your PYTHONPATH.
  make py
  make test -j8
  # (Optional)
  make runtest -j8
  ```

## Detection
See [`module/README.md`](module/README.md) for more info.

## Training

### Data Preparation
Follow the instructions at [`data/ILSVRC2016/README.md`](data/ILSVRC2016/README.md) to format ImageNet-like data into an LMDB database.
Don't forget to modify the .txt files in `$ILSVRC_ROOT/ImageSets/DET` to split your data accordingly.
This project used the following ImageNet synsets for training:
* guitar
* bass guitar
* acoustic guitar
* electric guitar
* Hawaiian guitar, steel guitar
* drum, membranophone, tympan
* snare drum, snare, side drum
* person
Finally, you must modify [`data/ILSVRC2016/labelmap_ilsvrc_det.prototxt`](data/ILSVRC2016/labelmap_ilsvrc_det.prototxt) to match the classes in your dataset.

### Fine Tuning
Be sure to download a pretrained model from the links below.
The model can be fine tuned using the script at [`examples/ssd/ssd_ilsvrc.py`](examples/ssd/ssd_ilsvrc.py). Additionally, [`examples/ssd/frozen_ssd_ilsvrc.py`](examples/ssd/frozen_ssd_ilsvrc.py) is provided, which doesn't recreate the train.prototxt, allowing individual layers to be frozen.
Make sure to update all relevant paths in either file (pretrained model, LMDB databases) and change all hyperparameters to fit your experiment.

## Models
These are the pretrained SSD models provided by the original authors. This project used the ILSVRC model.
To help reproduce the results in [Table 6](https://arxiv.org/pdf/1512.02325v4.pdf), most models contain a pretrained `.caffemodel` file, many `.prototxt` files, and python scripts.

1. PASCAL VOC models:
   * 07+12: [SSD300*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712_SSD_300x300.tar.gz), [SSD512*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712_SSD_512x512.tar.gz)
   * 07++12: [SSD300*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712Plus_SSD_300x300.tar.gz), [SSD512*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712Plus_SSD_512x512.tar.gz)
   * COCO<sup>[1]</sup>: [SSD300*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712_SSD_300x300_coco.tar.gz), [SSD512*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712_SSD_512x512_coco.tar.gz)
   * 07+12+COCO: [SSD300*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712_SSD_300x300_ft.tar.gz), [SSD512*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712_SSD_512x512_ft.tar.gz)
   * 07++12+COCO: [SSD300*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712Plus_SSD_300x300_ft.tar.gz), [SSD512*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_VOC0712Plus_SSD_512x512_ft.tar.gz)

2. COCO models:
   * trainval35k: [SSD300*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_coco_SSD_300x300.tar.gz), [SSD512*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_coco_SSD_512x512.tar.gz)

3. ILSVRC models:
   * trainval1: [SSD300*](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_ILSVRC2016_SSD_300x300.tar.gz), [SSD500](http://www.cs.unc.edu/~wliu/projects/SSD/models_VGGNet_ilsvrc15_SSD_500x500.tar.gz)

<sup>[1]</sup>We use [`examples/convert_model.ipynb`](https://github.com/weiliu89/caffe/blob/ssd/examples/convert_model.ipynb) to extract a VOC model from a pretrained COCO model.
