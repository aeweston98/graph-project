from abc import abstractmethod, ABC

class EdgeInterface(ABC):
    @abstractmethod
    def GetID(self) -> str:
        pass
    
    @abstractmethod
    def GetBaggage(self, key: str) -> str:
        pass

    @abstractmethod
    def SetBaggage(self, key, value: str):
        pass

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
    def GetAdjacent(self) -> set:
        pass

class GraphInterface(ABC):
    @abstractmethod
    def GetRandomNode(self) -> NodeInterface:
        pass

    @abstractmethod
    def GetNode(self, id: str) -> NodeInterface:
        pass
