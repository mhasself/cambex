ifneq ($(wildcard Makefile.local),)
include Makefile.local
endif

ifneq ($(PREFIX),)
install_args = --prefix=$(PREFIX)
endif

default: .build

.build:
	python setup.py build

install:
	python setup.py install $(install_args)

clean:
	-python setup.py clean
	-rm -r build
