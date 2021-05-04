#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool sanitize_input(char *buffer) {
	bool valid = true;
	int cnt = 0;
	while (buffer[cnt] != '\x00') {
		switch(buffer[cnt]) {
			case 'I' :
				break;
			case 'V' :
				break;
			case 'X' :
				break;
			case 'L' :
				break;
			case 'C' :
				break;
			case 'D' :
				break;
			case 'M' :
				break;
			default:
				valid = false;
		}
		cnt += 1;
	}
	return valid;
}

int converter(char *buffer) {
	int ret = 0, cnt = 0;
	while(buffer[cnt] != '\x00') {
		if (cnt == 0) {
			switch(buffer[cnt]) {
				case 'I' :
				if (buffer[cnt + 1] != '\x00') {
					switch(buffer[cnt + 1]) {
						case 'V':
							ret = 
					}
				}
			}
		}
	}
	return ret;
}

void main() {
	char buffer[100];
	char *ptr = buffer;
	printf("[+] Please enter roman number: ");
	scanf("%s", &buffer);
	printf("[+] Your input is %s\n", buffer);
	printf("[+] Checking if input contains correct characters.\n");
	if (!sanitize_input(ptr)) {
		printf("[+] Invalid character detected please try again.\n");
		exit(1);
	}
	else {
		printf("[+] Sanitize passed\n");
	}
}