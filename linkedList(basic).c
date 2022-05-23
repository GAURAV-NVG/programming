// linkedlist creation by gaurav nv

//o/p 10 20

#include <stdio.h>
#include <stdlib.h> // used for using malloc

//node structure
struct node{
    int data;
    struct node *next;
};

struct node *head = NULL;
int main()
{
    head = malloc(sizeof(struct node));
    head->data = 10;
 
    //second node creation   
    struct node *secondNode = NULL;
    secondNode = malloc(sizeof(struct node));
    secondNode->data = 20;
    secondNode->next = NULL;
    head->next = secondNode; // changing next pointer of first node from NULL
                            //to address of next node
    
    //traversing
    
    struct node *ptr = head;
    while(ptr!=NULL){
        printf("%d ",ptr->data);
        ptr = ptr->next;
    }
    
}
