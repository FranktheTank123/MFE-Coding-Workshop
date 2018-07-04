clean: clean-pyc
	conda remove --name mfe_workshop --all --yes || echo
	echo Run "source deactivate" to exit from the conda environment

clean-pyc: ## removes pyc files from your local directory
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;

install:
	conda create --name mfe_workshop --channel conda-forge --file conda-requirements.txt --yes
	source activate mfe_workshop && \
	pip install -r requirements.txt
	echo Run "source activate mfe_workshop" activate the conda environment

test:
	pytest src/production_code