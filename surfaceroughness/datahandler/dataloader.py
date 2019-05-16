import numpy as np


class DataLoader(object):
    """
    This class is loading data from 3D scanner and convert to a numpy object. The accepted file format is: [asc]
    """

    def __init__(self):
        self.data = None

    @staticmethod
    def load_from_file(datafile_path: str, filetype: str = 'asc'):
        """
        This function will skip first and end line of the asc file
        :param datafile_path:
        :param filetype:
        :return:
        """
        assert datafile_path.endswith(filetype), f"except a filetype of {filetype} but get {datafile_path}"
        if filetype == "asc":
            points_3d = []
            with open(datafile_path, encoding="utf-8") as f_in:
                file_data = f_in.readlines()
                for idx, line in enumerate(file_data):
                    if idx == 0 or idx == len(file_data) - 1:
                        continue
                    points_3d.append([float(e) for e in line.split()])
            points_3d = np.array(points_3d)
        else:
            points_3d = None
            assert f"unsupported filetype {filetype}"
        return points_3d

    def load_data(self, data_path):
        return self.load_from_file(data_path)
