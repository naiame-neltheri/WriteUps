
	#include <stdio.h>
	unsigned char code[] = "\xeb\x4d\x5e\x66\x83\xec\x0c\x48\x89\xe0\x48\x31\xc9\x68\xdd\x76\xc6\x2b\x48\x89\xcf\x80\xc1\x0c\x40\x8a\x3e\x40\xf6\xd7\x40\x88\x38\x48\xff\xc6\x68\xe9\xaf\x56\xa6\x48\xff\xc0\xe2\xea\x2c\x0c\x48\x89\xc6\x68\xd5\xd8\x9f\x85\x48\x31\xc0\x48\x89\xc7\x04\x01\x48\x89\xc2\x80\xc2\x0b\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xae\xff\xff\xff\x99\xa6\xcf\x95\xb8\xb4\xb6\x97\x8a\x89\xb6\x8e\x9b\x1b\x5f\xef\xcd\xf7\xc1\x94\xb8\x5e\x23\x0e\xf7\xc5\x61\xce\xa6\x68\xe3\xd0\xbb\x8f\x5b\x52\x41\x4e\x44\x53\x54\x52\x32\x5d";
	int main(int argc, char **argv){
		int foo_value = 0;
		int (*foo)() = (int(*)())code;
		foo_value = foo();
	}
	