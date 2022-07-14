"""Load tfrecord files into torch datasets."""

import numpy as np
import torch.utils.data
from typing import Union, Optional, Callable, List, Dict, Any, Tuple

from slideflow.tfrecord import reader
from slideflow.tfrecord import iterator_utils


class TFRecordDataset(torch.utils.data.IterableDataset):
    """Parse (generic) TFRecords dataset into `IterableDataset` object,
    which contain `np.ndarrays`s. By default (when `sequence_description`
    is None), it treats the TFRecords as containing `tf.Example`.
    Otherwise, it assumes it is a `tf.SequenceExample`.

    Params:
    -------
    data_path: str
        The path to the tfrecords file.

    index_path: str or None
        The path to the index file.

    description: list or dict of str, optional, default=None
        List of keys or dict of (key, value) pairs to extract from each
        record. The keys represent the name of the features and the
        values ("byte", "float", or "int") correspond to the data type.
        If dtypes are provided, then they are verified against the
        inferred type for compatibility purposes. If None (default),
        then all features contained in the file are extracted.

    shuffle_queue_size: int, optional, default=None
        Length of buffer. Determines how many records are queued to
        sample from.

    transform : a callable, default = None
        A function that takes in the input `features` i.e the dict
        provided in the description, transforms it and returns a
        desirable output.

    sequence_description: list or dict of str, optional, default=None
        Similar to `description`, but refers to the sequence features
        within a `SequenceExample`. When this field is `None`, then it
        is assumed that an `Example` is being read otherwise, a
        `SequenceExample` is read. If an empty list or dictionary is
        passed, then all features contained in the file are extracted.

    compression_type: str, optional, default=None
        The type of compression used for the tfrecord. Choose either
        'gzip' or None.

    """

    def __init__(
        self,
        data_path: str,
        index_path: Union[str, None] = None,
        description: Union[List[str], Dict[str, str], None] = None,
        shuffle_queue_size: Optional[int] = None,
        transform: Callable[[dict], Any] = None,
        sequence_description: Union[List[str], Dict[str, str], None] = None,
        compression_type: Optional[str] = None,
        autoshard: bool = False,
        clip: Optional[int] = None,
    ) -> None:
        super(TFRecordDataset, self).__init__()
        self.data_path = data_path
        self.index_path = index_path
        self.description = description
        self.sequence_description = sequence_description
        self.shuffle_queue_size = shuffle_queue_size
        self.transform = transform or (lambda x: x)
        self.compression_type = compression_type
        self.autoshard = autoshard
        self.clip = clip

    def __iter__(self):
        worker_info = torch.utils.data.get_worker_info()
        if self.autoshard and worker_info is not None:
            shard = worker_info.id, worker_info.num_workers
            np.random.seed(worker_info.seed % np.iinfo(np.uint32).max)
        else:
            shard = None
        it = iter(reader.tfrecord_loader(
            data_path=self.data_path,
            index=self.index_path,
            description=self.description,
            shard=shard,
            clip=self.clip,
            sequence_description=self.sequence_description,
            compression_type=self.compression_type)
        )
        if self.shuffle_queue_size:
            it = iterator_utils.shuffle_iterator(it, self.shuffle_queue_size)
        if self.transform:
            it = map(self.transform, it)
        return it


class MultiTFRecordDataset(torch.utils.data.IterableDataset):
    """Parse multiple (generic) TFRecords datasets into an `IterableDataset`
    object, which contain `np.ndarrays`s.

    Params:
    -------
    data_pattern: str
        Input data path pattern.

    index_pattern: str or None
        Input index path pattern.

    splits: dict
        Dictionary of (key, value) pairs, where the key is used to
        construct the data and index path(s) and the value determines
        the contribution of each split to the batch.

    description: list or dict of str, optional, default=None
        List of keys or dict of (key, value) pairs to extract from each
        record. The keys represent the name of the features and the
        values ("byte", "float", or "int") correspond to the data type.
        If dtypes are provided, then they are verified against the
        inferred type for compatibility purposes. If None (default),
        then all features contained in the file are extracted.

    shuffle_queue_size: int, optional, default=None
        Length of buffer. Determines how many records are queued to
        sample from.

    transform : a callable, default = None
        A function that takes in the input `features` i.e the dict
        provided in the description, transforms it and returns a
        desirable output.

    shard: tuple of ints, optional, default=None
        A tuple (index, count) representing worker_id and num_workers
        count. Necessary to evenly split/shard the dataset among many
        workers (i.e. >1).

    sequence_description: list or dict of str, optional, default=None
        Similar to `description`, but refers to the sequence features
        within a `SequenceExample`. When this field is `None`, then it
        is assumed that an `Example` is being read otherwise, a
        `SequenceExample` is read. If an empty list or dictionary is
        passed, then all features contained in the file are extracted.

    compression_type: str, optional, default=None
        The type of compression used for the tfrecord. Choose either
        'gzip' or None.

    infinite: bool, optional, default=True
        Whether the Dataset should be infinite or not
    """

    def __init__(
        self,
        paths: List[str],
        indices: List[str],
        splits: Optional[Dict[str, float]],
        description: Union[List[str], Dict[str, str], None] = None,
        shuffle_queue_size: Optional[int] = None,
        transform: Callable[[dict], Any] = None,
        shard: Optional[Tuple[int, int]] = None,
        clip: Optional[List[int]] = None,
        sequence_description: Union[List[str], Dict[str, str], None] = None,
        compression_type: Optional[str] = None,
        infinite: bool = True
    ) -> None:
        super(MultiTFRecordDataset, self).__init__()
        self.paths = paths
        self.indices = indices
        self.splits = splits
        self.description = description
        self.sequence_description = sequence_description
        self.shuffle_queue_size = shuffle_queue_size
        self.transform = transform
        self.compression_type = compression_type
        self.infinite = infinite
        self.shard = shard
        self.clip = clip
        self.loader = None

    def __iter__(self):
        self.loader = reader.multi_tfrecord_loader(
            paths=self.paths,
            indices=self.indices,
            splits=self.splits,
            description=self.description,
            sequence_description=self.sequence_description,
            compression_type=self.compression_type,
            shard=self.shard,
            clip=self.clip,
            infinite=self.infinite
        )
        it = iter(self.loader)
        if self.shuffle_queue_size:
            it = iterator_utils.shuffle_iterator(it, self.shuffle_queue_size)
        if self.transform:
            it = map(self.transform, it)
        return it

    def close(self):
        if self.loader is not None:
            self.loader.close()
