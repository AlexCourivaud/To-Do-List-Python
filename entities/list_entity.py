class ListEntity:
    def __init__(self, id=None, title=None, mark_as_done=None):
        self.id = id
        self.title = title
        self.mark_as_done = mark_as_done

    def __str__(self):
        return f"ListEntity(id={self.id}, title={self.title}, mark_as_done={self.mark_as_done})"