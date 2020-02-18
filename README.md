# AutoDex
Android app able to detect and recognize 40 of the most popular car emblems in real time through the
camera input. The model is a Single Shot MultiBox Detector using MobileNetV2 as the feature extractor. and  based on the [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection).  
  
*Only some code for the dataset creation is provided here.*

## Demo
<img src="https://s5.gifyu.com/images/demo_res70.gif"/>  

## Usage
Download a set of images for a given car brand.  
```
python3 download_images.py --dir=some_dir/images --query=BMW --n_images=100 --format=jpg
```
Delete some garbage images that may be downloaded and proceed with labeling. You can use [this](https://github.com/tzutalin/labelImg) as your annotation tool.  
```
python3 .../labelImg/labelImg.py
```
Split the data into train and test directories inside *some_dir/images*.  
```
python3 train_test_split.py --img_dir=some_dir/images --train_percentage=0.8
```
After running the above steps for each car brand, bring the datasets to TFRecord format.
```
python3 xml_to_csv.py --in_dir=some_dir/images/train --out_dir=some_dir/csv --out_fname=train_labels.csv
python3 xml_to_csv.py --in_dir=some_dir/images/test --out_dir=some_dir/csv --out_fname=test_labels.csv
python3 generate_tfrecord.py --csv_input=./data/csv/train_labels.csv  --output_path=some_dir/tfrecords/train.record --image_dir=some_dir/images/train
python3 generate_tfrecord.py --csv_input=some_dir/csv/test_labels.csv  --output_path=some_dir/tfrecords/test.record --image_dir=some_dir/images/test
```
Now what's left is to pick a model, train it using the [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) and then integrate by editing some example from [here](https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection).  
[Here](https://towardsdatascience.com/detecting-pikachu-on-android-using-tensorflow-object-detection-15464c7a60cd)'s an excellent blogpost explaining all this.
