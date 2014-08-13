#include<stdio.h>

long long cnt = 0;
int size = 0;

void merge(long long arr[], int min, int mid, int max)
{
  long long tmp[size];
  int i,j,k,m; 
  j=min;
  m=mid+1;
  for(i=min; j<=mid && m<=max ; i++)
  {
     if(arr[j]<=arr[m])
     {
         tmp[i]=arr[j];
         j++;
     }
     else
     {
         cnt += 1 * (mid+1-j);
         tmp[i]=arr[m];
         m++;
     }
  }
  if(j>mid)
  {
     for(k=m; k<=max; k++)
     {
         tmp[i]=arr[k];
         i++;
     }
  }
  else
  {
     for(k=j; k<=mid; k++)
     {
        tmp[i]=arr[k];
        i++;
     }
  }
  for(k=min; k<=max; k++)
     arr[k]=tmp[k];
}

void part(long long arr[], int min, int max)
{
 int mid;
 if(min<max)
 {
   mid=(min+max)/2;
   part(arr,min,mid);
   part(arr,mid+1,max);
   merge(arr,min,mid,max);
 }
}

int main()
{
 int i,t;

 scanf("%d", &t);

 while (t--) {
   scanf("%d",&size);
   long long arr[size];
   for(i=0; i<size; i++)
   {
     scanf("%lld",&arr[i]);
   }
   cnt = 0;
   part(arr,0,size-1);
   printf("%lld\n",cnt);
 }

 return 0;
}