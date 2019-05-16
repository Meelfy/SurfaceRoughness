import numpy as np

from surfaceroughness.common.test_case import SurfaceRoughnessTestCase
from surfaceroughness.datahandler import DataLoader


class TestDataloader(SurfaceRoughnessTestCase):
    def test_load_from_file(self):
        dataloader = DataLoader()
        asc_file_path = self.FIXTURES_ROOT / "asc_files" / "asc_file_test_case_1.asc"
        asc_file_path = str(asc_file_path)
        data = dataloader.load_from_file(asc_file_path)
        assert data.shape == (12, 3)
        assert data.dtype == np.float
