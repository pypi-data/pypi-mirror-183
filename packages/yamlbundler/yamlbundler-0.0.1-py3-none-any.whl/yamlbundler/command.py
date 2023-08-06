from dataclasses import dataclass
from pathlib import Path
import argparse
import contextlib

import yaml

from yamlbundler.exception import YAMLBundlerException

# metaclass magic is used to register a constructor for Include.
# you can also use yaml.add_constructor().
from yamlbundler.include import Include as _  # noqa: F401


@dataclass(eq=True)
class Args:
    input: Path
    output: Path | None


def run() -> None:
    args = parse_args()
    main(args)


def main(args: Args) -> object:
    abspath = args.input.resolve()

    with (
        open(abspath, "r") as f,
        contextlib.chdir(abspath.parent),
    ):
        obj = yaml.full_load(f)

    yamlstr = yaml.dump(obj)

    if args.output is None:
        print(yamlstr)
    else:
        with open(args.output, "w") as f:
            f.write(yamlstr)

    return obj


def parse_args(test_args: list[str] | None = None) -> Args:
    parser = argparse.ArgumentParser(
        prog="YAML Bundler", description="Handle !include tag and bundle YAML files."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("-i", "--inplace", action="store_true")
    args = parser.parse_args(test_args)

    if args.inplace and args.output is not None:
        raise YAMLBundlerException("either one of -o or -i must be specified")

    return Args(
        input=args.input,
        output=args.input if args.inplace else args.output,
    )


if __name__ == "__main__":
    run()
