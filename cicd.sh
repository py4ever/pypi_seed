echo "setup env"

if [ ! -e "venv" ] then
  virtualenv venv
fi

source ./venv/bin/activate && \
python -m pip install --upgrade pip && \
pip install -r test_requirements.txt && \
pytest --cov=pypi_seed

source ./venv/bin/activate && \
python setup.py bdist_wheel --universal

source ./venv/bin/activate && \
pip install twine && \
twine upload dist/pypi_seed-1.0.6-py2.py3-none-any.whl