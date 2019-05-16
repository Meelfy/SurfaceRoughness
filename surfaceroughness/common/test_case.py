import logging
from pathlib import Path
from unittest import TestCase


class SurfaceRoughnessTestCase(TestCase):
    """
    A custom subclass of :class:`~unittest.TestCase` that disables some of the
    more verbose logging and that creates and destroys a temp directory
    as a test fixture.
    """
    PROJECT_ROOT = Path(__file__).parents[2].resolve()
    MODULE_ROOT = PROJECT_ROOT / "surfaceroughness"
    TESTS_ROOT = MODULE_ROOT / "tests"
    FIXTURES_ROOT = TESTS_ROOT / "fixtures"

    def setUp(self):
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s',
            level=logging.DEBUG,
            handlers=[
                logging.FileHandler(self.PROJECT_ROOT / "log" / "unit_test.log", encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
