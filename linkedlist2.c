#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<conio.h>
struct node
{
	int data;
	struct node *next;
}*start=NULL,*temp,*newnode,*t,*temp1,*cnode,*nnode,*pnode;
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
int search()
{
	temp=start;
	int loc=0,data;
	printf("\nenter data to search:\n");
	scanf("%d",&data);
	if(temp==NULL)
	{
		printf("list is empty:\n");
	}
	else
	{
		printf("\ndata is stored in position no:");
		while(temp!=NULL)
		{
			loc=loc+1;
			if(data==temp->data)
			{
				printf(" %d\n",loc);
			}
			temp=temp->next;
		}
	}
}
void reverse()
{
    cnode=start;
    nnode=cnode->next;
    cnode->next=NULL;
    while(nnode!=NULL)
    {
		pnode=cnode;
		cnode=nnode;
		nnode=nnode->next;
		cnode->next=pnode;
	}
	start=cnode;
	
}
void show()
{
	t=start;
	while(t!=NULL)
	{
		printf("%d->",t->data);
		t=t->next;
	}
	printf("NULL");
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
	while(1)
	{
		printf("\n\nenter your choice:\n");
		printf("1.searching:\n");
		printf("2.reverse:\n");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:
				search();
				break;
			case 2:
				reverse();
            	show();
				
		}
	}
	getch();
}
