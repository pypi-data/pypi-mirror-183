class SavedFile:
     def __init__(self, 
                file = None,
                status = None,
                message = None,
                target = None) -> None:

        self.file = file
        self.status = status
        self.message = message
        self.target = target