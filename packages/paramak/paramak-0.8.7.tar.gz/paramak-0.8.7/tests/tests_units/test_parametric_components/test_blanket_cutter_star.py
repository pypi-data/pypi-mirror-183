import unittest

import pytest

import paramak


class TestBlanketCutterStar(unittest.TestCase):
    def setUp(self):
        self.test_shape = paramak.BlanketCutterStar(distance=100)

    def test_default_parameters(self):
        """Checks that the default parameters of a BlanketCutterStar are correct."""

        assert self.test_shape.azimuth_placement_angle == [
            0.0,
            36.0,
            72.0,
            108.0,
            144.0,
            180.0,
            216.0,
            252.0,
            288.0,
            324.0,
        ]
        assert self.test_shape.height == 2000
        assert self.test_shape.width == 2000
        assert self.test_shape.name == "blanket_cutter_star"

    def test_points_calculation(self):
        """Checks that the points used to construct the BlanketCutterStar component
        are calculated correctly from the parameters given."""

        assert self.test_shape.points == [
            (0, -1000),
            (2000, -1000),
            (2000, 1000),
            (0, 1000),
        ]

    def test_processed_points_calculation(self):
        """Checks that the points used to construct the BlanketCutterStar component
        are calculated correctly from the parameters given."""

        assert self.test_shape.processed_points == [
            (0, -1000, "straight"),
            (2000, -1000, "straight"),
            (2000, 1000, "straight"),
            (0, 1000, "straight"),
            (0, -1000, "straight"),
        ]

    def test_creation(self):
        """Creates a solid using the BlanketCutterStar parametric component
        and checks that a cadquery solid is created."""

        assert self.test_shape.solid is not None
        assert self.test_shape.volume() > 1000

    def test_distance_volume_impact(self):
        """Creates solid using the BlanketCutterStar parametric component
        with different distances and checks that the volume changes accordingly
        ."""

        test_volume = self.test_shape.volume()
        self.test_shape.distance = 50
        # not quite two times as large as there is overlap in the center
        assert test_volume == pytest.approx(self.test_shape.volume() * 2, rel=0.1)
