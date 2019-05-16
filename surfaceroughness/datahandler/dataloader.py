import logging
import random

import numpy as np

logger = logging.getLogger(__name__)


class DataLoader(object):
    """
    This class is loading data from 3D scanner and convert to a numpy object. The accepted file format is: [asc]
    """

    def __init__(self):
        self.max_point_number = -1
        self.sampling_ratio = 1.0
        self.should_shuffle = False

    def load_data(self, data_path, max_point_number: int = None, sampling_ratio: float = None):
        if sampling_ratio is not None:
            # If the sampling ratio is set, the data will be shuffled
            self.should_shuffle = True
            self.sampling_ratio = sampling_ratio
        if max_point_number is not None:
            self.max_point_number = max_point_number
        return self.load_from_file(data_path)

    def load_from_file(self, datafile_path: str, filetype: str = 'asc'):
        """
        This function will skip first and end line of the asc file
        :param datafile_path:
        :param filetype:
        :return:
        """
        assert datafile_path.endswith(filetype), f"except a filetype of {filetype} but get {datafile_path}"
        logger.info(f"load 3d points data from {datafile_path}")
        if filetype == "asc":
            points_3d = []
            with open(datafile_path, encoding="utf-8") as f_in:
                # remove file and end line which is useless
                file_data = f_in.readlines()[1:-1]
                # get samples number limit
                if self.max_point_number == -1:
                    self.max_point_number = len(file_data)
                self.max_point_number = min(self.max_point_number, int(self.sampling_ratio * len(file_data)))
                print(self.sampling_ratio * len(file_data))

                if self.should_shuffle:
                    random.shuffle(file_data)

                for idx, line in enumerate(file_data):
                    points_3d.append([float(e) for e in line.split()])
                    if len(points_3d) >= self.max_point_number:
                        # reach the max sample limitation
                        break
            points_3d = np.array(points_3d)
        else:
            points_3d = None
            logging.error("filetype is not supported")
            assert f"unsupported filetype {filetype}"
        return points_3d
