source ./venv/bin/activate && \
python -m pip install --upgrade pip && \
pip install -r test_requirements.txt && \
pytest

python setup.py bdist_wheel --universal


twine upload dist/pypi_seed-1.0.6-py2.py3-none-any.whl