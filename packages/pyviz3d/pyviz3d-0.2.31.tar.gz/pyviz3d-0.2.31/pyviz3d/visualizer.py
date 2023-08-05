"""The visualizer class is used to show 3d point clouds or bounding boxes in the browser."""

from .points import Points
from .labels import Labels
from .lines import Lines
from .mesh import Mesh
from .camera import Camera
from .cuboid import Cuboid
from .polyline import Polyline
from .arrow import Arrow

import os
import sys
import shutil
import json
import numpy as np


class Visualizer:
    def __init__(self, position=None, look_at=None, up=None):
        if position is None:
            position = [3.0, 3.0, 3.0]
        if look_at is None:
            look_at = [0.0, 0.0, 0.0]
        if up is None:
            up = [0.0, 0.0, 1.0]

        self.camera = Camera(
            position=np.array(np.array(position)),
            look_at=np.array(np.array(look_at)),
            up=np.array(np.array(up))
        )
        self.elements = {"Camera_0": self.camera}  # dict of elements to display

    def __parse_name(self, name):
        """Makes sure the name does not contain invalid character combinations.

        :param name:
        :return:
        """
        return name.replace(':', ';')

    def add_points(
        self,
        name,
        positions,
        colors=None,
        normals=None,
        point_size=25,
        visible=True,
        alpha=1.0,
    ):
        """Add points to the visualizer.

        :param name: The name of the points displayed in the visualizer. Use ';' in the name to create sub-layers.
        :param positions: The point positions.
        :param normals: The point normals.
        :param colors: The point colors.
        :param point_size: The point size.
        :param visible: Bool if points are visible.
        :param alpha: Alpha value of colors.
        """

        assert positions.shape[1] == 3
        assert colors is None or positions.shape == colors.shape
        assert normals is None or positions.shape == normals.shape

        shading_type = 1  # Phong shading
        if colors is None:
            colors = np.ones(positions.shape, dtype=np.uint8) * 50  # gray
        if normals is None:
            normals = np.ones(positions.shape, dtype=np.float32)
            shading_type = 0  # Unifor shading when no normals are available

        positions = positions.astype(np.float32)
        colors = colors.astype(np.uint8)
        normals = normals.astype(np.float32)

        alpha = min(max(alpha, 0.0), 1.0)  # cap alpha to [0..1]

        self.elements[self.__parse_name(name)] = Points(
            positions, colors, normals, point_size, visible, alpha, shading_type
        )

    def add_labels(self, name, labels, positions, colors, visible=True):
        """Add labels to the visualizer.
        
        :param name: The name of the labels.
        :param labels: The text value of the labels.
        :param positions: The 3D positions of the labels.
        :param colors: The text color of the individual labels.
        :param visible: Bool if lines are visible.
        """

        self.elements[self.__parse_name(name)] = Labels(labels, positions, colors, visible)

    def add_lines(self, name, lines_start, lines_end, colors=None, visible=True):
        """Add lines to the visualizer.

        :param name: The name of the lines displayed in the visualizer.
        :param lines_start: The start positions of the lines.
        :param lines_end: The end positions of the lines.
        :param colors: The line colors.
        :param visible: Bool if lines are visible.
        """

        assert lines_start.shape[1] == 3
        assert lines_start.shape == lines_end.shape
        assert colors is None or lines_start.shape == colors.shape

        if colors is None:
            colors = np.ones(lines_start.shape, dtype=np.uint8) * 50  # gray

        colors = colors.astype(np.uint8)
        lines_start = lines_start.astype(np.float32)
        lines_end = lines_end.astype(np.float32)
        self.elements[self.__parse_name(name)] = Lines(lines_start, lines_end, colors, colors, visible)

    def add_bounding_box(self, name, position, size, orientation=None, color=None, alpha=1.0, edge_width=0.01, visible=True):
        """Add bounding box.

        :param name: The bounding box name. (string)
        :param position: The center position. (float32, 3x1)
        :param size: The size. (float32, 3x1)
        :param orientation: The 3D orientation (quaternion w, x, y, z) of the object.
        :param color: The color. (int32, 3x1)
        :param alpha: The transparency. (float32)
        :param edge_width: The width of the edges. (float32)
        :param visible: Bool, whether visible or not.
        """
        if orientation is None:
            orientation = np.array([0.0, 0.0, 0.0, 1.0])
        if color is None:
            color = np.array([255, 0, 0])
        orientation /= np.linalg.norm(orientation)
        self.elements[self.__parse_name(name)] = Cuboid(position, size, orientation, color, alpha, edge_width, visible)

    def add_mesh(self, name, path, translation=[0, 0, 0], rotation=[0, 0, 0, 1], scale=[1, 1, 1], color=[255, 255, 255], visible=True):
        """Adds a polygon mesh to the scene, as specified in the path, it has to be an .obj file.

        :param name: The name of the mesh displayed in the layers.
        :param path: The path to the .obj polygon mesh file.
        :param translation: The 3D translation of the object.
        :param rotation: The 3D rotation (quaternion w, x, y, z) of the object.
        :param scale: The 3D scaling of the original object.
        :param color: The uniform color of the object.
        :param visible: Whether the object is visible or not.
        """
        rotation = np.array(rotation)
        rotation = (rotation / np.linalg.norm(rotation)).tolist()
        mesh = Mesh(path, translation=translation, rotation=rotation, scale=scale, color=color, visible=visible)
        self.elements[self.__parse_name(name)] = mesh

    def add_polyline(self, name, positions, color=None, alpha=1.0, edge_width=0.01, visible=True):
        """Add polyline.

        :param name: The bounding box name. (string)
        :param positions: The N 3D positions along the polyline. (float32, Nx3)
        :param color: The color. (int32, 3x1)
        :param alpha: The transparency. (float32)
        :param edge_width: The width of the edges. (float32)
        :param visible: Bool, whether visible or not.
        """
        if color is None:
            color = np.array([255, 0, 0])
        self.elements[self.__parse_name(name)] = Polyline(positions, color, alpha, edge_width, visible)

    def add_arrow(self, name, start, end, color=None, alpha=1.0, stroke_width=0.01, head_width=0.03, visible=True):
        """Add polyline.
        :param name: The bounding box name. (string)
        :param positions: The N 3D positions along the polyline. (float32, Nx3)
        :param color: The color. (int32, 3x1)
        :param alpha: The transparency. (float32)
        :param edge_width: The width of the edges. (float32)
        :param visible: Bool, whether visible or not.
        """
        if color is None:
            color = np.array([255, 0, 0])
        self.elements[self.__parse_name(name)] = Arrow(start, end, color, alpha, stroke_width, head_width, visible)

    def save(self, path, port=6008, verbose=True):
        """Creates the visualization and displays the link to it.

        :param path: The path to save the visualization files.
        :param port: The port to show the visualization.
        :param verbose: Whether to print the web-server message or not.
        """

        # Delete destination directory if it exists already
        directory_destination = os.path.abspath(path)
        if os.path.isdir(directory_destination):
            shutil.rmtree(directory_destination)

        # Copy website directory
        directory_source = os.path.realpath(os.path.join(os.path.dirname(__file__), "src"))
        shutil.copytree(directory_source, directory_destination)

        # Assemble binary data files
        nodes_dict = {}
        for name, e in self.elements.items():
            binary_file_path = os.path.join(directory_destination, name + ".bin")
            nodes_dict[name] = e.get_properties(name + ".bin")
            e.write_binary(binary_file_path)

        # Write json file containing all scene elements
        json_file = os.path.join(directory_destination, "nodes.json")
        with open(json_file, "w") as outfile:
            json.dump(nodes_dict, outfile)

        if not verbose:
            return

        # Display link
        http_server_string = "python -m SimpleHTTPServer " + str(port)
        if sys.version[0] == "3":
            http_server_string = "python -m http.server " + str(port)
        print("")
        print(
            "************************************************************************"
        )
        print("1) Start local server:")
        print("    cd " + directory_destination + "; " + http_server_string)
        print("2) Open in browser:")
        print("    http://0.0.0.0:" + str(port))
        print(
            "************************************************************************"
        )
