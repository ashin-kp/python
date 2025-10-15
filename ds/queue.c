#include<stdio.h>
# define size 5
int queue[size],rear=-1,front=-1;
void enqueue(int val)
{
    if(rear==size-1)
    {
        printf("\nQueue is full");
    }
    else
    {
        if(front==-1)
        {
            front=0;        }
        rear++;
        queue[rear]=val;
        printf("\nElement inserted=%d",val);
    }
}
void dequeue()
{  
    if(front==-1||front>rear)
    {
        printf("\nQueue is empty");

    }
    else{
         
     int item=queue[front];
     front++;
     printf("\npopped item=%d",item);


    } 
}
void display()
{
    if(front==-1 || front>rear)
    {
        printf("Queue is empty");
    }
    else{
        printf("\nElements in queue are:");
        for(int i=front;i<=rear;i++)
        {
            printf("%d\t",queue[i]);
        }
        
    }
}
int main()
{
   int choice,elem;
   char ch;
   printf("select the operation:");
   printf("\n1.enqueue \n2.dequeue \n3.display");
   scanf("%d",&choice);
   do
   {
    switch(choice)
    {
        case 1: printf("Enter the element to be inserted=");
                scanf("%d",&elem);
                enqueue(elem);
                break;
        case 2: dequeue();
                break;
        case 3: display();
                break;
        default: printf("invalid input");
                break;
                
    }
    printf("Do you want to continue Y OR N:");
    scanf(" %c",&ch);
   } while(ch=='y'||ch=='Y');
   return 0;
   

}