# TensorFlow detect speed vehicle
The goal here is to run a TensorFlow-based program
And I solved many problems to solve and run, one of the training tasks with the company Smart methods

The code I have tried it from
#### <p align="center"> [detect-speed-vehicle](https://github.com/bluesven869/detect-speed-vehicle)</p>

The end result when running the code via anaconda Prompt (anaconda3)
![alt text](https://github.com/MohammadYAmmar/entry-to-computer-vision-and-smart-operations-via-Python/blob/master/TensorFlow%20detect%20speed%20vehicle/GIF%20Identification%20of%20the%20vehicle%20and%20monitoring%20of%20the%20violation.gif "result")

![much-a image](https://github.com/MohammadYAmmar/entry-to-computer-vision-and-smart-operations-via-Python/blob/master/TensorFlow%20detect%20speed%20vehicle/Image%20showing%20identification%20of%20the%20car.png) 


The project considered the renewal of cars, their color and the percentage of confirmation about that, in addition to monitoring the speed at a specific place and counting the violating cars

It uses many libraries and this is described in sequence:
![much-a image](https://user-images.githubusercontent.com/22610163/41812993-a4b5a172-7735-11e8-89f6-083ec0625f21.png) 

The code you used was using an old version of TensorFlow so I have modified a number of lines to match the latest version:
1
```
#After [import sys] add
sys.path.append("{YOU_PATH}\models-master\research")
```
2
```
#add
from object_detection.utils import ops as utils_ops #pip install tensorflow-object-detection-api
utils_ops.tf = tf.compat.v1
tf.gfile = tf.io.gfile
```
3
```
#use "tf.compat.v1.GraphDef()" instead if you are using tensorflow 2.0
    # od_graph_def = tf.GraphDef() #Error , to
    od_graph_def = tf.compat.v1.GraphDef()
```
4
```
        #with tf.Session(graph=detection_graph) as sess: #error to
        with tf.compat.v1.Session(graph=detection_graph) as sess:
```

