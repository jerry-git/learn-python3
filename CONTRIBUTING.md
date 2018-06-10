# Contributing

If you spot a typo or the content does not make sense in some way, feel free to open an issue or directly create a PR.

I am open for enhancement ideas and feature requests. If there's some topic you'd like to see a notebook about, feel free to open an issue and request it there.
 
## Development

#### post_save_hook
* Copy the content of utils/post_save_hook.py to your jupyter_notebook_config.py before making changes to notebooks
* This will setup a post_save_hook which will generate a html version of the notebook automatically when the notebook is saved
* htmls are not generated for exercises

#### Testing
* Travis CI will make sure that the code cells in the notebooks can be executed
* You test the same locally by:
    * install tox by: `pip install tox`
    * run tox: `tox`
* Tests are not run for exercises (because the code in the exercise cells is usually intentionally incomplete)