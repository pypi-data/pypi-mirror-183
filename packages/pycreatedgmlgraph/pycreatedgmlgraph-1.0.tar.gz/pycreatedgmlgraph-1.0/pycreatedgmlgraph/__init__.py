from abc import ABC, abstractmethod
from types import ModuleType
from typing import Any, Iterable
from dis import Bytecode
from importlib import import_module
from pycolorgenerator import ColorGenerator #type: ignore



class Render:
    _nodes: list[str]
    _links: list[str]

    @property
    def nodes(self): return self._nodes

    @property
    def links(self): return self._links

    def __init__(self):
        self._nodes = []
        self._links = []

    def render(self) -> str:
        nodes_str = "\n".join(self._nodes)
        links_str = "\n".join(self._links)
        return f"""
<?xml version="1.0" encoding="utf-8"?>
<DirectedGraph Title="DrivingTest" xmlns="http://schemas.microsoft.com/vs/2009/dgml" Layout="Sugiyama" GraphDirection="TopToBottom">
<Nodes>
{nodes_str}
</Nodes>
<Links>
{links_str}
</Links>
</DirectedGraph>"""


class Node:
    _childs: Iterable["Node"]
    _name: str
    _id: int
    _color: str

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def get_render(self) -> Render:
        render = Render()
        render.nodes.append(
            f'<Node Id="{self._id}" Label="{self._name}" Background="White" Stroke="{self._color}" StrokeThickness=5/>')

        for child in self._childs:
            child_render = child.get_render()
            render.nodes.extend(child_render.nodes)
            render.links.extend(child_render.links)
            render.links.append(
                f'<Link Source="{self._id}" Target="{child.id}" />')

        return render

    def render(self) -> str:
        return self.get_render().render()

    def __init__(self, name: str, childs: Iterable["Node"], id: int, color1: str):
        self._name = name
        self._childs = childs
        self._id = id
        self._color = color1


        



class ColorChooser:
    _d: dict[Any, str]

    def __init__(self):
        self._color_generator = ColorGenerator()
        self._d = {}

    def get_color(self, key: Any) -> str:
        if key in self._d:
            return self._d[key]
        else:
            self._d[key] = color = next(self._color_generator)
            return color

class AbstractGraph(ABC):
    _root_node: Node
    _color_chooser: ColorChooser
    _last_id: int

    def __init__(self):
        self._color_chooser = ColorChooser()
        self._last_id = 0

    def render(self):
        return self._root_node.render()


class Graph(AbstractGraph):
    def set_root_node(self, node: Node):
        self._root_node = node

    def new_node(self, name: str, *childs: Node) -> Node:
        self._last_id += 1
        return Node(name, childs, self._last_id, *self._color_chooser.get_color(name))


class AbstractModulesGraph(AbstractGraph):
    def __init__(self, module: ModuleType):
        super().__init__()
        self._root_node = self._new_node(module)
            
    @classmethod
    def _to_show_module_childs(cls, module: ModuleType) -> bool:
        """Returns True if childs of the module should be shown"""
        return True

    @classmethod
    @abstractmethod
    def _to_show_module(cls, module: ModuleType) -> bool:
        """Returns True if the module should be shown"""
        raise NotImplementedError

    def _new_node(self, module: ModuleType, parent_module_files: list[str] = []) -> Node: 
        name = module.__name__
        childs: list[Node] = []
        if hasattr(module, "__file__") and module.__file__ and self._to_show_module_childs(module):
            new_parent_module_files = parent_module_files + [module.__file__]
            try:
                bytecode = Bytecode(module.__spec__.loader.get_code(module.__name__)) # type: ignore        
            except:
                pass
            else:
                for instruction in bytecode:
                    if instruction.opname == "IMPORT_NAME":
                        try:
                            new_module = import_module(instruction.argval)
                        except (ImportError, ValueError):
                            pass
                        else:
                            if hasattr(new_module, "__file__") and new_module.__file__ not in new_parent_module_files and self._to_show_module(new_module):
                                childs.append(self._new_node(new_module, new_parent_module_files))

        self._last_id += 1
        return Node(name, childs, self._last_id, self._color_chooser.get_color(name))

    def render(self):
        return self._root_node.render()