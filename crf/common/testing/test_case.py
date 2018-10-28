# ==============================================================================
#
#  Copyright (c) 2018 AllenAI
#
#  Apache License
#  Version 2.0, January 2004
#  http://www.apache.org/licenses/
#
# ==============================================================================


# pylint: disable=invalid-name,protected-access
import logging
import os
import pathlib
import shutil
import tempfile
from unittest import TestCase

from crf.common.checks import log_pytorch_version_info

TEST_DIR = tempfile.mkdtemp(prefix="crf_tests")

class NlpTestCase(TestCase):  # pylint: disable=too-many-public-methods
    """
    A custom subclass of :class:`~unittest.TestCase` that disables some of the
    more verbose AllenNLP logging and that creates and destroys a temp directory
    as a test fixture.
    """
    PROJECT_ROOT = (pathlib.Path(__file__).parent / ".." / ".." / "..").resolve()  # pylint: disable=no-member
    MODULE_ROOT = PROJECT_ROOT / "crf"
    TESTS_ROOT = PROJECT_ROOT / "tests"

    def setUp(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                            level=logging.DEBUG)
        # Disabling some of the more verbose logging statements that typically aren't very helpful
        # in tests.
        logging.getLogger('crf.common.params').disabled = True
        logging.getLogger('crf.nn.initializers').disabled = True
        logging.getLogger('crf.modules.token_embedders.embedding').setLevel(logging.INFO)
        logging.getLogger('urllib3.connectionpool').disabled = True
        log_pytorch_version_info()

        self.TEST_DIR = pathlib.Path(TEST_DIR)

        os.makedirs(self.TEST_DIR, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.TEST_DIR)
