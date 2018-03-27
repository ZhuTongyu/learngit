#include<stdio.h>
int main()
{
	int a[2][4] = { {2,5,6,8},{22,55,66,88} };
	int c[4] = { 5,8,9,4 };
	int d[3] = { 23,12,443 };
	int e[4] = { 1,2,3,4 };
	int *p[4], (*q)[4];
	q = a;
	*p = c;
	*(p + 1) = d;
	*(p + 2) = e;
	int i, j;
	/*for (i = 0; i < 3; i++) {
		for (j = 0; j < 4; j++) {
			//if (i == 1 && j == 3) break;
			printf("(*(p+%d)+%d) = %d\n", i, j, *(*(p + i) + j)); // *p row address
			//printf("(*(p+%d)+%d) = %d\n", i, j, p[i][j]);
		}
	}*/

	puts("====================");
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			//printf("*(*(q+%d)+%d)=%d\n", i, j, *(*(q + i) + j));
			printf("*(*(q+%d)+%d)=%d\n", i, j, q[i][j]);
		}
	}
	puts("====================");


}