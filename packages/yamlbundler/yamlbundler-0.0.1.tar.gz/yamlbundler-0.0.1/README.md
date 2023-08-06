# YAML Bundler
`yamlbundler` is a useful command that bundles multiple YAML files into a single file.
It finds `!include` tag in a YAML file and replaces it with the contents of another YAML file.

## Install

```bash
pip install yamlbundler
```

## Quick start
Save these files in your working directory.

```yaml
# ./main.yaml

# include entire file
a: !include ./sub1.yaml  # relative path from the parent directory of main.yaml 
b: !include
  filepath: ./sub2.yaml 

# include specific value using jsonpath
c: !include
  filepath: ./sub1.yaml
  jsonpath: $.foo

# include multiple files
# Array elements are flattened.
d: !include
- filepath: ./sub1.yaml
- filepath: ./sub2.yaml

# include multiple files
# If all of them are map elements, they are merged into a single map.
e: !include
- filepath: ./sub1.yaml
- filepath: ./sub3.yaml
```
```yaml
# ./sub1.yaml
foo: bar
```

```yaml
# ./sub2.yaml
- one
- two
```

```yaml
# ./sub3.yaml
hoge: !include
  # relative path from the parent directory of sub3.yaml (not main.yaml)
  filepath: ./sub2.yaml
  jsonpath: $[0]
```

Then, run this command.
The result is shown in your terminal as STDOUT.
Comments in original YAML are removed.

```bash
yamlbundler ./main.yaml

# a:
#   foo: bar
# b:
# - one
# - two
# c: bar
# d:
# - foo: bar
# - one
# - two
# e:
#   foo: bar
#   hoge: one
```

You can save the result as a new file using `--output` parameter.
If you want to overwrite the original file, use `--inplace` parameter.

```bash
yamlbundler --output ./result.yaml ./main.yaml
yamlbundler --inplace ./main.yaml
```

# Feedback
If you find any bugs, please feel free to create an issue.
