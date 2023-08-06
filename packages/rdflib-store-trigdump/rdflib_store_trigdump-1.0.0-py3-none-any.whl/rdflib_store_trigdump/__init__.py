import inspect
import logging
from pathlib import Path
from typing import Optional, TYPE_CHECKING, Union

from rdflib import Graph
from rdflib.plugins.stores.memory import Memory
from rdflib.store import NO_STORE, VALID_STORE

if TYPE_CHECKING:
    from rdflib.term import Identifier

__all__ = ["TriGDumpStore"]

logger = logging.getLogger(__name__)


def _find_graph_in_stack() -> Optional[Graph]:
    for finfo in inspect.stack()[2:]:
        obj = finfo.frame.f_locals.get("self", None)
        if isinstance(obj, Graph):
            return obj

    return None


class TriGDumpStore(Memory):
    """A thin caching wrapper around the default Memory store.

    This store implementation extends RDFLib's Memory store to dump and load
    data in a TriG file during uses.
    """

    def __init__(
        self, configuration: Optional[str] = None, identifier: Optional["Identifier"] = None
    ):
        self._graph = None
        self._path = None

        super().__init__(configuration, identifier)

    def open(self, configuration: Union[Path, str], create=False) -> int:
        self._path = Path(configuration)

        self._graph = _find_graph_in_stack()
        if self._graph is None:
            raise RuntimeError("open() must be called through Graph.open()")

        if create:
            logger.info("Creating parent directories and file %s", str(self._path))
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._path.touch(exist_ok=True)

        if not self._path.exists():
            return NO_STORE

        logger.info("Reading graph data from %s", str(self._path))
        self._graph.parse(self._path, format="trig")

        return VALID_STORE

    def close(self, commit_pending_transaction: Optional[bool] = None) -> None:
        if self._path is None:
            logger.warning("Tried to close an undefined TriG dump store")
            return

        logger.info("Writing graph data to %s", str(self._path))
        self._graph.serialize(self._path, format="trig")

        self._graph = None
        self._path = None

    def destroy(self, configuration: Union[Path, str]) -> None:
        path = Path(str)

        logger.info("Deleting file %s", str(path))
        path.unlink(missing_ok=True)

        self._graph = None
        self._path = None
