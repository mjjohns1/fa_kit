"""
Unit tests for rotation module
"""

import pytest
import numpy as np

from fa_kit import rotation


TEST_DIM = 100


def test_varimax_python():
    """Test varimax rotation python implementation"""

    in_comps = np.eye(TEST_DIM)
    rot = rotation.VarimaxRotatorPython()
    rot_comps = rot.rotate(in_comps)

    assert np.array_equal(
        in_comps.dot(rot_comps.T),
        np.eye(TEST_DIM)
        )


def test_quartimax_python():
    """Test quartimax rotation python implementation"""

    in_comps = np.eye(TEST_DIM)
    rot = rotation.QuartimaxRotatorPython()
    rot_comps = rot.rotate(in_comps)

    assert np.array_equal(
        in_comps.dot(rot_comps.T),
        np.eye(TEST_DIM)
        )


def test_varimax_tf():
    """Test varimax rotation TF implementation"""

    in_comps = np.eye(TEST_DIM)
    rot = rotation.VarimaxRotatorTf()
    rot_comps = rot.rotate(in_comps)

    assert np.array_equal(
        in_comps.dot(rot_comps.T),
        np.eye(TEST_DIM)
        )

def test_quartimax_tf():
    """Test quartimax rotation TF implementation"""

    in_comps = np.eye(TEST_DIM)
    rot = rotation.QuartimaxRotatorTf()
    rot_comps = rot.rotate(in_comps)

    assert np.array_equal(
        in_comps.dot(rot_comps.T),
        np.eye(TEST_DIM)
        )
