import os
import unittest
from pathlib import Path

import pytest
from cadquery import Plane

import paramak


class TestShape(unittest.TestCase):
    def setUp(self):

        self.my_shape = paramak.CenterColumnShieldHyperbola(
            height=500,
            inner_radius=50,
            mid_radius=60,
            outer_radius=100,
        )

        self.test_rotate_mixed_shape = paramak.RotateMixedShape(
            rotation_angle=1,
            points=[
                (100, 0, "straight"),
                (200, 0, "circle"),
                (250, 50, "circle"),
                (200, 100, "straight"),
                (150, 100, "straight"),
                (140, 75, "straight"),
                (110, 45, "straight"),
            ],
        )
        self.test_extrude_mixed_shape = paramak.ExtrudeMixedShape(
            distance=1,
            points=[
                (100, 0, "straight"),
                (200, 0, "circle"),
                (250, 50, "circle"),
                (200, 100, "straight"),
                (150, 100, "straight"),
                (140, 75, "straight"),
                (110, 45, "straight"),
            ],
        )

    def test_shape_default_properties(self):
        """Creates a Shape object and checks that the points attribute has
        a default of None."""

        test_shape = paramak.Shape()

        assert test_shape.points is None

    def test_azimuth_placement_angle_getting_setting(self):
        """Checks that the azimuth_placement_angle of a Shape can be
        changed to a single value or iterable."""

        test_shape = paramak.Shape()

        assert test_shape.azimuth_placement_angle == 0
        test_shape.azimuth_placement_angle = 180
        assert test_shape.azimuth_placement_angle == 180
        test_shape.azimuth_placement_angle = [0, 90, 180, 270]
        assert test_shape.azimuth_placement_angle == [0, 90, 180, 270]

    def test_missing_filename_arg_in_export_stp(self):
        """Checks that an error is raised when a stp export is requested
        without a filename."""

        def incorrect_args():
            self.my_shape.export_stp()

        self.assertRaises(TypeError, incorrect_args)

    def test_missing_filename_arg_in_export_stl(self):
        """Checks that an error is raised when a stl export is requested
        without a filename."""

        def incorrect_args():
            self.my_shape.export_stl()

        self.assertRaises(TypeError, incorrect_args)

    def test_incorrect_color_values(self):
        """Checks that an error is raised when the color of a shape is
        defined as an invalid string."""

        def incorrect_color_string():
            paramak.Shape(color=("1", "0", "1"))

        self.assertRaises(ValueError, incorrect_color_string)

    def test_incorrect_workplane(self):
        """Creates Shape object with incorrect workplane and checks errors
        are raised."""

        with pytest.raises(ValueError):
            paramak.Shape(workplane="AB")

        with pytest.raises(TypeError):
            paramak.Shape(workplane=2)

        with pytest.raises(TypeError):
            paramak.Shape(workplane=[1, 2])

    def test_incorrect_points(self):
        """Creates Shape objects and checks errors are raised correctly when
        specifying points."""

        test_shape = paramak.Shape()

        def incorrect_points_end_point_is_start_point():
            """Checks ValueError is raised when the start and end points are
            the same."""
            # setting straight otherwise another error is caught
            test_shape.connection_type = "straight"
            test_shape.points = [(0, 200), (200, 100), (0, 0), (0, 200)]

        # check that an error is raised
        with pytest.raises(ValueError) as err:
            incorrect_points_end_point_is_start_point()

        # check that the correct error was raised
        expected_err_message = "The coordinates of the last and first points are"
        assert expected_err_message in str(err.value)

        def incorrect_points_missing_z_value():
            """Checks ValueError is raised when a point is missing a z
            value."""

            test_shape.points = [(0, 200), (200), (0, 0), (0, 50)]

        self.assertRaises(ValueError, incorrect_points_missing_z_value)

        def incorrect_points_not_a_list():
            """Checks ValueError is raised when the points are not a list."""

            test_shape.points = "(0, 0), (0, 20), (20, 20), (20, 0)"

        self.assertRaises(ValueError, incorrect_points_not_a_list)

        def incorrect_points_wrong_number_of_entries():
            """Checks ValueError is raised when individual points dont have 2
            or 3 entries."""

            test_shape.points = [(0, 0), (0, 20), (20, 20, 20, 20)]

        self.assertRaises(ValueError, incorrect_points_wrong_number_of_entries)

        def incorrect_x_point_value_type():
            """Checks ValueError is raised when X point is not a number."""

            test_shape.points = [("string", 0), (0, 20), (20, 20)]

        self.assertRaises(ValueError, incorrect_x_point_value_type)

        def incorrect_y_point_value_type():
            """Checks ValueError is raised when Y point is not a number."""

            test_shape.points = [(0, "string"), (0, 20), (20, 20)]

        self.assertRaises(ValueError, incorrect_y_point_value_type)

    def test_create_limits(self):
        """Creates a Shape object and checks that the create_limits function
        returns the expected values for x_min, x_max, z_min and z_max."""

        test_shape = paramak.Shape(connection_type="straight")

        test_shape.points = [
            (0, 0),
            (0, 10),
            (0, 20),
            (10, 20),
            (20, 20),
            (20, 10),
            (20, 0),
            (10, 0),
        ]

        assert test_shape.create_limits() == (0.0, 20.0, 0.0, 20.0)

        # test with a component which has a find_points method
        test_shape2 = paramak.Plasma()
        test_shape2.create_limits()
        assert test_shape2.x_min is not None

    def test_create_limits_error(self):
        """Checks error is raised when no points are given."""

        test_shape = paramak.Shape()

        def limits():
            test_shape.create_limits()

        self.assertRaises(ValueError, limits)

    def test_initial_solid_construction(self):
        """Creates a shape and checks that a cadquery solid with a unique hash
        value is created when .solid is called."""

        test_shape = paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20), (20, 0)], rotation_angle=360)

        assert test_shape.hash_value is None
        assert test_shape.solid is not None
        assert type(test_shape.solid).__name__ == "Workplane"
        assert test_shape.hash_value is not None

    def test_solid_return(self):
        """Checks that the same cadquery solid with the same unique hash value
        is returned when shape.solid is called again after no changes have been
        made to the Shape."""

        test_shape = paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20), (20, 0)], rotation_angle=360)

        assert test_shape.solid is not None
        initial_hash_value = test_shape.hash_value
        assert test_shape.solid is not None
        assert initial_hash_value == test_shape.hash_value

    def test_conditional_solid_reconstruction(self):
        """Checks that a new cadquery solid with a new unique hash value is
        constructed when shape.solid is called after changes to the Shape have
        been made."""

        test_shape = paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20)], rotation_angle=360)

        assert test_shape.solid is not None
        assert test_shape.hash_value is not None
        initial_hash_value = test_shape.hash_value

        test_shape.rotation_angle = 180

        assert test_shape.solid is not None
        assert test_shape.hash_value is not None
        assert initial_hash_value != test_shape.hash_value

    def test_hash_value_update(self):
        """Checks that the hash value of a Shape is not updated until a new
        cadquery solid has been created."""

        test_shape = paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20)], rotation_angle=360)
        test_shape.solid
        assert test_shape.hash_value is not None
        initial_hash_value = test_shape.hash_value

        test_shape.rotation_angle = 180
        assert test_shape.hash_value == initial_hash_value
        test_shape.solid
        assert test_shape.hash_value != initial_hash_value

    def test_export_html(self):
        """Checks a plotly figure of the Shape is exported by the export_html
        method with the correct filename with RGB and RGBA colors."""

        test_shape = paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20), (20, 0)], rotation_angle=360)

        os.system("rm filename.html")
        test_shape.export_html("filename")
        assert Path("filename.html").exists() is True
        os.system("rm filename.html")
        test_shape.color = (1, 0, 0, 0.5)
        test_shape.export_html("filename")
        assert Path("filename.html").exists() is True
        os.system("rm filename.html")

    def test_export_html_view_planes(self):
        """Checks a plotly figure of the Shape is exported by the export_html
        method with a range of different view_plane options."""

        test_shape = paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20), (20, 0)], rotation_angle=180)

        for view_plane in ["XZ", "XY", "YZ", "YX", "ZY", "ZX", "RZ", "XYZ"]:
            os.system("rm *.html")
            test_shape.export_html(filename="filename", view_plane=view_plane)
            assert Path("filename.html").exists() is True

    def test_export_html_with_points_None(self):
        """Checks that an error is raised when points is None and export_html"""
        test_shape = paramak.Shape()

        def export():
            test_shape.export_html("out.html")

        self.assertRaises(ValueError, export)

    def test_export_html_with_wire_None(self):
        """Checks that an error is raised when wire is None and export_html"""
        test_shape = paramak.Shape(
            points=[(0, 0), (0, 20), (20, 20), (20, 0)],
            connection_type="straight",
        )
        test_shape.wire = None

        def export():
            test_shape.export_html("out.html")

        self.assertRaises(ValueError, export)

    def test_invalid_stp_filename(self):
        """Checks ValueError is raised when invalid stp filenames are used."""

        def invalid_filename_suffix():

            test_shape = paramak.RotateStraightShape(
                points=[(0, 0), (0, 20), (20, 20)],
            )
            test_shape.export_stp(filename="test_shape.txt")

        self.assertRaises(ValueError, invalid_filename_suffix)

        def invalid_filename_type():

            test_shape = paramak.RotateStraightShape(
                points=[(0, 0), (0, 20), (20, 20)],
            )
            test_shape.export_stp(filename=1)

        self.assertRaises(TypeError, invalid_filename_type)

    def test_invalid_stl_filename(self):
        """Checks ValueError is raised when invalid stl filenames are used."""

        def invalid_filename_suffix():

            test_shape = paramak.RotateStraightShape(
                points=[(0, 0), (0, 20), (20, 20)],
            )
            test_shape.export_stl(filename="test_shape.txt")

        self.assertRaises(ValueError, invalid_filename_suffix)

        def invalid_filename_type():

            test_shape = paramak.RotateStraightShape(
                points=[(0, 0), (0, 20), (20, 20)],
            )
            test_shape.export_stp(filename=1)

        self.assertRaises(TypeError, invalid_filename_type)

    def test_invalid_color(self):
        """Checks ValueError is raised when invalid colors are used."""

        def invalid_color_type():

            paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20)], color=255)

        self.assertRaises(ValueError, invalid_color_type)

        def invalid_color_length():

            paramak.RotateStraightShape(points=[(0, 0), (0, 20), (20, 20)], color=(255, 255, 255, 1, 1))

        self.assertRaises(ValueError, invalid_color_length)

    def test_volumes_add_up_to_total_volume_Compound(self):
        """Checks the volume and volumes attributes are correct types
        and that the volumes sum to equalt the volume for a Compound."""

        test_shape = paramak.PoloidalFieldCoilSet(heights=[10, 10], widths=[20, 20], center_points=[(15, 15), (50, 50)])

        assert isinstance(test_shape.volume(), float)
        assert isinstance(test_shape.volume(split_compounds=True), list)
        assert isinstance(test_shape.volume(split_compounds=True)[0], float)
        assert isinstance(test_shape.volume(split_compounds=True)[1], float)
        assert len(test_shape.volume(split_compounds=True)) == 2
        assert sum(test_shape.volume(split_compounds=True)) == pytest.approx(test_shape.volume())

    def test_volumes_add_up_to_total_volume(self):
        """Checks the volume and volumes attributes are correct types
        and that the volumes sum to equalt the volume."""

        test_shape = paramak.PoloidalFieldCoil(center_point=(100, 100), height=50, width=50)

        assert isinstance(test_shape.volume(), float)
        assert isinstance(test_shape.volume(split_compounds=True), list)
        assert isinstance(test_shape.volume(split_compounds=True)[0], float)
        assert len(test_shape.volume(split_compounds=True)) == 1
        assert sum(test_shape.volume(split_compounds=True)) == pytest.approx(test_shape.volume())

    def test_areas_add_up_to_total_area_Compound(self):
        """Checks the area and areas attributes are correct types
        and that the areas sum to equalt the area for a Compound."""

        test_shape = paramak.PoloidalFieldCoilSet(heights=[10, 10], widths=[20, 20], center_points=[(15, 15), (50, 50)])

        assert isinstance(test_shape.area, float)
        assert isinstance(test_shape.areas, list)
        assert isinstance(test_shape.areas[0], float)
        assert isinstance(test_shape.areas[1], float)
        assert isinstance(test_shape.areas[2], float)
        assert isinstance(test_shape.areas[3], float)
        assert isinstance(test_shape.areas[4], float)
        assert isinstance(test_shape.areas[5], float)
        assert isinstance(test_shape.areas[6], float)
        assert isinstance(test_shape.areas[7], float)
        assert len(test_shape.areas) == 8
        assert sum(test_shape.areas) == pytest.approx(test_shape.area)

    def test_areas_add_up_to_total_area(self):
        """Checks the area and areas attributes are correct types
        and that the areas sum to equalt the area."""

        test_shape = paramak.PoloidalFieldCoil(center_point=(100, 100), height=50, width=50)

        assert isinstance(test_shape.area, float)
        assert isinstance(test_shape.areas, list)
        assert isinstance(test_shape.areas[0], float)
        assert isinstance(test_shape.areas[1], float)
        assert isinstance(test_shape.areas[2], float)
        assert isinstance(test_shape.areas[3], float)
        assert len(test_shape.areas) == 4
        assert sum(test_shape.areas) == pytest.approx(test_shape.area)

    def test_create_patch_error(self):
        """Checks _create_patch raises a ValueError when points is None."""

        test_shape = paramak.Shape()

        def patch():
            test_shape._create_patch()

        self.assertRaises(ValueError, patch)

    def test_create_patch_alpha(self):
        """Checks _create_patch returns a patch when alpha is given."""

        test_shape = paramak.PoloidalFieldCoil(center_point=(100, 100), height=50, width=50, color=(0.5, 0.5, 0.5, 0.1))
        assert test_shape._create_patch() is not None

    def test_azimuth_placement_angle_error(self):
        """Checks an error is raised when invalid value for
        azimuth_placement_angle is set.
        """

        test_shape = paramak.Shape()

        def angle_str():
            test_shape.azimuth_placement_angle = "coucou"

        def angle_str_in_Iterable():
            test_shape.azimuth_placement_angle = [0, "coucou"]

        self.assertRaises(ValueError, angle_str)
        self.assertRaises(ValueError, angle_str_in_Iterable)

    def test_name_error(self):
        """Checks an error is raised when invalid value for name is set."""

        test_shape = paramak.Shape()

        def name_float():
            test_shape.name = 2.0

        def name_int():
            test_shape.name = 1

        def name_list():
            test_shape.name = ["coucou"]

        self.assertRaises(ValueError, name_float)
        self.assertRaises(ValueError, name_int)
        self.assertRaises(ValueError, name_list)

    def test_workplane_of_type_cadquery_plane(self):
        """Tests that a Cadquery.Plane is accepted as a workplane entry"""

        normal_vec = (1, 1, 1)
        workplane = Plane(origin=(0, 0, 0), xDir=(-1, 1, 0), normal=normal_vec)
        # in future releases of CQ, origin and xDir will be optional

        test_shape = paramak.Shape(
            workplane=workplane,
        )

        assert isinstance(test_shape.workplane, Plane)

    def test_get_rotation_axis(self):
        """Creates a shape and test the expected rotation_axis is the correct
        values for several cases
        """
        shape = paramak.Shape()
        expected_dict = {
            "X": [(-1, 0, 0), (1, 0, 0)],
            "-X": [(1, 0, 0), (-1, 0, 0)],
            "Y": [(0, -1, 0), (0, 1, 0)],
            "-Y": [(0, 1, 0), (0, -1, 0)],
            "Z": [(0, 0, -1), (0, 0, 1)],
            "-Z": [(0, 0, 1), (0, 0, -1)],
        }
        # test with axis from string
        for axis in expected_dict:
            shape.rotation_axis = axis
            assert shape.get_rotation_axis()[0] == expected_dict[axis]
            assert shape.get_rotation_axis()[1] == axis

        # test with axis from list of two points
        expected_axis = [(-1, -2, -3), (1, 4, 5)]
        shape.rotation_axis = expected_axis
        assert shape.get_rotation_axis()[0] == expected_axis
        assert shape.get_rotation_axis()[1] == "custom_axis"

        # test with axis from workplane
        shape.rotation_axis = None

        workplanes = ["XY", "XZ", "YZ"]
        expected_axis = ["Y", "Z", "Z"]
        for wp, axis in zip(workplanes, expected_axis):
            shape.workplane = wp
            assert shape.get_rotation_axis()[0] == expected_dict[axis]
            assert shape.get_rotation_axis()[1] == axis

        # test with axis from path_workplane
        for wp, axis in zip(workplanes, expected_axis):
            shape.path_workplane = wp
            assert shape.get_rotation_axis()[0] == expected_dict[axis]
            assert shape.get_rotation_axis()[1] == axis

    def test_rotation_axis_error(self):
        """Checks errors are raised when incorrect values of rotation_axis are
        set
        """
        incorrect_values = [
            "coucou",
            2,
            2.2,
            [(1, 1, 1), "coucou"],
            [(1, 1, 1), 1],
            [(1, 1, 1), 1.0],
            [(1, 1, 1), (1, 1, 1)],
            [(1, 1, 1), (1, 0, 1, 2)],
            [(1, 1, 1, 2), (1, 0, 2)],
            # [(1, 1, 2), [1, 0, 2]], lists are now acceptable
            [(1, 1, 1)],
            [(1, 1, 1), (1, "coucou", 1)],
            [(1, 1, 1), (1, 0, 1), (1, 2, 3)],
        ]
        shape = paramak.Shape()

        def set_value():
            shape.rotation_axis = incorrect_values[i]

        for i in range(len(incorrect_values)):
            self.assertRaises(ValueError, set_value)

    def test_setting_color_incorrectly_too_large(self):
        """Sets the shape.colour outside of the the 0 to 1 range"""

        def check_correct_error_is_rasied():
            self.my_shape.color = (255, 255, 2)

        self.assertRaises(ValueError, check_correct_error_is_rasied)

    def test_setting_color_incorrectly_too_small(self):
        """Sets the shape.colour outside of the the 0 to 1 range"""

        def check_correct_error_is_rasied():
            self.my_shape.color = (-1, 0, 0)

        self.assertRaises(ValueError, check_correct_error_is_rasied)

    def test_reuse_points_between_shapes(self):
        """Checks that points can be reused between shapes"""
        points = [
            (100, 0, "straight"),
            (200, 0, "straight"),
            (250, 50, "straight"),
            (200, 100, "straight"),
        ]
        paramak.Shape(points=points)
        paramak.Shape(points=points)

    def test_reuse_points_and_connections(self):
        """Checks that points can be reused between shapes"""
        points = [
            (100, 0, "straight"),
            (200, 0, "straight"),
            (250, 50, "straight"),
            (200, 100, "straight"),
        ]
        test_shape = paramak.Shape(points=points)

        assert test_shape.points == [
            (100, 0, "straight"),
            (200, 0, "straight"),
            (250, 50, "straight"),
            (200, 100, "straight"),
        ]

    def test_reuse_points(self):
        """Checks that points can be reused between shapes"""
        points = [
            (100, 0),
            (200, 0),
            (250, 50),
            (200, 100),
        ]
        test_shape = paramak.Shape(points=points, connection_type="straight")

        assert test_shape.points == [
            (100, 0),
            (200, 0),
            (250, 50),
            (200, 100),
        ]


if __name__ == "__main__":
    unittest.main()
