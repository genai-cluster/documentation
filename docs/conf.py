project = 'CORE GenAI-Cluster Dokumentation'
copyright = '2025, DIGIT TU Clausthal'
author = 'DIGIT TU Clausthal'

extensions = [
    'myst_parser',
    'sphinx_copybutton',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_logo = '_static/logotransparent.png'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['disable-dark-mode.js']

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#000000",
        "color-brand-content": "#000000",
    },
}
