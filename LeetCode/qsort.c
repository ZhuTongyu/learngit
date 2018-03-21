#include<stdio.h>
#include<stdlib.h>
int cmp(const void* a, const void* b) {
	return(*(int*)a - *(int*)b);
}
// return(*(int *)b-*(int *)a); 
// return((*(double*)a - *(double*)b>0) ? 1 : -1);
// return(*(char *)a-*(char *)b); 
int main()
{
	int a[] = { 3,1,4,1,5 };
	int n = 5;
	int k = 2;
	int i = 0;
	qsort(a, n, sizeof(a[0]), cmp);
	for (i = 0; i < n; i++) {
		printf("%d ", a[i]);

	}
	printf("\n");

}