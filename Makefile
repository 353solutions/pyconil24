default:
	$(error please pick a target)

proto:
	python -m grpc_tools.protoc \
		-I . \
		--python_out=. \
		--grpc_python_out=. \
		unter.proto

env:
	test -d .venv || python -m venv .venv
	./.venv/bin/python -m pip install .
	rm -rf build unter.egg-info/
