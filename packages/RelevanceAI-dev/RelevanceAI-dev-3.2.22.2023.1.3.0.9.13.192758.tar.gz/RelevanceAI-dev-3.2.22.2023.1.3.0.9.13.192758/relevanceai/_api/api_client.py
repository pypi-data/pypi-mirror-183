# -*- coding: utf-8 -*-
"""Batch client to allow for batch insertions/retrieval and encoding
"""
from typing import Callable

from relevanceai._api.batch.insert import BatchInsertClient


class APIClient(BatchInsertClient):
    """Batch API client"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def batch_insert(self):
        raise NotImplemented

    def batch_get_and_edit(self, dataset_id: str, chunk_size: int, bulk_edit: Callable):
        """Batch get the documents and return the documents"""
        raise NotImplemented

    # Other useful utilities
    def append_metadata_list(
        self,
        field: str,
        value_to_append,
        only_unique: bool = False,
        verbose: bool = True,
    ):
        """
        Easily append to a list value in metadata using this function.
        This prevents overwriting if there is one.
        """
        metadata = self.datasets.metadata(self.dataset_id)["results"]
        if self.is_field(field, metadata):
            value_list = self.get_field(field, metadata)
        else:
            value_list = []

        if not isinstance(value_list, list):
            raise ValueError("Can't append to object that is not a list.")

        # Used for not including multiple entries when subclustering
        if only_unique:
            for v in value_list:
                if v == value_to_append:
                    return

        value_list.append(value_to_append)
        self.set_field(field, metadata, value_list)
        self.datasets.post_metadata(
            dataset_id=self.dataset_id,
            metadata=metadata,
        )
