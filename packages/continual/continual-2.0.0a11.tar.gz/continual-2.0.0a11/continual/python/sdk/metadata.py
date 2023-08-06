from __future__ import annotations
from typing import List, Optional

from continual.python.sdk.iterators import Pager
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.rpc.management.v1 import (
    management_types_pb2,
    management_pb2,
    types as management_types_py,
)
import json
import numpy as np
import datetime


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
        try:
            x = str(obj)
        except:
            pass
        else:
            return x
        return json.JSONEncoder.default(self, obj)


class MetadataManager(Manager):
    """Manages metadata resources."""

    # the name pattern for metadata depends on the resource it was created for
    name_pattern: str = ""

    def create(
        self,
        key: str,
        data: dict,
        type: str = "MAP",
        group_name: str = "",
    ) -> Metadata:
        """Create metadata.

        Arguments:
            key: A common name used to retrieve the metadata
            data: the metadata
            type: the type of metadata
            group_name: the group the metadata is associated with

        Returns
            Metadata.

        Examples:
            >>> ... # Assume environment `env`is defined
            >>> run = env.runs.create('run0')
            >>> model_version = run.models.create("example-model").model_versions.create()
            >>> model_version.metadata.create(
            ...      key="test_map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ...      type="MAP",
            ...      group_name="test"
            ... )
            <Metadata object {'name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cegkr0i5lsrkc0osu0eg/metadata/cegkr0i5lsrkc0osu0g0',
            'key': 'test_map', 'create_time': '2022-12-20T05:52:02.552140Z', 'update_time': '2022-12-20T05:52:02.552140Z', 'data': '{"key1": "value1", "key2": 10, "key3": 0.5}',
            'group_name': 'test', 'type': 'MAP'}>
        """
        req = management_pb2.CreateMetadataRequest(
            parent=self.parent,
            metadata=management_types_pb2.Metadata(
                key=key,
                data=json.dumps(data, cls=NpEncoder),
                type=type,
                group_name=group_name,
            ),
        )
        resp = self.client._management.CreateMetadata(req)
        return Metadata.from_proto(resp, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        latest: bool = True,
    ) -> List[Metadata]:
        """List metadata.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            latest: If true, the results are sorted in descending order, else ascending.

        Returns:
            A list of metadata.

        Examples:
            >>> ... # Assume environment `env`is defined
            >>> run = env.runs.create('run0')
            >>> model_version = run.models.create("example-model").model_versions.create()
            >>> metadatas = [model_version.metadata.create(key=f'metadata_{i}', data={'key': 'value'}) for i in range(3)]
            >>> [m.key for m in model_version.metadata.list(page_size=3)]
            ['metadata_2', 'metadata_1', 'metadata_0']
            >>> [m.key for m in model_version.metadata.list(page_size=3, latest=False)]
            ['metadata_0', 'metadata_1', 'metadata_2']
        """
        if not self.client:
            print(f"Cannot list metadata without client")
            return

        req = management_pb2.ListMetadataRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            latest=latest,
        )
        resp = self.client._management.ListMetadata(req)
        return [Metadata.from_proto(x, client=self.client) for x in resp.metadata]

    def list_all(self) -> Pager[Metadata]:
        """List all metadata.

        Pages through all metadata using an iterator.

        Returns:
            A iterator of all metadata.

        Examples:
            >>> ... # Assume environment `env`is defined
            >>> run = env.runs.create('run0')
            >>> model_version = run.models.create("example-model").model_versions.create()
            >>> metadatas = [model_version.metadata.create(key=f'metadata_{i}', data={'key': 'value'}) for i in range(3)]
            >>> [m.key for m in model_version.metadata.list_all()]
            ['metadata_0', 'metadata_1', 'metadata_2']
        """

        def next_page(next_page_token):
            req = management_pb2.ListMetadataRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListMetadata(req)
            return (
                [Metadata.from_proto(x, client=self.client) for x in resp.metadata],
                resp.next_page_token,
            )

        return Pager(next_page)

    def get(self, name: str = "", key: str = "", group_name: str = "") -> Metadata:
        """Get metadata.

        Arguments:
            name: The fully qualified name of the metadata obj
            key: A string used to uniquely identify an artifact for a given parent object
            group_name: The group the metadata is associated with

        Return
            Metadata

        Examples:
            >>> ... # Assume environment `env`is defined
            >>> run = env.runs.create('run0')
            >>> model_version = run.models.create("example-model").model_versions.create()
            >>> metadata = model_version.metadata.create(
            ...      key="test_map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ...      type="MAP",
            ...      group_name="test"
            ... )
            >>> model_version.metadata.get(name=metadata.name)      # Get by name
            <Metadata object {'name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cegkr0i5lsrkc0osu0eg/metadata/cegkr0i5lsrkc0osu0g0',
            'key': 'test_map', 'create_time': '2022-12-20T05:52:02.552140Z', 'update_time': '2022-12-20T05:52:02.552140Z', 'data': '{"key1": "value1", "key2": 10, "key3": 0.5}',
            'group_name': 'test', 'type': 'MAP'}>
            >>> model_version.metadata.get(key="test_map")          # Get by key
            <Metadata object {'name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cegkr0i5lsrkc0osu0eg/metadata/cegkr0i5lsrkc0osu0g0',
            'key': 'test_map', 'create_time': '2022-12-20T05:52:02.552140Z', 'update_time': '2022-12-20T05:52:02.552140Z', 'data': '{"key1": "value1", "key2": 10, "key3": 0.5}',
            'group_name': 'test', 'type': 'MAP'}>
        """
        if not self.client:
            print(f"Cannot fetch metadata without client")
            return

        req = management_pb2.GetMetadataRequest(
            parent=self.parent, name=name, key=key, group_name=group_name
        )
        res = self.client._management.GetMetadata(req)
        return Metadata.from_proto(res, client=self.client)

    def delete(self, name: str):
        """Delete metadata.

        Arguments:
            name: The fully qualified name of the metadata obj

        Examples:
            >>> ... # Assume environment `env`is defined
            >>> run = env.runs.create('run0')
            >>> model_version = run.models.create("example-model").model_versions.create()
            >>> metadata = model_version.metadata.create(
            ...      key="test_map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ...      type="MAP",
            ...      group_name="test"
            ... )
            >>> len(list(model_version.metadata.list_all()))
            1
            >>> model_version.metadata.delete(name=metadata.name)
            >>> len(list(model_version.metadata.list_all()))
            0
        """
        if not self.client:
            print(f"Cannot delete metadata without client")
            return

        req = management_pb2.DeleteMetadataRequest(name=name)
        self.client._management.DeleteMetadata(req)


class Metadata(Resource, management_types_py.Metadata):
    """Metadata resource."""

    # the name pattern for metadata depends on the resource it was created for
    name_pattern: str = ""

    _manager: MetadataManager
    """Metadata manager."""

    def _init(self):
        self._manager = MetadataManager(parent=self.parent, client=self.client)
