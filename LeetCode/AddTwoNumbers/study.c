#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int data;
	struct Node *next;
} Node;

Node *headNode = NULL;
int nodeCounter = 0;

Node* nodeInit() {
	headNode = (struct Node*) malloc(sizeof(struct Node));
	headNode->data = 0;
	headNode->next = NULL;
}

int get(int index) {
	Node *curr = headNode;
	int counter = 0;
	while(curr) {
		if (counter == index) {
			return curr->data;
		}
		curr = curr->next;
		counter += 1;
	}
	return -1;
}

void addAtHead(/*Node **test ,*/int val) {
	// Node *newNode = (Node *) malloc(sizeof(Node));
	// newNode->data = val;
	// newNode->next = *headNode;
	// *headNode = newNode;
	// nodeCounter += 1;
	Node *newNode = (Node *) malloc(sizeof(Node));
	newNode->data = val;
	newNode->next = headNode;
	headNode = newNode;
	nodeCounter += 1;
}

void addAtTail(int val) {
	Node *newNode = (Node *) malloc(sizeof(Node));
	newNode->data = val;
	newNode->next = NULL;
	Node *currNode = headNode;
	while (currNode->next) {
		currNode = currNode->next;
	}
	currNode->next = newNode;
	nodeCounter += 1;
}

void addAtIndex(int index, int val) {
	Node *newNode = (Node *) malloc(sizeof(Node));
	newNode->data = val;
	newNode->next = NULL;
	Node *curr = headNode;
	int counter = 0;
	while (curr) {
		if ((counter + 1) == index) {
			newNode->next = curr->next;
			curr->next = newNode;
			break;
		}
		else {
			curr = curr->next;
		}
		counter += 1;
	}
}

void deleteAtIndex(int index) {
	int counter = 0;
	Node *curr = headNode;
	while (curr) {
		if ((counter + 1) == index) {
			Node *prev = curr;
			Node *next = NULL;
			curr = curr->next;
			next = curr->next;
			prev->next = next;
			free(curr);
			nodeCounter -= 1;
			break;
		}
		curr = curr->next;
	}
}

void printAll() {
	int counter = 0;
	Node *curr = headNode;
	printf("[+] Total number of NODE is : %d\n", nodeCounter);
	while (curr) {
		printf("[+] Value of index %d is : %d\n", counter, curr->data);
		curr = curr->next;
		counter += 1;
	}
}

int main(int argc, char *argv[]) {
	printf("[+] Naiame testing Linked List\n");
	printf("[+] Initializing struct\n");
	nodeInit();
	addAtHead(/*&headNode,*/5);
	addAtHead(15);
	addAtHead(20);
	addAtTail(1);
	addAtIndex(3,11);
	printAll();
	deleteAtIndex(0);
	printAll();
	return 0;
}
