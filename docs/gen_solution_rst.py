# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('..'))


def gen_solution_rst():
    solution_py_path = os.path.abspath("../src/solution")
    solution_rst_path = os.path.abspath("source/solution")
    d = os.listdir(solution_py_path)
    no_name_map = dict()
    module_name = []
    for i in d:
        fname = i[0:-3]
        if fname == "__init__":
            continue
        rst = os.path.join(solution_rst_path, f"{fname}.rst")
        print(f"write {fname}.rst")
        with open(rst, "w") as f:
            f.write(f"{fname}\n")
            f.write("=" * 100)
            f.write("\n\n")
            f.write(f".. automodule:: src.solution.{fname}\n")
            f.write("   :members:\n")
            f.write("   :undoc-members:\n")
            f.write("   :show-inheritance:\n")

        num = fname.split("_")[0]
        no_name_map[int(num)] = fname
        module_name.append(int(num))

    module_name.sort()

    print(f"start build index.rst")
    with open(os.path.join(solution_rst_path, "index.rst"), "w") as f:

        f.write("Solution\n")
        f.write("=" * 100)
        f.write("\n\n")

        f.write(".. toctree::\n")
        f.write("   :maxdepth: 1\n\n")

        for i in module_name:
            print(f"write {no_name_map[i]}")
            f.write(f"   {no_name_map[i]}\n")


gen_solution_rst()
