import datetime
import pathlib
from typing import List, Dict, Union, Optional, Tuple


class PyVcsID:
    ...


class PyRemoteRepository:
    def __init__(self, resource: str, repository: str, owner: str) -> None:
        ...

class PyVcsInfo:
    def __init__(self, sha: str, remote: Optional[PyRemoteRepository]) -> None:
        ...

    def id(self) -> PyVcsID:
        ...


class PyRunID:
    def __init__(self, endpoint: ArtefactEndpoint) -> None:
        ...

    @staticmethod
    def from_existing(uuid_str: str) -> PyRunID:
        ...


class PyMetricFilter:
    def __init__(self, name: str, value: float, ordering: str) -> None:
        ...

    def or_(self, metric: PyMetricFilter) -> PyMetricFilter:
        ...

    def and_(self, metric: PyMetricFilter) -> PyMetricFilter:
        ...


class LocalArtefactRegistry:
    path: Optional[pathlib.Path]

    def __init__(self, path: Optional[pathlib.Path]) -> None:
        self.path = path


class LocalEndpoint:
    def __init__(self, registry_endpoint: LocalArtefactRegistry, storage_location: Optional[pathlib.Path]) -> None:
        ...


class ShareableAIEndpoint:
    def __init__(self, api_key: str) -> None:
        ...


ArtefactEndpoint = Union[LocalEndpoint, ShareableAIEndpoint]


class PyID:
    """
    Artefact or Artefact Set ID - readable in Python
    """

    def as_string(self) -> str: ...

    def as_hex_string(self) -> str: ...


class PyModelRun:
    def __init__(self, endpoint: ArtefactEndpoint, run_id: PyRunID, model_uuid: str, model_name: str,
                 vcs: PyVcsInfo) -> None:
        ...

    def save_metrics(self, endpoint: ArtefactEndpoint, metrics: List[Tuple[datetime.datetime, str, float]]):
        ...


class PyModelUUID:
    """
        Identifier for a Python Model class - used to distinguish classes with the same
        name during the same run.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def from_existing(uuid_str: str) -> PyModelUUID: ...


class PyModelID:
    name: str
    vcs_id: PyVcsID
    artefact_schema_id: PyID

    def __init__(self, name: str, vcs_hash: str, artefact_set_id: PyID) -> None: ...


class PyArtefact:
    """
    Data Backing for a Python-Compatible Artefact
    """

    def id(self) -> PyID:
        ...

    def path(self, temp_dir: pathlib.Path) -> pathlib.Path: ...

    """
       Retrieve or create a local path containing the Model Artefact
    """


class ModelData:
    """
    Model Data Representation for Save/Load
    """

    def __init__(
            self,
            name: str,
            vcs_info: PyVcsInfo,
            local_artefacts: List[LocalArtefactPath],
            children: Dict[str, PyModelID],
    ):
        """Create a Model Data Representation
        Args:
            name: Model Name
            vcs_hash: The Version Control System hash for the file
            local_artefacts: Paths for artefacts on the local system
            remote_artefacts: Paths for artefacts on remote systems
            children: Model IDs for Model Children
        """
        ...

    def dumps(
            self, endpoint: ArtefactEndpoint, model_run_id: Optional[PyModelUUID, PyRunID]
    ) -> PyModelID: ...

    @property
    def model_id(self) -> PyModelID: ...

    @property
    def child_ids(self) -> dict[str, PyModelID]: ...

    def artefact_by_slot(self, slot: str) -> PyArtefact: ...

    def child_id_by_slot(self, slot: str) -> PyModelID: ...


class LocalArtefactPath:
    """
    Local Artefact - referenced by absolute path
    """

    def __init__(self, slot: str, path: str) -> None: ...



def load_model_data(
        model_name: str,
        vcs_id: PyVcsID,
        artefact_schema_id: PyID,
        endpoint: ArtefactEndpoint
) -> ModelData:
    """
    Load Model Data from Model Identifiers

    Requests the Model Data from the remote SQL server, and the Artefact Data from the remote Storage server.

    The model info and artefact data is copied to the local sql server and storage server respectively,
    and then artefacts are provided to the caller. The artefacts are presented with the OnDisk data backing,
    giving the most flexibility in terms of use. It is entirely possible to instead present Remote links to the
    end user, but this means consuming a stream each time the data must be checked, and assuming that the remote
    connection remains valid after the object is returned, which cannot be guaranteed.

    :param vcs_id: Version Control Information ID
    :param model_name: Name of the Model
    :param artefact_schema_id: ID representing the saved Artefacts and their layout in the model
    :param endpoint: Connection Options

    """
    ...


def search_for_models(
        endpoint: ArtefactEndpoint,
        names: List[str],
        runs: List[PyRunID],
        metric_filter: Optional[PyMetricFilter],
        vcs_id: List[PyVcsID],
) -> List[PyModelID]:
    ...


def search_for_vcs_id(
        endpoint: ArtefactEndpoint,
        repository_name: str
) -> List[PyVcsID]:
    ...
