#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome(int x) {
	if (x == 0) {
		return true;
	}
	else if (x < 0) {
		return false;
	}
	int rawx = x;
	printf("[*] Entry point value : %d\n", x);
	uint reverse = 0;
	int leftover;
	while (x > 0) {
		printf("[*] DIVIDING : %d to 10\n", x);
		leftover = x % 10;
		x = x / 10;
		reverse = reverse * 10 + leftover;
		printf("[*] LEFT : %d\n[*] X : %d\n[*] REVERSE: %d\n", leftover, x, reverse);
	}
	printf("[*] Comparing : %d to %d\n", reverse, rawx);
	if (reverse == rawx) {
		return true;
	}
	else {
		return false;
	}
}

int main(int argc, char *argv[]) {
	printf("[+] There is total of %d arguments in the command line.\n[+] Arguments are : ", (argc - 1));
	for (int i=1; i < argc; i++) {
		if (i == (argc - 1)) {
			printf("%s\n", argv[i]);
		}
		else {
			printf("%s, ", argv[i]);
		}
	}
	int result;
	for (int i=1; i < argc; i++) {
		char *ptr;
		long converted = strtol(argv[i], &ptr, 10);
		result = isPalindrome((int) converted);
		if (result) {
			printf("[+] Result is TRUE\n");
		}
		else {
			printf("[+] Result is FALSE\n");
		}
	}
	return 0;
}