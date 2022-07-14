from typing import List, Union

import numpy as np


class GetClusteringCost:
    def __init__(self, cost_matrix: List[List[Union[float, int]]], cluster_list: List):
        self.cost_matrix = cost_matrix
        self.cluster_list = cluster_list
        self.dimension = len(cost_matrix)
        self.num_class = len(set(self.cluster_list))
        self.cost = self.__get_cost__()

    def __get_cost__(self) -> float:
        # N = self.adjacency_matrix.shape[0]
        _cluster_matrix = np.zeros((self.dimension, self.num_class))

        for node, clstr in enumerate(self.cluster_list):
            _cluster_matrix[node, clstr] = 1

        actual_cost = float(
            np.sum(
                np.diagonal(
                    np.matmul(
                        np.matmul(_cluster_matrix.T, self.cost_matrix),
                        _cluster_matrix,
                    )
                )
            )
        )

        return actual_cost
