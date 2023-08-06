# Auto-Deep-Learning (Auto Deep Learning)
[![Downloads](https://static.pepy.tech/personalized-badge/auto-deep-learning?period=month&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/auto_deep_learning) ![Version](https://img.shields.io/badge/version-0.1.1-blue) ![Python-Version](https://img.shields.io/badge/python-3.9-blue) ![issues](https://img.shields.io/github/issues/Nil-Andreu/auto_deep_learning) ![PyPI - Status](https://img.shields.io/pypi/status/auto_deep_learning) ![License](https://img.shields.io/github/license/Nil-Andreu/auto_deep_learning) 

```auto_deep_learning```: with this package, you will be able to create, train and deploy neural networks automatically based on the input that you provide.

## Alert
This package is still on development, but Start the Project to know further updates in next days!
For the moment, would be for computer vision classification tasks on images (multi-modal included).

## Installation
Use the package manager [pip](https://pypi.org/project/pip/) to install *auto_deep_learning*.

To install the package:
```bash
    pip install auto_deep_learning
```

**If using an old version of the package, update it:**
```bash
    pip install --upgrade auto_deep_learning
```


## Project Structure
The project structure is the following one:

```bash
    ├── auto_deep_learning                  # Python Package
    │   ├── cloud                           # Cloud module for saving & service DL models
    │   │   ├── aws                         # Amazon Web Services
    │   │   └── gcp                         # Google Cloud
    │   ├── enum                            # Enumerations for the model
    │   ├── exceptions                      # Exceptions 
    │   │   ├── model                       # Exceptions related to the definition/creation of the model
    │   │   └── utils                       # Exceptions related to the utilities folder
    │   │       └── data_handler            # Exceptions related to handling the data
    │   ├── model                           # Module for creating & training the models 
    │   │   └── arch                        # Architectures supported of the models
    │   │       └── convolution
    │   ├── schemas                         # Schemas of expected outputs
    │   └── utils                           # Utilities for the project
    │       ├── data_handler                # Utilities related to handling the data
    │       │   ├── creator                 # Utilities related to creating the loaders
    │       │   └── transform               # Utilities related to the transformation of the data
    │       └── model                       # Utilities related to the creation of the model
    ├── examples                            # Examples of how the package can be used
    └── tests                               # Tests
```


## Basic Usage
How easy can be to create and train a deep learning model:
```python
    from auto_deep_learning import Model
    from auto_deep_learning.utils import DataCreator, DataSampler, image_folder_convertion

    df = image_folder_convertion()
    data = DataCreator(df)
    data_sampled = DatasetSampler(data)
    model = Model(data_sampled)
    model.fit()
    model.predict('image.jpg')
```

We provide also with a configuration object, where it centralizes some of the most important configurations that you might want to do:
```python
    ConfigurationObject(
        n_epochs: int = 10,
        batch_size_train: int = 64,
        batch_size_valid: int = 128,
        batch_size_test: int = 128,
        valid_size: float = 0.1,
        test_size: float = 0.05,
        image_size: int = 224,
        num_workers: int = 6,
        objective: ModelObjective = ModelObjective.THROUGHPUT,
        img_transformers: Dict[str, ImageTransformer] =  {
            'train': ImageTransformer(
                rotation=3.0,
                color_jitter_brightness=3.0,
                color_jitter_contrast=3.0,
                color_jitter_hue=3.0,
                color_jitter_saturation=3.0,
                color_jitter_enabled=True,
                resized_crop_enabled=True
            ),
            'valid': ImageTransformer(),
            'test': ImageTransformer()
        }
    )
```
So by default, it is going to do image augmentation on the training data.
Note that if for example we did not want to make a validation split because our dataset is too small, we would change this value as:

```python
    conf_obj = ConfigurationObject()
    conf_obj.valid_size = 0.0
```


### Dataset

The data that it expects is a pd.DataFrame(), where the columns are the following:
```
    - image_path: the path to the image
    - class1: the classification of the class nr. 1. For example: {t-shirt, glasses, ...}
    - class2: the classification of the class nr. 2. For example: {summer, winter, ...}
    - ...
    - split_type: whether it is for train/valid/test
```
For better performance, it is suggested that the classes and the type are of dtype *category* in the pandas DataFrame.
If the type is not provided in the dataframe, you should use the utils function of *data_split_types* (in *utils.dataset.sampler* file). 

If instead you have the images ordered in the structure of ImageFolder, which is the following structure:
```
    train/  
        class1_value/
            1.jgp
            2.jpg
            ...
        class2_value/
            3.jpg
            4.jpg
            ...
    test/
        class1_value/
            1.jgp
            2.jpg
            ...
        class2_value/
            3.jpg
            4.jpg
            ...
```
For simplifying logic, we have provided a logic that gives you the expected dataframe that we wanted, with the function of *image_folder_convertion* (in *utils.functions*), where it is expecting a path to the parent folder where the *train/* and */test* folders are.