import numpy as np

from surfaceroughness.common.test_case import SurfaceRoughnessTestCase
from surfaceroughness.datahandler import DataLoader


class TestDataloader(SurfaceRoughnessTestCase):
    def test_load_from_file(self):
        asc_file_path = self.FIXTURES_ROOT / "asc_files" / "asc_file_test_case_1.asc"
        asc_file_path = str(asc_file_path)

        data_loader = DataLoader()
        data = data_loader.load_from_file(asc_file_path)
        assert data.shape == (12, 3)
        assert data.dtype == np.float

    def test_load_data(self):
        asc_file_path = self.FIXTURES_ROOT / "asc_files" / "asc_file_test_case_1.asc"
        asc_file_path = str(asc_file_path)

        data_loader = DataLoader()
        data = data_loader.load_data(asc_file_path, sampling_ratio=0.5)
        assert data.shape == (6, 3)
        assert data.dtype == np.float

        # IMPORTANT: the data_loader.sampling_ratio = 0.5, so the max_point_number = min(5, 6) = 5
        data = data_loader.load_data(asc_file_path, max_point_number=5)
        assert data.shape == (5, 3)
        assert data.dtype == np.float
