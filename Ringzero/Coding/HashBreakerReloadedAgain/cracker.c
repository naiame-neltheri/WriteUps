#include <stdio.h>
#include <stdlib.h>

void help_print() {
	printf("[!] Invalid number of arguments\n[!] Usage : cracker [HASH STRING]\n");
}

void breaker(char *raw_hash) {
	printf("[+] Test : %s", raw_hash);
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		help_print();
		exit(1);
	}
	else {
		char *result;
		printf("[+] Given hash is : %s\n", argv[1]);
		breaker( argv[1]);
	}
	return 0;
}