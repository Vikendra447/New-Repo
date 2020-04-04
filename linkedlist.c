#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<conio.h>
struct node
{
	int data;
	struct node *next;
}*start=NULL,*temp,*newnode,*t,*temp1;
int create()
{
	int i,d;
	scanf("%d",&d);
	temp=(struct node*)malloc(sizeof(struct node));
	temp->next=NULL;
	temp->data=d;
	if(start==NULL)
	{
		start=temp;
	}
	else
	{
		temp=start;
		while(temp->next!=NULL)
		{
		    temp=temp->next;
		}
		newnode=(struct node*)malloc(sizeof(struct node));
	    newnode->data=d;
	    newnode->next=NULL;
	    temp->next=newnode;
		}
}
int insertbig()
{
	int d;
	printf("\nenter data to insert in begining:\n");
	scanf("%d",&d);
	newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=d;
	newnode->next=start;
	start=newnode;
}
void insertend()
{
	int d;
	temp=start;
	printf("\nenter data to insert at the end\n");
	scanf("%d",&d);
	while(temp->next!=NULL)
	{
		temp=temp->next;
	}
	newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=d;
	newnode->next=NULL;
	temp->next=newnode;
}
void insertspec()
{
	int p,d,i;
	temp=start;
	printf("\nenter position to insert data:\n");
	scanf("%d",&p);
	printf("enter data to insert:\n");
	scanf("%d",&d);
	for(i=1;i<p-1;i++)
	{
		temp=temp->next;
	}
	newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=d;
	newnode->next=temp->next;
	temp->next=newnode;
}
void deletebig()
{
	temp=start;
	if(temp==NULL)
	{
		printf("list is empty:\n");
	}
	else
	{
	    start=temp->next;
	    free(temp);
    }
}
void deleteend()
{
	temp=start;
	if(temp==NULL)
	{
		printf("list is full:\n");
	}
	else
	{
		while(temp->next!=NULL)
		{
			temp1=temp;
			temp=temp->next;
		}
		temp1->next=NULL;
		free(temp);
	}
}
void deletespec()
{
	temp=start;
	int p,i;
	if(temp==NULL && temp->next==NULL)
	{
		printf("list is empty:\n");
	}
	else
	{
	printf("enter position to delete:\n");
	scanf("%d",&p);
	for(i=1;i<p-1;i++)
	{
	     temp=temp->next;
	}
	temp1=temp->next;
	temp->next=temp1->next;
	free(temp1);
	}
}
void show()
{
	t=start;
	while(t!=NULL)
	{
		printf("%d->",t->data);
		t=t->next;
	}
	printf("NULL\n");
}
int main()
{
	int i,n,ch,op;
	printf("enter size of your list:\n");
	scanf("%d",&n);
	printf("enter data to create list\n");
	for(i=0;i<n;i++)
	{
		create();
	}
	printf("\nstarting list is\n");
	show();
	printf("\nenter your option:");
	printf("\n1.insertion:");
	printf("\n2.deletion:\n");
	scanf("%d",&op);
	if(op==1)
	{
	while(1)
	{
		printf("\nwhat u want:\n");
		printf("1.insert at begining:\n");
		printf("2.insert at end:\n");
		printf("3.insert at specified position:\n");
		printf("\nenter your choice:\n");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:
				insertbig();
	            printf("after insertion at biging list is\n");
	            show();
	            break;
	        case 2:
				insertend();
            	printf("\nafter insertion at the end list is\n");
            	show();
            	break;
            case 3:
				insertspec();
	            printf("\nafter insertion in the specified location list is\n");
            	show();
            	break;
		}
		
     }
	 }
	 if(op==2)
	{
	while(1)
	{
		printf("what u want:\n");
		printf("1.delete at begining:\n");
		printf("2.delete at end:\n");
		printf("3.delete at specified position:\n");
		printf("\nenter your choice:\n");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:
				deletebig();
	            printf("after deletion at biging list is\n");
	            show();
	            break;
	        case 2:
				deleteend();
            	printf("\nafter deletion at the end list is\n");
            	show();
            	break;
            case 3:
				deletespec();
	            printf("\nafter deletion at the specified location list is\n");
            	show();
            	break;
		}
		
     }
	 }
	getch();
}
