# VocToYolo

VocToYolo is a tool for converting a TensorFlow Voc dataset into a YOLO compatible dataset. This tool also allows the **conversion of an image containing more than one label** (multi-label).
You can use this tool, to help you with a label tool like this https://github.com/Microsoft/VoTT

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need lxml to parse TensorFlow Voc dataset

```
pip3 install lxml
```

### Installing

You just have to clone the repository

```
git clone https://github.com/Nicolas-Constanty/VocToYolo.git
```

## Running

### Linux

```
cd ./VocToYolo/
py voctoyolo.py -s "./exemple/TensorFlow Pascol VOC/"
```

This should generate a file structure like this :
```
VocToYolo
         |__ data
                |__ obj.data
                |__ obj.names
                |__ test.txt
                |__ train.txt
                |__ obj
                       |__ img0.jpg
                       |__ img0.txt
                       |__ img1.jpg
                       |__ img1.txt
                       |__ imgN.jpg
                       |__ imgN.txt
```

If you want to customize project name, you can use -n

```
cd ./VocToYolo/
py voctoyolo.py -s "./exemple/TensorFlow Pascol VOC/" -n card_recognition
```

This should generate a file structure like this :
```
VocToYolo
         |__ data
                |__ card_recognition.data
                |__ card_recognition.names
                |__ test.txt
                |__ train.txt
                |__ card_recognition
                                    |__ img0.jpg
                                    |__ img0.txt
                                    |__ img1.jpg
                                    |__ img1.txt
                                    |__ imgN.jpg
                                    |__ imgN.txt
```

### Window
```
cd .\VocToYolo\
py voctoyolo.py -s "./exemple/TensorFlow Pascol VOC/"
```

This should generate a file structure like this :
```
VocToYolo
         |__ data
                |__ obj.data
                |__ obj.names
                |__ test.txt
                |__ train.txt
                |__ obj
                       |__ img0.jpg
                       |__ img0.txt
                       |__ img1.jpg
                       |__ img1.txt
                       |__ imgN.jpg
                       |__ imgN.txt
```

If you want to customize project name, you can use -n

```
cd .\VocToYolo\
py voctoyolo.py -s "./exemple/TensorFlow Pascol VOC/" -n card_recognition
```

This should generate a file structure like this :
```
VocToYolo
         |__ data
                |__ card_recognition.data
                |__ card_recognition.names
                |__ test.txt
                |__ train.txt
                |__ card_recognition
                                    |__ img0.jpg
                                    |__ img0.txt
                                    |__ img1.jpg
                                    |__ img1.txt
                                    |__ imgN.jpg
                                    |__ imgN.txt
```

### Help

```
cd .\VocToYolo\
py voctoyolo.py -h
```

### Options

 - -s \<Source folder>
 - -n \<Project Name>
 - -o \<Output folder>
 - -l \<Label file>

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details
