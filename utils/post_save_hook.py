"""
Jupyter post_save_hook script for generating .py/.html files automatically when .ipynb file is saved.

Add the content to your jupyter_notebook_config.py. The location is usually $HOME/.jupyter/jupyter_notebook_config.py.
If you don't have one yet, you can generate the file: jupyter notebook --generate-config
"""

import json
import os
from subprocess import check_call

SAVE_PY = False  # Save .py files (location is <dir of original>/py/)
SAVE_HTML = True  # Save .html files (location is <dir of original>/html/)

# Run notebook before saving py/html. Note: this won't affect to the state of the .ipynb file.
RUN_NB_BEFORE_SAVE = True

# Skip saving of files which name contains of the following
DONT_SAVE = {'exercise', 'copy', 'untitled'}

# Add beatufil "Toggle output" button at the top of html page
USE_TOGGLE_BTN_IN_HTML = True

TOGGLE_OUTPUT_BTN = {
    "cell_type":
    "raw",
    "metadata": {},
    "source": [
        "<script>\n", "  function toggle() {\n",
        "    show ? $('div.output').hide('200') : $('div.output').show('200')\n",
        "    show = !show\n", "  }\n", "\n",
        "  $( document ).ready(function(){\n", "show=false;\n",
        "    $('div.output').hide()\n", "  });\n", "</script>\n", "\n",
        "<form action=\"javascript:toggle()\" style=\"text-align:center;\">\n",
        "  <input type=\"submit\" id=\"toggleButton\" value=\"Toggle output 🐍\" \n",
        "    style=\"\n", "      font-size: 20px;\n",
        "      text-align: center;\n", "      color: green;\n",
        "      border-radius: 12px;\n", "      width: 200px;\n",
        "      height: 50px;\n", "      margin-bottom: 20px;\n",
        "      margin-top: 20px;\">\n", "\n", "</form>"
    ]
}


def _run_cmd(cmd, cwd=None):
    check_call(cmd.split(), cwd=cwd)


def post_save(model, os_path, contents_manager):
    if model['type'] != 'notebook' or not (SAVE_PY or SAVE_HTML):
        return

    dir_, fname = os.path.split(os_path)

    for word in DONT_SAVE:
        if word.lower() in fname.lower():
            return

    source, tmp_name = fname, None
    out_file_base, _ = os.path.splitext(fname)

    if RUN_NB_BEFORE_SAVE:
        tmp_name = 'tmp_{}'.format(fname)
        cmd = 'jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=30 --output {} {}'.format(
            tmp_name, os_path)
        _run_cmd(cmd, cwd=dir_)
        source = tmp_name

    if SAVE_PY:
        out_dir_py = os.path.join(os.path.dirname(dir_), 'py')
        os.makedirs(out_dir_py, exist_ok=True)
        cmd = 'jupyter nbconvert --to python --output-dir {} --output {}.py {}'.format(
            out_dir_py, out_file_base, source)
        _run_cmd(cmd, cwd=dir_)

    if SAVE_HTML:
        if USE_TOGGLE_BTN_IN_HTML and RUN_NB_BEFORE_SAVE:
            with open(os.path.join(dir_, source), 'r+') as tmp_source:
                content = json.loads(tmp_source.read())
                content['cells'] = [TOGGLE_OUTPUT_BTN] + content.get(
                    'cells', [])
                tmp_source.seek(0)
                tmp_source.write(json.dumps(content))
                tmp_source.truncate()

        out_dir_html = os.path.join(os.path.dirname(dir_), 'html')
        os.makedirs(out_dir_html, exist_ok=True)
        cmd = 'jupyter nbconvert --to html --output-dir {} --output {}.html {}'.format(
            out_dir_html, out_file_base, source)
        _run_cmd(cmd, cwd=dir_)

    if tmp_name:
        tmp_file = os.path.join(dir_, tmp_name)
        if os.path.exists(tmp_file):
            os.remove(tmp_file)

c.FileContentsManager.post_save_hook = post_save