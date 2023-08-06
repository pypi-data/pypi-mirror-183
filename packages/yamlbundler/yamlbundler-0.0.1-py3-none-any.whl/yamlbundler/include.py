import contextlib
import os
import yaml
from yaml.nodes import Node
from dataclasses import dataclass

import jsonpath_ng

from yamlbundler.exception import YAMLBundlerException
from yamlbundler.util import is_list_of_dict


@dataclass
class Parameter:
    filepath: str
    jsonpath: str


class Include(yaml.YAMLObject):
    yaml_tag = "!include"

    @classmethod
    def from_yaml(cls, _: object, node: Node) -> object:
        if not isinstance(node, yaml.SequenceNode):
            param_pair = node2pram_pair(node)
            return param_pair2obj(param_pair)

        param_pairs = []
        for n in node.value:
            param_pairs.append(node2pram_pair(n))

        objs = []
        for p in param_pairs:
            objs.append(param_pair2obj(p))

        if (res := is_list_of_dict(objs)).ok:
            dict_: dict[object, object] = {}
            for obj in res.value:
                if dict_.keys().isdisjoint(obj.keys()):
                    dict_.update(obj)
                else:
                    raise YAMLBundlerException("got duplicate key!")
            return dict_

        arr: list[object] = []
        for elm in objs:
            if isinstance(elm, list):
                arr.extend(elm)
            else:
                arr.append(elm)

        return arr


def node2pram_pair(node: yaml.nodes.Node) -> Parameter:
    filepath = None
    jsonpath = "$"

    if isinstance(node, yaml.ScalarNode):
        filepath = node.value
    elif isinstance(node, yaml.MappingNode):
        for item in node.value:
            match key := item[0].value:
                case "filepath":
                    filepath = item[1].value
                case "jsonpath":
                    jsonpath = item[1].value
                case _:
                    raise YAMLBundlerException(f"got unexpected parameter: {key}")
    else:
        raise YAMLBundlerException(
            f"expected ScalarNode or MappingNode but got: {node.__class__.__name__}"
        )

    if filepath is None:
        raise YAMLBundlerException("filepath is not specified!")

    return Parameter(filepath, jsonpath)


def param_pair2obj(param: Parameter) -> object:
    filepath = os.path.abspath(param.filepath)
    # TODO avoid chdir
    with (
        open(filepath, "r") as f,
        contextlib.chdir(os.path.dirname(filepath)),
    ):
        obj = yaml.full_load(f)

    temp = jsonpath_ng.parse(param.jsonpath).find(obj)
    if len(temp) == 1:
        obj = temp[0].value
    else:
        obj = [x.value for x in temp]

    return obj
