'''
Todo: Enthält die Klasse Todo, diese enthält alle nötigen Attribute.
'''

class Todo:
    """Object for TODO-Items"""
    todo_id: int = -1 # todo_id is set by the Database
    title: str = None
    content: str = None
    is_done: bool = False

    # Constructor
    def __init__(self, title: str, content: str, is_done: bool, todo_id: int = -1):
        self.todo_id = todo_id
        self.title = title
        self.content = content
        self.is_done = is_done

#    def __init__(self, title: str, content: str, is_done: bool):
#        self.title = title
#        self.content = content
#        self.is_done = is_done

    def __str__(self):
        return str(self.todo_id) + "\n" + self.title + "\n" + self.content + "\nDone: " + str(self.is_done)
