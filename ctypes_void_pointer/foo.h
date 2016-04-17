#ifndef __FOO_H
#define __FOO_H

typedef struct foobar {
    int count;
    void *void_pointer; 
} FOOBAR;

int set_values_foobar(int value, FOOBAR *foobar_p);


#endif /* __FOO_H */
