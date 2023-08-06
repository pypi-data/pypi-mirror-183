
from typing import Tuple

from alphafed import logger


def init_dataset(self, dataset_dir: str) -> Tuple[bool, str]:
    self.dataset_dir = dataset_dir
    try:
        if not self._is_dataset_initialized:
            self.training_loader
            self.validation_loader
            self.testing_loader
            if not self.training_loader or not self.testing_loader:
                logger.error('Both training data and testing data are missing.')
                return False, 'Must provide train dataset and test dataset to fine tune.'
            self.labels = (self.training_loader.dataset.labels
                            if self.training_loader
                            else self.testing_loader.dataset.labels)
            self._is_dataset_initialized = True
        return True, 'Initializing dataset complete.'
    except Exception:
        logger.exception('Failed to initialize dataset.')
        return False, '初始化数据失败，请联系模型作者排查原因。'
