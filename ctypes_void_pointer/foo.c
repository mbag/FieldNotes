#include<stdlib.h>
#include "foo.h"


int set_values_foobar(int value, FOOBAR *foobar_p){
    
    int *x = malloc(value * sizeof(int));
    int i = 0;
    foobar_p->count = value;
    
    for (i=0; i < value; i++) {
        x[i] = i;
    }
    foobar_p->void_pointer = x;
    
    
    return 0;
}
