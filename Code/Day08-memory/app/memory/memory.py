class Memory:


    def __init__(
        self
    ):
        self.massages= []

    def add(
        self,
        massage : str
    ):
        self.massages.append(massage)

    def get_all(
        self
    ):
        return self.massages
