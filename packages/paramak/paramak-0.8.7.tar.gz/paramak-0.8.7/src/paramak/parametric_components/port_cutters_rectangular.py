from typing import Tuple

from paramak import ExtrudeStraightShape


class PortCutterRectangular(ExtrudeStraightShape):
    """Creates an extruded shape with a rectangular section that is used to cut
    other components (eg. blanket, vessel,..) in order to create ports.

    Args:
        height: height (cm) of the port cutter.
        width: width (cm) of the port cutter.
        distance: extruded distance (cm) of the port cutter.
        center_point: Center point of the port cutter. Defaults to (0, 0).
        workplane: workplane in which the port cutters are created. Defaults
            to "ZY".
        rotation_axis: axis around which the port cutters are rotated and
            placed. Defaults to "Z".
        extrusion_start_offset (float, optional): the distance between 0 and
            the start of the extrusion. Defaults to 1..
        fillet_radius (float, optional): If not None, radius (cm) of fillets
            added to edges orthogonal to the Z direction. Defaults to None.
        name (str, optional): defaults to "rectangular_port_cutter".
    """

    def __init__(
        self,
        height: float,
        width: float,
        distance: float,
        center_point: Tuple[float, float] = (0, 0),
        workplane: str = "ZY",
        rotation_axis: str = "Z",
        extrusion_start_offset: float = 1.0,
        fillet_radius: float = None,
        name: str = "rectangular_port_cutter",
        **kwargs
    ):

        super().__init__(
            workplane=workplane,
            rotation_axis=rotation_axis,
            extrusion_start_offset=extrusion_start_offset,
            extrude_both=False,
            name=name,
            distance=distance,
            **kwargs
        )

        self.height = height
        self.width = width
        self.center_point = center_point
        self.fillet_radius = fillet_radius

    def find_points(self):
        if self.workplane[0] < self.workplane[1]:
            parameter_1 = self.width
            parameter_2 = self.height
        else:
            parameter_1 = self.height
            parameter_2 = self.width

        points = [
            (-parameter_1 / 2, parameter_2 / 2),
            (parameter_1 / 2, parameter_2 / 2),
            (parameter_1 / 2, -parameter_2 / 2),
            (-parameter_1 / 2, -parameter_2 / 2),
        ]
        points = [(e[0] + self.center_point[0], e[1] + self.center_point[1]) for e in points]

        self.points = points

    def add_fillet(self, solid):
        if "X" not in self.workplane:
            filleting_edge = "|X"
        if "Y" not in self.workplane:
            filleting_edge = "|Y"
        if "Z" not in self.workplane:
            filleting_edge = "|Z"

        if self.fillet_radius is not None and self.fillet_radius != 0:
            solid = solid.edges(filleting_edge).fillet(self.fillet_radius)

        return solid
