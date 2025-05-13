


The .pre-commit-config.yaml requires that you install the pre-commit python lib
> python -m pip install pre-commit

To set it up:
> pre-commit install

To check if its working or use it without really committing:
> pre-commit run --all-files

NOTE: when using pre-commit, know that it will run on the entire repo, not just the sub folder

