### Figures in the CHAOS API documention
This folder contains a number of figures written in LaTeX with the _tikZ_
package.

#### Build
List the figures in `figure_list.json`

    { "filename": "<image width>x<image height>", ... }

Then build the figures by running

    python build_figures.py

this will update the figures in `source/static/`.

#### Dependencies
* LuaTeX
* the `tikZ` LaTeX package
* ImageMagick
* Python with the `Cheetah` and `sh` packages

#### Image size
ImageMagick will create `.png`-images with correct aspect ratio (according to the
LaTeX document) that fits inside a bounding box of `width x height`. In other words
the generated image will never be larger than your size specification, but will
most likely be smaller in order to preserve the aspect ratio.