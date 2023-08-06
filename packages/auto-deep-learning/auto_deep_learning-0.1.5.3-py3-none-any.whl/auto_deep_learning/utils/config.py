from typing import Dict, Any

from .singleton import Singleton
from auto_deep_learning.utils.data_handler.transform.augmentation import ImageTransformer
from auto_deep_learning.enum import ModelObjective, OptimizerType


class ConfigurationObject(metaclass=Singleton):
    def __init__(
        self,
        n_epochs: int = 10,
        batch_size_train: int = 64,
        batch_size_valid: int = 128,
        batch_size_test: int = 128,
        valid_size: float = 0.1,
        test_size: float = 0.05,
        image_size: int = 224,
        num_workers: int = 6,
        optimizer: OptimizerType = OptimizerType.ADAM,
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
        },
    ):

        self._img_transformers = img_transformers
        self._batch_size: Dict[str, int] = {
            'train': batch_size_train,
            'valid': batch_size_valid,
            'test': batch_size_test
        }
        self._valid_size: int = valid_size
        self._test_size: int = test_size
        self._image_size: int = image_size
        self._num_workers: int = num_workers  # TODO: https://discuss.pytorch.org/t/guidelines-for-assigning-num-workers-to-dataloader/813/4
        self._n_epochs: int = n_epochs
        self._objective: str = objective
        self._optimizer: str = optimizer


    @property
    def optimizer(self):
        return self._optimizer
    

    @optimizer.setter
    def optimizer(self, new_optimizer):
        self._optimizer = new_optimizer
        return self._optimizer


    @property
    def objective(self):
        return self._objective
    

    @objective.setter
    def objective(self, new_objective):
        self._objective = new_objective
        return self._objective


    @property
    def n_epochs(self):
        return self._n_epochs
    

    @n_epochs.setter
    def n_epochs(self, new_n_epochs):
        self._n_epochs = new_n_epochs
        return self._n_epochs


    @property
    def batch_size(self):
        return self.batch_size
    

    @batch_size.setter
    def batch_size(self, split_type, new_batch_size):
        self._batch_size[split_type] = new_batch_size

        return self._batch_size
    

    @property
    def num_workers(self):
        return self._num_workers
    

    @num_workers.setter
    def num_workers(self, new_num_workers):
        self._num_workers = new_num_workers

        return self._num_workers

    @property
    def valid_size(self):
        return self._valid_size
    

    @valid_size.setter
    def valid_size(self, new_valid_size):
        self._valid_size = new_valid_size
        return self._valid_size

    
    @property
    def test_size(self):
        return self._test_size
    

    @test_size.setter
    def test_size(self, new_test_size):
        self._test_size = new_test_size
        return self._test_size


    @property
    def image_size(self):
        return self._image_size
    

    @image_size.setter
    def image_size(self, new_image_size):
        self._image_size = new_image_size
        return self._image_size