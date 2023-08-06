"""
    PyJAMAS is Just A More Awesome Siesta
    Copyright (C) 2018  Rodrigo Fernandez-Gonzalez (rodrigo.fernandez.gonzalez@utoronto.ca)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# tests for image module
# for coverage, run:
# coverage run -m pytest
# coverage report -i

import numpy
from PyQt5.QtCore import QBuffer, QIODevice
import pytest
import skimage

from pyjamas.pjscore import PyJAMAS
from pyjamas.rimage.rimutils import rimutils
from pyjamas.rcallbacks.rcbimage import projection_types
import tests.unit.pjsfixtures as pjsfixtures

PyJAMAS_FIXTURE: PyJAMAS = PyJAMAS()
PyJAMAS_FIXTURE.options.cbSetCWD(pjsfixtures.TMP_DIR)


@pytest.mark.usefixtures("contrastlimits_fixture")
def test_cbAdjustContrast(contrastlimits_fixture):
    PyJAMAS_FIXTURE.image.cbAdjustContrast(contrastlimits_fixture[0], contrastlimits_fixture[1])

    theqimage = PyJAMAS_FIXTURE._imageItem.pixmap().toImage()
    displayed_image = numpy.empty((PyJAMAS_FIXTURE.height, PyJAMAS_FIXTURE.width), dtype=numpy.uint8)

    for row_index in range(PyJAMAS_FIXTURE.height):
        for col_index in range(PyJAMAS_FIXTURE.width):
            displayed_image[row_index, col_index] = theqimage.pixel(col_index, row_index)

    assert numpy.array_equal(displayed_image,
                             numpy.array(
                                 rimutils.stretch(PyJAMAS_FIXTURE.imagedata,
                                                  contrastlimits_fixture[0],
                                                  contrastlimits_fixture[1]),
                                 dtype=numpy.uint8))


@pytest.mark.usefixtures("projectionpath_fixture")
def test_cbProjectImage(projectionpath_fixture):
    for aprojectionpath, aprojectiontype in zip(projectionpath_fixture, projection_types):
        PyJAMAS_FIXTURE.image.cbProjectImage([], aprojectiontype)
        theproj = PyJAMAS_FIXTURE.slices.copy()
        PyJAMAS_FIXTURE.options.cbUndo()

        assert numpy.array_equal(theproj, skimage.io.imread(aprojectionpath))


PyJAMAS_FIXTURE.app.quit()
