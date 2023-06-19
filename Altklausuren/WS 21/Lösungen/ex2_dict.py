from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

## Aufgabe 2 (Dict) ############################################################

def cluster_by_points(result: dict) -> dict:
    cluster = dict()
    for name, points in result.items():
        cluster_val = (points//10)*10
        if cluster_val in cluster:
            cluster[cluster_val] += [name]
        else:
            cluster[cluster_val] = [name]
    return cluster
