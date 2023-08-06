import math
from typing import Tuple

from paramak import RotateMixedShape


class CapsuleVacuumVessel(RotateMixedShape):
    """A cylindrical vessel volume with constant thickness that has addition
    hemispherical head.

    Arguments:
        outer_start_point: the x,z coordinates of the outer bottom of the
            vacuum vessel
        radius: the radius from which the centres of the vessel meets the outer
            circumference.
        thickness: the radial thickness of the vessel in cm.
    """

    def __init__(
        self,
        radius: float,
        outer_start_point: Tuple[float, float],
        thickness: float,
        **kwargs,
    ):
        self.radius = radius
        self.thickness = thickness
        self.outer_start_point = outer_start_point[0], outer_start_point[1]

        super().__init__(**kwargs)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("VacuumVessel.radius must be a number. Not", value)
        if value <= 0:
            msg = "VacuumVessel.radius must be a positive number above 0. " f"Not {value}"
            raise ValueError(msg)
        self._radius = value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if not isinstance(value, (float, int)):
            msg = f"VacuumVessel.thickness must be a number. Not {value}"
            raise ValueError(msg)
        if value <= 0:
            msg = f"VacuumVessel.thickness must be a positive number above 0. Not {value}"
            raise ValueError(msg)
        self._thickness = value

    def find_points(self):
        """
        Finds the XZ points joined by straight and circle connections that describe the
        2D profile of the vessel shape.
        """

        radius = self.radius
        thickness = self.thickness
        bottom_outer_x, bottom_outer_y = self.outer_start_point
        top_outer_y = bottom_outer_y + (4 * radius)
        top_outer_x = bottom_outer_x
        inner_r = radius - thickness
        (bottom_outer_x, bottom_outer_y, thickness, radius, top_outer_x, top_outer_y, inner_r,) = (
            float(bottom_outer_x),
            float(bottom_outer_y),
            float(thickness),
            float(radius),
            float(top_outer_x),
            float(top_outer_y),
            float(inner_r),
        )

        point_1 = (bottom_outer_x, bottom_outer_y, "circle")
        point_3 = (point_1[0] + radius, point_1[1] + radius, "straight")
        point_4 = (point_3[0], point_3[1] + radius * 2, "circle")
        point_6 = (top_outer_x, top_outer_y, "straight")
        point_7 = (point_6[0], point_6[1] - thickness, "circle")
        point_9 = (point_4[0] - thickness, point_4[1], "straight")
        point_10 = (point_3[0] - thickness, point_3[1], "circle")
        point_12 = (point_1[0], point_1[1] + thickness, "straight")
        point_2 = (
            (point_1[0]) + (radius * math.cos((3 * math.pi) / 8)),
            (point_1[1] + radius) - (radius * math.sin((3 * math.pi) / 8)),
            "circle",
        )
        point_5 = (
            (point_6[0] + (radius * math.cos((2 * math.pi) / 8))),
            (point_6[1] - radius) + (radius * math.sin((2 * math.pi) / 8)),
            "circle",
        )
        point_8 = (
            (point_7[0] + (inner_r * math.cos((2 * math.pi) / 8))),
            (point_7[1] - inner_r) + (inner_r * math.sin((2 * math.pi) / 8)),
            "circle",
        )
        point_11 = (
            (point_12[0]) + (inner_r * math.cos((3 * math.pi) / 8)),
            (point_12[1] + inner_r) - (inner_r * math.sin((3 * math.pi) / 8)),
            "circle",
        )

        self.points = [
            point_1,
            point_2,
            point_3,
            point_4,
            point_5,
            point_6,
            point_7,
            point_8,
            point_9,
            point_10,
            point_11,
            point_12,
        ]
