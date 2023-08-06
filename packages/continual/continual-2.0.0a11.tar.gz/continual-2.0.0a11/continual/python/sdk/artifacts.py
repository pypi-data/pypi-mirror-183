from __future__ import annotations
from typing import List, Optional, Tuple
import os
import io
import json
import requests
import tarfile
import mimetypes
from google.resumable_media import DataCorruption
from google.resumable_media.requests import ResumableUpload

from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.rpc.management.v1 import management_pb2, types

CHUNK_SIZE = 117440512  # 112 MB in bytes, chosen arbitrarily


class ArtifactsManager(Manager):
    """Manages artifact resources."""

    # the name pattern for artifacts depends on the resource it was created for
    name_pattern: str = ""

    def create(
        self,
        key: str,
        path: str = "",
        external: bool = False,
        type: str = "",
        url: str = None,
        metadata: dict = None,
        upload: bool = True,
    ) -> Artifact:
        """Create artifact.

        Arguments:
            key: A string to uniquely identify and artifact for a given parent.
            path: Path to the artifact in the local filesystem if not external.
            external: True if this artifact will be stored in a Continual google bucket, false if it is remote.
            type: A label for the type of artifact.
            url: URL for the artifact. Is a signed URL to a google bucket if artifact is not external,
                 optional user-provided URL if it is an external artifact.
            metadata: Key value pairs associated with this artifact.
            upload: Whether to upload the artifact specified in `path`. Only valid if external=False.

        Returns:
            An Artifact

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> with open("test.txt", "w") as f:
            ...     f.write("test content")
            >>> dataset_version.artifacts.create(
            ...     key="test_artifact_internal",
            ...     path=os.path.join(os.getcwd(), "test.txt"),
            ...     external=False,
            ...     type="txt",
            ...     metadata={"key": "value"},
            ...     upload=True
            ... )
            <Artifact object {'name': 'projects/continual_test_proj...", 'external': True ...}>
            >>> dataset_version.artifacts.create(
            ...     key="test_artifact_external",
            ...     external=True,
            ...     type="txt",
            ...     url="http://test-url"
            ... )
            <Artifact object {'name': 'projects/continual_test_proj...", 'external': False ...}>
        """
        if external or not upload:
            req = management_pb2.CreateArtifactRequest(
                parent=self.parent,
                artifact=Artifact(
                    key=key,
                    path=path,
                    type=type,
                    external=True,
                    url=url,
                    metadata=metadata,
                    run_name=self.run_name,
                ).to_proto(),
            )
            res = self.client._management.CreateArtifact(req)
            return Artifact.from_proto(res, client=self.client)

        elif upload:
            artifact_name = ""
            try:
                file_to_upload = path
                if os.path.isdir(path):
                    tarfile_name = os.path.basename(path) + ".tar.gz"
                    with tarfile.open(tarfile_name, "w:gz") as tar:
                        tar.add(
                            path,
                            recursive=True,
                            arcname=os.path.basename(tarfile_name).split(".")[0],
                        )
                    file_to_upload = tarfile_name

                mime_type, _ = mimetypes.guess_type(file_to_upload)

                payload = ""
                with open(file_to_upload, "rb") as f:
                    payload = f.read()

                total_bytes = len(payload)
                exceeds_chunk_size = total_bytes >= CHUNK_SIZE

                req = management_pb2.GenerateArtifactUploadURLRequest(
                    resource=self.parent,
                    key=key,
                    path=path,
                    type=type,
                    mime_type=mime_type or "",
                    metadata=json.dumps(metadata or dict()),
                    resumable=exceeds_chunk_size,
                    run_name=self.run_name,
                )
                res = self.client._management.GenerateArtifactUploadURL(req)

                upload_url = res.url
                artifact_name = res.artifact.name

                headers = dict()
                if mime_type:
                    headers["Content-Type"] = mime_type

                if exceeds_chunk_size:
                    transport = requests.Session()

                    stream = io.BytesIO(payload)

                    upload = ResumableUpload(upload_url, CHUNK_SIZE)
                    upload._resumable_url = upload_url
                    upload._total_bytes = total_bytes
                    upload._stream = stream

                    while not upload.finished:
                        try:
                            print("Writing chunk ... ")
                            response = upload.transmit_next_chunk(transport, timeout=60)
                            print(f"Chunk response: {response}")
                        except DataCorruption:
                            raise
                else:
                    upload_res = requests.put(
                        upload_url, data=payload, headers={"Content-Type": mime_type}
                    )
                    upload_res.raise_for_status()

                return Artifact.from_proto(res.artifact, client=self.client)
            except:
                if artifact_name:
                    req = management_pb2.DeleteArtifactRequest(name=artifact_name)
                    res = self.client._management.DeleteArtifact(req)
                raise

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        latest: bool = True,
    ) -> List[Artifact]:
        """List artifacts.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list of artifacts.
            latest: If true, the results are sorted in descending order, else ascending.

        Returns:
            A list of artifacts.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(key=f"test_artifact_{i}", path="example_path/test.txt") for i in range(5)]
            >>> [a.key for a in dataset_version.artifacts.list(page_size=2)]
            ['test_artifact_4', 'test_artifact_3']
            >>> [a.key for a in dataset_version.artifacts.list(page_size=2, latest=False)]
            ['test_artifact_0', 'test_artifact_1']
        """
        req = management_pb2.ListArtifactsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            latest=latest,
        )
        resp = self.client._management.ListArtifacts(req)
        return [Artifact.from_proto(x, client=self.client) for x in resp.artifacts]

    def get(self, name: str = "", key: str = "") -> Artifact:
        """Get artifact.

        Arguments:
            name: The fully qualified name of the artifact
            key: A string used to identify an artifact for a given parent

        Returns:
            An artifact.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(key=f"test_artifact_{i}", path="example_path/test.txt") for i in range(5)]
            >>> dataset_version.artifacts.get(key="test_artifact_0")
            <Artifact object {'name': 'projects/continual_test_proj...", 'key': 'tes_artifact_0', 'external': False ...}>
        """
        if not self.client:
            print(f"Cannot fetch artifact without client")
            return

        req = management_pb2.GetArtifactRequest(parent=self.parent, name=name, key=key)
        res = self.client._management.GetArtifact(req)
        return Artifact.from_proto(res, client=self.client)

    def delete(self, name: str):
        """Delete artifact.

        Arguments:
            name: The fully qualified name of the artifact

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(key=f"test_artifact_{i}", path="example_path/test.txt") for i in range(5)]
            >>> [dataset_version.artifacts.delete(a.name) for a in dataset_version.artifacts.list(page_size=5)]
            [None, None, None, None, None]
            >>> len(dataset_version.artifacts.list(page_size=5))
            0
        """
        if not self.client:
            print(f"Cannot delete artifact without client")
            return

        req = management_pb2.DeleteArtifactRequest(name=name)
        self.client._management.DeleteArtifact(req)

    def download(
        self,
        id: str,
        download_dir: str = "./artifacts",
    ) -> Tuple[Artifact, str]:
        """Download artifact.

        Arguments:
            id: The name or id of the artifact
            download_dir: The directory to which to download the artifact

        Returns:
            A tuple of the Artifact object and the path where it was downloaded.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> with open("test.txt", "w") as f:
            ...     f.write("test content")
            >>> artifact = dataset_version.artifacts.create(
            ...     key="test_artifact_internal",
            ...     path=os.path.join(os.getcwd(), "test.txt"),
            ...     external=False,
            ...     type="txt",
            ...     metadata={"key": "value"},
            ...     upload=True
            ... )
            >>> artifact, dest_path = dataset_version.artifacts.download(id=artifact.id) # Download the artifact
            >>> with open(dest_path, "r") as f:
            ...     print(f.read())
            "test content"
        """

        artifact = self.get(id)
        downloaded_to = ""
        if not artifact.url:
            raise ValueError(
                f"Artifact cannot be downloaded - no URL was found: {artifact.url}"
            )
        elif artifact.external:
            raise ValueError(f"Cannot download an external artifact - {artifact.url}")

        try:
            res = requests.get(artifact.url, stream=True)
            with tarfile.open(fileobj=res.raw, mode="r") as f:
                f.extractall(download_dir)

            root_dir = os.path.basename(artifact.path or "").split(".")[0]
            downloaded_to = os.path.join(download_dir, root_dir)
        except:
            res = requests.get(artifact.url)
            downloaded_to = os.path.join(
                download_dir,
                os.path.basename(artifact.path or artifact.name.split("/")[-1]),
            )
            with open(downloaded_to, "wb") as f:
                f.write(res.content)
        return artifact, downloaded_to


