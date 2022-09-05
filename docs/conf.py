# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.redoc'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


# -- Extension configuration -------------------------------------------------

# add sourcecode to path
import sys, os
sys.path.insert(0, os.path.abspath('../src'))
 
 
############################
# SETUP THE RTD LOWER-LEFT #
############################

# The short X.Y version.
version = '6.16.1-dev'

# The full version, including alpha/beta/rc tags.
release = version

html_theme_options = {
    'logo_only': False,
    'display_version': True
}
