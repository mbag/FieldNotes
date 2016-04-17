CC=gcc

SO_FLAGS=-fPIC -shared

libfoo.so: foo.c foo.h
	${CC} ${SO_FLAGS} foo.c -o libfoo.so

all: libfoo.so

clean:
	rm libfoo.so 
