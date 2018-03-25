#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool isToeplitzMatrix(int** matrix, int matrixRowSize, int *matrixColSizes) {
	int i = 1, j = 1;
	for (i = 1; i < matrixRowSize; i++) {
		for (j = 1; j < (sizeof(matrixColSizes) / sizeof(matrixColSizes[0])); j++) {
			if (matrix[i][j] != matrix[i - 1][j - 1])
				return false;
		}
	}
	return true;
}
int main()
{
	int num[3][4] = { { 1, 2, 3, 4 },{ 5, 1, 2, 3 },{ 9, 5, 1, 2 } };
	bool result=false;
	int *a[3] = { num[0],num[1],num[2] };

	//int * matrixColSizes =
	result = isToeplitzMatrix(a, 3, num[0]);
	printf("%s\n", result);
	//return 0;
}