class Artifact(Resource, types.Artifact):
    """Artifact resource."""

    # the name pattern for artifacts depends on the resource it was created for
    name_pattern: str = ""

    _manager: ArtifactsManager
    """Artifact manager."""

    def _init(self):
        self._manager = ArtifactsManager(parent=self.parent, client=self.client)

    def download(self, dest_dir: str = "./artifacts") -> Tuple[Artifact, str]:
        """Download artifact.

        Arguments:
            dest_dir: The directory to which to download the artifact

        Returns:
            A tuple of the Artifact object and the path where it was downloaded.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> with open("test.txt", "w") as f:
            ...     f.write("test content")
            >>> artifact = dataset_version.artifacts.create(
            ...     key="test_artifact_internal",
            ...     path=os.path.join(os.getcwd(), "test.txt"),
            ...     external=False,
            ...     type="txt",
            ...     metadata={"key": "value"},
            ...     upload=True
            ... )
            >>> artifact, dest_path = artifact.download() # Download the artifact
            >>> with open(dest_path, "r") as f:
            ...     print(f.read())
            "test content"
        """
        # Create if the default doesnt exist
        if dest_dir == "./artifacts":
            dest_dir = os.path.join(os.getcwd(), "artifacts")
            os.makedirs(dest_dir, exist_ok=True)
        return self._manager.download(id=self.name, download_dir=dest_dir)

    def delete(self):
        """Delete artifact.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(key=f"test_artifact_{i}", path="example_path/test.txt") for i in range(5)]
            >>> [a.delete() for a in dataset_version.artifacts.list(page_size=5)]
            [None, None, None, None, None]
            >>> len(dataset_version.artifacts.list(page_size=5))
            0
        """
        self._manager.delete(name=self.name)
