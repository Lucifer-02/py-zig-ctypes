run:
	zig build-lib module.zig -dynamic -target native
	python3 test.py
