from typing import Callable, Dict, Tuple


def patient_use_case(repository: Dict[str, Callable]) -> Tuple[Callable]:

    def create(patients: list[str]):
        repository["create"](patients)

    return create,
