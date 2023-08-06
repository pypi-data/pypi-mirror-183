from abc import ABC, abstractmethod
from typing import List

from graphdb.schema import Node


class NodeDeleteInterface(ABC):
    """Base class for basic operation delete node"""

    @abstractmethod
    def remove_all_node_property(self, node: Node) -> Node:
        """Remove all property from this node
        :param node: object node
        :return: object node
        """
        raise NotImplementedError

    @abstractmethod
    def remove_node_property(self, node: Node, properties: List[str]) -> Node:
        """Remove specified property from node
        :param node: object node
        :param properties: list of property you want to remove from this node
        :return: object node
        """
        raise NotImplementedError

    @abstractmethod
    def delete_node_with_relationship(self, node: Node) -> Node:
        """Delete for specified node object, please note this will remove node with all relationship on it
        :param node: object node that we want to delete
        :return: object node
        """
        raise NotImplementedError

    @abstractmethod
    def delete_node(self, node: Node) -> Node:
        """Delete for specified node object, it will leave relationship as it is
        :param node: object node that we want to delete
        :return: object node
        """
        raise NotImplementedError
