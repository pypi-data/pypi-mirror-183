from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.10'
DESCRIPTION = "Uses pandas/numpy/numexpr for operations on pictures - very fast"

# Setting up
setup(
    name="a_pandas_ex_image_tools",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_image_tools',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_cv2_imshow_thread', 'a_cv_imwrite_imread_plus', 'a_pandas_ex_closest_color', 'a_pandas_ex_column_reduce', 'a_pandas_ex_enumerate_groups', 'a_pandas_ex_horizontal_explode', 'a_pandas_ex_lookupdict', 'a_pandas_ex_multiloc', 'a_pandas_ex_obj_into_cell', 'a_pandas_ex_plode_tool', 'a_pandas_ex_to_tuple', 'ansi', 'flatten_everything', 'flexible_partial', 'numexpr', 'numpy', 'opencv_python', 'pandas', 'PrettyColorPrinter', 'scikit_learn', 'Shapely'],
    keywords=['pandas', 'OpenCV', 'cv2', 'images', 'pixels', 'detection'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_cv2_imshow_thread', 'a_cv_imwrite_imread_plus', 'a_pandas_ex_closest_color', 'a_pandas_ex_column_reduce', 'a_pandas_ex_enumerate_groups', 'a_pandas_ex_horizontal_explode', 'a_pandas_ex_lookupdict', 'a_pandas_ex_multiloc', 'a_pandas_ex_obj_into_cell', 'a_pandas_ex_plode_tool', 'a_pandas_ex_to_tuple', 'ansi', 'flatten_everything', 'flexible_partial', 'numexpr', 'numpy', 'opencv_python', 'pandas', 'PrettyColorPrinter', 'scikit_learn', 'Shapely'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*