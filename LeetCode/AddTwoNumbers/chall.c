#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct ListNode {
	unsigned int val;
	struct ListNode *next;
} ListNode;

void addNode(int value, ListNode *curr) {
	ListNode *new = (ListNode *) malloc(sizeof(struct ListNode));
	new->val = value;
	new->next = NULL;
	while (curr->next) {
		curr = curr->next;
	}
	curr->next = new;
}

struct ListNode *addAtHead(ListNode *curr, int val) {
	ListNode *new = (ListNode *) malloc(sizeof(struct ListNode));
	new->val = val;
	new->next = curr;
	return new;
}

void iterateAllNode(ListNode *curr) {
	printf("[+] Iterator\n");
	unsigned int counter = 0;
	while(curr) {
		printf("[+] Index of %d value is %d\n", counter, curr->val);
		curr = curr->next;
		counter += 1;
	}
	printf("[+] End of Iterator\n");
}

unsigned int reverse(ListNode *curr) {
	unsigned int counter = 0, ret = 0;
	while(curr) {
		if (counter == 0) {
			ret = curr->val;
		}
		else {
			ret = ((pow(10, counter)) * curr->val) + ret;
		}
		counter += 1;
		curr = curr->next;
	}
	printf("[+] Result is : %d\n", ret);
	return ret;
}

struct ListNode *char2struct(char *inp) {
	// CONVERT COMMAND LINE ARGUMENT INTO CHAR ARRAY FOR ADDING TO STRUCT CHAR BY CHAR
	int cnt = 0;
	for (cnt; inp[cnt] != '\0'; cnt++);
	char tmpInp[cnt];
	strncpy(tmpInp, inp, cnt);

	// CONVERT ARGUMENT INTO LINKED LIST
	ListNode *new = (ListNode *) malloc(sizeof(struct ListNode));
	new->val = (int) (tmpInp[0] - '0');
	for(int i=1 ; i < sizeof(tmpInp); i++) {
		addNode((int)(tmpInp[i] - '0'), new);
	}
	return new;
}

int main(int argc, char *argv[]) {
	if (argc <= 1) {
		printf("[+] Not enough arguments\n[+] Usage chall <NUMBERS SEPERATED BY SPACE>\n");
		exit(1);
	}
	unsigned int listsCounter = 0;
	ListNode *lists[argc - 1], *nodeResult;
	for (int i = 1; i < argc; i++) {
		lists[listsCounter] = char2struct(argv[i]);
		listsCounter += 1;
	}
	unsigned int result = 0;
	unsigned int counter = 0;
	for (int i=0 ; i < listsCounter; i++) {
		iterateAllNode(lists[i]);
		result += reverse(lists[i]);
	}
	printf("[+] Sum is : %d\n", result);
	unsigned int divider = result, cnt = 0;
	while(divider) {
		divider = divider / 10;
		cnt += 1;
	}
	printf("[+] Converting result integer to char array\n");
	char res[cnt + 1];
	char *ptr = res;
	snprintf(res,cnt + 1, "%d", result);
	printf("[+] Converting char array to linked list\n");
	ListNode *final;
	nodeResult = char2struct(ptr);
	printf("[+] Reversing linked list\n");
	while(nodeResult) {
		final = addAtHead(final, nodeResult->val);
		nodeResult = nodeResult->next;
	}
	iterateAllNode(final);
	printf("[+] Challenge done\n");
}