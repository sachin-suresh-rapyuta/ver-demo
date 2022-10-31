# Configuration file for the Sphinx documentation builder.
import os
import sphinx

# -- Project information

project = 'Lumache'
copyright = '2022, Rapyuta Robotics'
author = 'Rapyuta Robotics'


# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.redoc',
    'sphinx_simplepdf'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'display_version': True
}

simplepdf_vars = {
    'primary-opaque': '#E11A27',
    'cover-bg': 'url(ug_front_cover.png) no-repeat center',
    'primary': '#E11A27',
    'secondary': '#E11A27',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': '#2980B9',
    'top-left-content': 'counter(page)',
    'top-center-content': '',
    'top-right-content': '"PA-AMR Documentation"',
    'bottom-left-content': 'counter(page)',
    'bottom-center-content': '"Rapyuta Robotics"',
    'bottom-right-content': 'string(heading)'
}

plantuml_output_format = "svg_img"
local_plantuml_path = os.path.join(os.path.dirname(__file__), "../", "docs", "utils", "plantuml.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"


def setup_jquery(app, exception):
    """
    Inject jQuery if Sphinx>=6.x

    Staring on Sphinx 6.0, jQuery is not included with it anymore.
    As this extension depends on jQuery, we are including it when Sphinx>=6.x
    """

    if sphinx.version_info >= (5, 0, 0):
        # https://jquery.com/download/#using-jquery-with-a-cdn
        jquery_cdn_url = "https://code.jquery.com/jquery-3.6.0.min.js"
        html_js_files = getattr(app.config, "html_js_files", [])
        html_js_files.append((
            jquery_cdn_url,
            {
                'integrity': 'sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=',
                'crossorigin': 'anonymous'
            }
        ))
        app.config.html_js_files = html_js_files

# The short X.Y version.
version = '6.16.1-dev'

# The full version, including alpha/beta/rc tags.
release = version


locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
