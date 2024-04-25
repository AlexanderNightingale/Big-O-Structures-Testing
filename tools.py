import timeit
import logging
import structures
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Timer:
    def __init__(self):
        self.start_time = 0.0
        self.stop_time = 0.0

    def start(self):
        self.start_time = timeit.default_timer()

    def stop(self):
        self.stop_time = timeit.default_timer()

    def get_time(self) -> float:
        return self.stop_time - self.start_time

class Unit_Test:
    def __init__(self,structure: structures):
        pass

    def test_access(self):
        pass

    def test_search(self):
        pass

    def test_insertion(self):
        pass

    def test_deleting(self):
        pass

class Storage:
    STORAGE_PATH = "storage/storage.json"

    def __init__(self):
        self._init_storage_file()

    def _init_storage_file(self):
        if not os.path.isdir("storage"):
            os.mkdir("storage")
            logger.info("Storge folder created")

        if not os.path.isfile(self.STORAGE_PATH):
            with open(self.STORAGE_PATH, "w"):
                logger.info("Storge file created")
