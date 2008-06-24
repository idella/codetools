from setuptools import setup, Extension, find_packages


# Function to convert simple ETS project names and versions to a requirements
# spec that works for both development builds and stable builds.  Allows
# a caller to specify a max version, which is intended to work along with
# Enthought's standard versioning scheme -- see the following write up:
#    https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers
def etsdep(p, min, max=None, literal=False):
    require = '%s >=%s.dev' % (p, min)
    if max is not None:
        if literal is False:
            require = '%s, <%s.a' % (require, max)
        else:
            require = '%s, <%s' % (require, max)
    return require


# Configure our setup.
setup(
    author = 'Enthought, Inc',
    author_email = 'info@enthought.com',
    dependency_links = [
        'http://code.enthought.com/enstaller/eggs/source',
        ],
    description = 'Numerical Modeling',
    extras_require = {
        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            "docutils",
            "Geo",    # we use geo.cow (a different enthought repo) in /ui/interactor.py
            'PIL',
            "numpy >=1.0.2",
            ],
        },
    include_package_data = True,
    install_requires = [
        TRAITS
        ],
    license = 'BSD',
    name = 'CodeTools',
    namespace_packages = [
        "enthought",
        ],
    packages = find_packages(exclude=[
        'integrationtests',
        'integrationtests.*',
        ]),
    tests_require = [
        DEVTOOLS,
        'nose >= 0.9',
        ],
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/ets',
    version = '3.0.0b1',
    zip_safe = False,
    )
