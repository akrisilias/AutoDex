# AutoDex
Android app able to detect and recognize 40 of the most popular car emblems in real time through the
camera input. The model is a Single Shot MultiBox Detector using MobileNetV2 as the feature extractor.  
  
*Only some code for the dataset creation is provided here.*

## Demo
<img src="https://s5.gifyu.com/images/demo_cropped69cd0d234cb2b9a0.gif"/>  

## Usage
Download a set of images for a given car brand.  
*Currently undergoing issue [#280](https://github.com/hardikvasa/google-images-download/issues/280) [#298](https://github.com/hardikvasa/google-images-download/pull/298)*
```
python3 download_images.py --dir=some_dir/images --query=BMW --n_images=100 --format=jpg
```
Delete some garbage images that may be downloaded and proceed with labeling. You can use [this](https://github.com/tzutalin/labelImg) as your annotation tool.  
```
python3 .../labelImg/labelImg.py
```
Split the data into train and test directories inside *some_dir/images*.  
```
python3 train_test_split.py --image_dir=some_dir/images --train_percentage=0.8
```
After running the above steps for each car brand, bring the dataset to csv format.
```
python3 xml_to_csv.py --in_dir=some_dir/images/train --out_dir=some_dir/csv --out_fname=train_labels.csv
python3 xml_to_csv.py --in_dir=some_dir/images/test --out_dir=some_dir/csv --out_fname=test_labels.csv
```
Now what's left is to bring the dataset to TFRecord format, pick a model, train it using the [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) and then integrate by editing some example from [here](https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection).  
[Here](https://towardsdatascience.com/detecting-pikachu-on-android-using-tensorflow-object-detection-15464c7a60cd)'s an excellent blogpost explaining all this.
