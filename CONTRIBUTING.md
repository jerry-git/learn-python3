# Contributing

If you spot a typo or the content does not make sense in some way, feel free to open an issue or directly create a PR.

I am open for enhancement ideas and feature requests. If there's some topic you'd like to see a notebook about, feel free to open an issue and request it there.
 
## Development
Install development dependencies
```
pip install -r dev-requirements.txt
```

#### Generating html
```
python scripts/notebook_to_html.py <path-to-ipynb-file>
```

#### Testing
```
pytest --nbval notebooks
```

#### pre-commit
```
pre-commit install
```
and it'll automatically run all the pre-commit hooks for each commit. 
