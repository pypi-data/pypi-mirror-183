from abc import abstractmethod, ABC
from typing import List, Dict, Any


class RecommendationInterface(ABC):
    @abstractmethod
    def recommendation(self) -> List[Dict[str, List[Dict[str, Any]]]]:
        """Fetch recommendation based on total records
        :return: list of dictionary
        """
        raise NotImplementedError
