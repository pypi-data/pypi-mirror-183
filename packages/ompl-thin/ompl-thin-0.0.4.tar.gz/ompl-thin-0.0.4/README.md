## ompl-thin
is a thin wrapper of [ompl](https://github.com/ompl/ompl). For a thick wrapper, please see ompl's [official python bindings](https://ompl.kavrakilab.org/python.html).

Advantage of this package is mainly in quickness and simpleness of building, achieved by focusing on only *thin-wrapping* the ompl pacakge and utilizing pybind11.

## installation
The package is available on [pypi](https://pypi.org/project/ompl-thin/). So, to install you just need to
```bash
sudo apt install libboost-filesystem-dev libboost-serialization-dev -y  # shared dependency
pip3 install ompl-thin
```
NOTE: binary distribution is available only for x86_64. For other architecture, only source distributions are available and takes few minutes to install.
