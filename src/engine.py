import typing

class RandomEngine():

    def __init__(self):
        pass

    def get_random(self, amount: int) -> typing.List[int]:
        assert amount > 0
        return [10 for _ in range(amount)] 
