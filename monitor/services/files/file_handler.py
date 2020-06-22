import zipfile


class FileHandler:
    """Handles generically useful file related operations.
    """

    @staticmethod
    def unzip(path, destination):
        with zipfile.ZipFile(path, 'r') as zipref:
            zipref.extractall(destination)
