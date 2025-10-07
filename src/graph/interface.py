from abc import abstractmethod, ABC
from typing import set

class NodeInterface(ABC):
    @abstractmethod
    def GetID(self) -> str:
        pass

    @abstractmethod
    def GetBaggage(self, key: str) -> str:
        pass

    @abstractmethod
    def SetBaggage(self, key, value: str):
        pass

    @abstractmethod
    def GetAdjacent(self) -> Set[NodeInterface]:
        pass

    @abstractmethod
    def AddAdjacent(self, adj: NodeInterface):
        pass

class GraphInterface(ABC):
    @abstractmethod
    def GetRandomNode(self) -> NodeInterface:
        pass

    @abstractmethod
    def GetNode(self, id: str) -> NodeInterface:
        pass
