class Node:
    def __init__(self, value):
        self._data: any = value
        self._next: Node | None = None

    def get_data(self) -> any:
        return self._data

    def get_next(self) -> "Node | None":
        return self._next

    def set_data(self, new_value: any) -> None:
        self._data = new_value

    def set_next(self, updated_next: "Node") -> None:
        self._next = updated_next

    def __str__(self) -> str:
        return f"Node [{str(self.get_data())}]"
