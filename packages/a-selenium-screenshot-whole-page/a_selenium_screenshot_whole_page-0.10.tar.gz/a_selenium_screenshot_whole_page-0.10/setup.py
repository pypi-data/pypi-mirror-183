from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.10'
DESCRIPTION = "Takes a screenshot from a whole page (same size as page / no repeating parts)"

# Setting up
setup(
    name="a_selenium_screenshot_whole_page",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_selenium_screenshot_whole_page',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_cv2_easy_resize', 'a_cv_imwrite_imread_plus', 'numpy', 'opencv_python', 'pandas'],
    keywords=['Selenium', 'automation', 'screenshot'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_cv2_easy_resize', 'a_cv_imwrite_imread_plus', 'numpy', 'opencv_python', 'pandas'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*