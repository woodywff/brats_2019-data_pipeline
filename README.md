# Data_pipeline for BraTS 2019 Dataset
This is a small piece of the project I'm working on currently, but still I'd like to publish it here because I hope this may help a little bit for people who're interested in playing with the [BraTS 2019](https://www.med.upenn.edu/cbica/brats2019.html) dataset.

In general, I've reconstructed the pipeline code in [this repository](https://github.com/woodywff/brats_2019]) with `h5py`.

To get started, you just need to unzip the downloaded datasets into the `brats_2019-data_pipeline/data` folder. Then to do the preprocess you can go with 
```
from preprocess import preprocess
preprocess()
```
The preprocess involves calculating the mean values and the standard deviations of all brain area voxels and making the z-score normalization for each modality. We also do the min-max scaling on every single image. For more details please refer to [this article](https://arxiv.org/abs/1909.12901). `preprocess()` also includes the split for cross validations.


The `Dataset` class in `generator.py` is designed for training and validation processes. 
```
import generator
dataset = generator.Dataset()
```
You could get the iterable generator for training by `dataset.train_generator` and for validation by `dataset.val_generator`.

## Acknowledgement
Again, this work is based on [my former repository](https://github.com/woodywff/brats_2019]) which inherited from [ellisdg's repository](https://github.com/ellisdg/3DUnetCNN.git). Deeply appreciate [ellisdg](https://github.com/ellisdg)'s contributions to the community.

Many thanks to the host of the [BraTS challenges](https://www.med.upenn.edu/cbica/brats2019.html).
