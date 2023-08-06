import unittest

import paramak


class TestCenterColumnShieldFlatTopCircular(unittest.TestCase):
    def setUp(self):
        self.test_shape = paramak.CenterColumnShieldFlatTopCircular(
            height=600,
            arc_height=400,
            inner_radius=100,
            mid_radius=150,
            outer_radius=200,
        )

    def test_default_parameters(self):
        """Checks that the default parameters of a CenterColumnShieldFlatTopCircular are
        correct."""

        assert self.test_shape.rotation_angle == 360

    def test_points_calculation(self):
        """Checks that the points used to construct the CenterColumnShieldFlatTopCircular
        component are calculated correctly from the parameters given."""

        assert self.test_shape.points == [
            (100, 0, "straight"),
            (100, 300, "straight"),
            (200, 300, "straight"),
            (200, 200, "circle"),
            (150, 0, "circle"),
            (200, -200, "straight"),
            (200, -300, "straight"),
            (100, -300, "straight"),
        ]

    def test_processed_points_calculation(self):
        """Checks that the processed_points used to construct the
        CenterColumnShieldFlatTopCircular component are calculated correctly
        from the parameters given."""

        assert self.test_shape.processed_points == [
            (100, 0, "straight"),
            (100, 300, "straight"),
            (200, 300, "straight"),
            (200, 200, "circle"),
            (150, 0, "circle"),
            (200, -200, "straight"),
            (200, -300, "straight"),
            (100, -300, "straight"),
            (100, 0, "straight"),
        ]

    def test_creation(self):
        """Creates a center column shield using the
        CenterColumnShieldFlatTopCircular parametric component and checks that
        a cadquery solid is created."""

        assert self.test_shape.solid is not None
        assert self.test_shape.volume() > 1000

    def test_faces(self):
        """Creates a center column shield using the
        CenterColumnShieldFlatTopCircular parametric component and checks that
        a solid is created with the correct number of faces"""

        assert len(self.test_shape.areas) == 6
        assert len(set([round(i) for i in self.test_shape.areas])) == 4

        self.test_shape.rotation_angle = 180
        assert len(self.test_shape.areas) == 8
        assert len(set([round(i) for i in self.test_shape.areas])) == 5
