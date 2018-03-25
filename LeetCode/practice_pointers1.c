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

	int * pt;
	int(*pa)[3];
	int ar1[2][3];
	int ar2[3][2];
	int **p2; // 指向指针的指针

	p2 = ar2; // 非法 
	// p2是指向指针的指针，ar2是指向由2个int值构成的数组的指针(是指向int[2]的指针)。
	// 因此p2和ar2的类型不同，不能把ar2的值赋给p2
	pt = &ar1[0][0]; // 可以，都指向int
	*p2 = ar2[0]; // ar2[0]=&ar2[0][0]， ar2[0]是指向其首元素ar2[0][0]的指针
	//因此，ar2[0]是指向int的指针，*p2也是指向int的指针，所以合法。
	pa = ar1; //合法
	pa = ar2; //非法




}