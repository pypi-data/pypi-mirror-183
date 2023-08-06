from __future__ import annotations


from collections import defaultdict
import copy
import logging
import random
import re
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from .prefetch_generator import PrefetchGenerator
from ..utils import is_available

import numpy as np
if is_available("tensorflow"):
    import tensorflow as tf
if is_available("torch"):
    import torch


logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s", level=logging.NOTSET)
logger = logging.getLogger(__name__)


class Dataset:
    """
    """

    def __init__(self, data: List[Dict[str, Any]] = None, **kwargs) -> None:
        self._data = data if data is not None else []
        self._length = 0

    def append(self, data: Dict[str, Any]):
        self._data.append(data)

    add = append

    def drop(self, condition):
        return self.filter(lambda x: not condition(x))

    def filter(self, condition):
        return Dataset(list(filter(condition, self._data)))

    def merge(self, key, values):
        new_values = "+".join(values)
        return Dataset([{k: (new_values if (key == k and d[k] in values) else d[k]) for k in d.keys()} for d in self._data])

    def __add__(self, other: Dataset):
        cls = Dataset(shuffle=self._shuffle, batch_size=self._batch_size)
        cls._data.extend(copy.deepcopy(self._data))
        cls._data.extend(copy.deepcopy(other._data))
        cls._length = self._length + other._length
        return cls

    def __radd__(self, other: Dataset):
        return self + other

    def __getitem__(self, index: slice):
        cls = Dataset()
        data = self._data[index]
        if isinstance(data, dict):
            cls._data.append(data)
            cls._length = 1
        else:
            cls._data.extend(data)
            cls._length = len(data)
        return cls

    def __len__(self):
        return self.num_data

    @property
    def data(self):
        if self._shuffle:
            random.shuffle(self._data)
        return self._data

    @property
    def num_data(self):
        if self._length == 0:
            self._length = len(self._data)
        return self._length

    def get_items(self, max_display):
        _items = defaultdict(lambda: defaultdict(int))
        for d in self._data:
            for k, v in d.items():
                if len(_items[k]) < max_display:
                    _items[k][v] += 1
        return {k1: dict(v1) for k1, v1 in _items.items()}
    
    def print_items(self, max_display=10):
        _items = self.get_items(max_display)
        _repr = []
        for k, v in _items.items():
            _tmp = []
            for _i, (_k, _v) in enumerate(v.items()):
                _tmp.append(f"{_k if _v == 1 else f'{_k}({_v})'}")
                if _i+1 == max_display:
                    _tmp.append("...")
                    break
            _repr.append(f"{k}: {', '.join(_tmp)}")
        _repr = "\n".join(_repr)
        _repr = re.sub(r"^", " " * 4, _repr, 0, re.M)
        logger.info(f"Dataset: {self.num_data}\n{_repr}")

    def __repr__(self):
        return f"Dataset: {self.num_data}\n"

    def __iter__(self):
        return iter(self._data)


class DataLoader:
    def __init__(self, dataset: Dataset, shuffle: bool = False, batch_size: int = 1, collate_fn: Optional[Callable] = None, prefetch_factor: int = 1, num_workers: int = 1, format: Optional[str] = None, padding_value: int = 0, **kwargs) -> None:
        self.dataset = dataset
        self._shuffle = shuffle
        self._batch_size = batch_size
        self._collate_fn = collate_fn
        self._prefetch_factor = prefetch_factor
        self._num_workers = num_workers
        self._format = format if format in {"tf", "torch"} else "numpy"
        self._padding_value = padding_value
        self._gen = PrefetchGenerator(self.dataset._data, num_prefetch=self._prefetch_factor*self._batch_size, num_workers=self._num_workers, shuffle=self._shuffle, processing_func=self._collate_fn, name="DataLoader")

    def as_format(self, batch):
        if is_available("numpy"):
            ranks = [len(b) for b in batch]
            rank = np.unique(ranks)
            if len(rank) == 1:
                rank = rank[0]
                datas = [[] for _ in range(rank)]
                for b in batch:
                    for i in range(rank):
                        datas[i].append(b[i])
                for i, data in enumerate(datas):
                    max_len = np.amax(np.array([d.shape if hasattr(d, "__len__") else 1 for d in data]), axis=0)
                    min_len = np.amin(np.array([d.shape if hasattr(d, "__len__") else 1 for d in data]), axis=0)
                    if np.all(max_len == min_len):
                        datas[i] = np.array(data)
                    else:
                        padded_begin = np.zeros(max_len.shape).astype(np.int32)
                        datas[i] = np.array([np.pad(d, np.stack((padded_begin, max_len - d.shape)).T, constant_values=self._padding_value) for d in data])                        
            else:
                raise ValueError("collate_fn에서 출력하는 데이터의 개수가 동일하지 않습니다.")
        else:
            raise ModuleNotFoundError("numpy")
        if self._format == "tf":
            if is_available("tensorflow"):
                for i in range(len(datas)):
                    datas[i] = tf.convert_to_tensor(datas[i])
            else:
                raise ModuleNotFoundError("tensorflow")
        elif self._format == "torch":
            if is_available("torch"):
                for i in range(len(datas)):
                    datas[i] = torch.tensor(datas[i])
            else:
                raise ModuleNotFoundError("torch")
        return datas

    def __next__(self):
        data = []
        for _ in range(self._batch_size):
            try:
                data.append(next(self._gen))
            except StopIteration:
                if data:
                    return self.as_format(data)
                else:
                    raise StopIteration
        return self.as_format(data)

    def __iter__(self):
        return self

    def __len__(self):
        return self.dataset.num_data//self._batch_size + (0 if self.dataset.num_data%self._batch_size == 0 else 1)