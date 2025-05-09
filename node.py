class Node:
    def __init__(self, value):
        self._data = value
        self._next = None
        
    def get_data(self):
        return self._data
    
    def get_next(self):
        return self._next
    
    def set_data(self, new_value):
        self._data = new_value
        
    def set_next(self, updated_next):
        self._next = updated_next
        
    def __str__(self):
        return f"Node [{str(self.get_data())}]"
