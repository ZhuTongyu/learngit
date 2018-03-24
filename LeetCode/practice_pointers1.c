//指向多维数组的指针，通过一个指针变量获取有关zippo的值
#include<stdio.h>

int main()
{
	int zippo[4][2] = { { 2,4 },{ 6,8 },{ 1,3 },{ 5,7 } };
	int(*pz)[2];
	pz = zippo; // pz 必须指向一个包含两个int值的数组

	printf("pz = %p,pz+1=%p\n", pz, pz + 1); // 1

	printf("pz[0]=%p,pz[0]+1=%p\n", pz[0], pz[0] + 1);// 2

	printf("*pz=%p,*pz+1=%p\n", *pz, *pz + 1); // 3

	printf("pz[0][0]=%d\n", pz[0][0]); // 4

	printf("*pz[0]= %d\n", *pz[0]); // 5

	printf("**pz=%d\n", **pz); // 6

	printf("pz[2][1]=%d\n", pz[2][1]); // 7

	printf("*(*(pz+2)+1)=%d\n", *(*(zippo + 2) + 1)); // 8


}