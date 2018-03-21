#include<stdio.h>
#include<stdlib.h>
int cmp(const void* a, const void* b)
{
	return(*(int *)a - *(int *)b);
}

int main()
{
	int a[] = {0 };
	int n = 0;
	int k = 0;
	int i ,j;
	int count = 0;
	qsort(a, n, sizeof(a[0]), cmp);
	
	for (i = 0; i < n; i++) {
		j = i + 1;
		while (j < n && (a[j] - a[i]) < k) {
			j++;
		}
		if ((a[j] - a[i]) == k && j<numsSize) {
			count++;
		}
		while (i + 1 < n && a[i + 1] == a[i])
			i++;

	}


	printf("%d\n", count);
	return 0;
}