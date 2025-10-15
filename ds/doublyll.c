#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
    struct node *prev;
};
struct node *head=NULL;
//create new node
struct node *create(int elem)
{  
     struct node *newnode=(struct node*)malloc(sizeof(struct node));
     if(newnode==NULL)
     {
        printf("\nMemory allocation failed");
     }
     newnode->data=elem;
     newnode->next=NULL;
     newnode->prev=NULL;
     return newnode;

}
//insert at beginning
void insertatbeg(int elem)
{
    struct node *newnode=create(elem);
    if(head==NULL)
    {
        head=newnode;
        newnode->prev=head;
        newnode->next=NULL;
    }
    else{
    newnode->next=head;
    head=newnode;
    newnode->prev=head;
    }
    printf("Element inserted at begining=%d",newnode->data);
}
//insert at end
void inseratend(int elem)
{
    struct node *newnode=create(elem);
    struct node *temp=head;
    if(head==NULL)
    {
        head=newnode;
        newnode->prev=head;
    }

    while(temp!=NULL)
    {
      temp=temp->next;
    }
    temp=newnode;
    newnode->prev=temp;
    newnode->next=NULL;
    printf("\nElements inserted %d=",temp->data);
}
void display()
{
    struct node *temp=head;
    if(temp==NULL)
    {
        printf("\nDoubly linked list is empty");
        return;
    }
    printf("Elements in doubly linked list=");

    while(temp!=NULL)
    {
        printf("\n%d",temp->data);
        temp=temp->next;
    }

}
int main()
{
    int elem,choice;
    char ch;
    do
    {
      printf("\nEnter the operation:");
      printf("\n1.insertion at begining\n2.insertion at end\n3.Display");
      scanf("%d",&choice);
      switch(choice)
      {
        case 1:printf("\nEnter the element to be inserted=");
               scanf("%d",&elem);
               insertatbeg(elem);
               break;
        case 2:printf("\nEnter the element to be inserted=");
               scanf("%d",&elem);
               inseratend(elem);
               break;
        case 3:display();
               break;
        default:printf("\n Invalid operation");
      }
      printf("\n Do you want to continue y or n=");
      scanf(" %c",&ch);
    }while(ch=='y'||ch=='Y');
return 0;
}