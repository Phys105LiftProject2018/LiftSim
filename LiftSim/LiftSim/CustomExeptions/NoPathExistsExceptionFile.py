class NoPathExistsException(Exception):
    def __init__(self, path):
        self.message = "The path \"" + path + "\" dosen't exist. Check that the path is valid. Don't use a path with spaces where possible."