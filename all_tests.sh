set -ex

python -m unittest
# this fixture was prepared to show how to use run_all/run_current_module; each file must be executed as separate process
python -m test_fixture.x
python -m test_fixture.y
python -m test_fixture.run_all