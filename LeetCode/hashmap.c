#include <stdio.h>
#include <stdlib.h>

#define SIZE 20;

typedef struct NodeData {
	int data;
	int key;
} NodeData;

struct NodeData *hashArray[SIZE];