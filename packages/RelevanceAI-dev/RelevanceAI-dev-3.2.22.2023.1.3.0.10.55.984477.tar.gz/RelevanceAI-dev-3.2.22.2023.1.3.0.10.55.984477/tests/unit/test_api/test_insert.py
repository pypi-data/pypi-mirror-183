"""Testing code for batch inserting
"""
import pytest

from typing import Dict, List

from relevanceai import Client

from relevanceai.dataset import Dataset

from tests.globals.constants import generate_dataset_id

from tests.unit.test_api.helpers import *


class TestInsert:
    test_dataset_id = generate_dataset_id()

    def test_batch_insert(
        self,
        test_dataset: Dataset,
        vector_documents: List[Dict],
    ):
        results = test_dataset.insert_documents(vector_documents)
        assert len(results["failed_documents"]) == 0

    def test_assorted_nested_upload(
        self,
        test_dataset: Dataset,
        assorted_nested_documents: List[Dict],
    ):
        results = test_dataset.insert_documents(assorted_nested_documents)
        assert len(results["failed_documents"]) == 0


class TestInsertImages:
    def setup(self):
        from pathlib import Path
        from uuid import uuid4

        self.filename = "lovelace.jpg"

        self.directory = Path(str(uuid4()))
        self.directory.mkdir()
        with open(self.filename, "wb") as f:
            f.write(b"ghuewiogahweuaioghweqrofleuwaiolfheaswufg9oeawhfgaeuw")

    @pytest.mark.skip(reason="need to fix image folder")
    def test_insert_media_folder(self, test_client: Client):
        self.ds = test_client.Dataset(generate_dataset_id())
        results = self.ds.insert_media_folder(
            field="images",
            path=self.directory,
            recurse=False,  # No subdirectories exist anyway
        )
        assert results is None

    def teardown(self):
        self.ds.delete()

        try:
            import os

            os.remove(self.directory / self.filename)
        except FileNotFoundError:
            pass

        self.directory.rmdir()
