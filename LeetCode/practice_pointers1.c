//ָ���ά�����ָ�룬ͨ��һ��ָ�������ȡ�й�zippo��ֵ
#include<stdio.h>

int main()
{
	int zippo[4][2] = { { 2,4 },{ 6,8 },{ 1,3 },{ 5,7 } };
	int(*pz)[2];
	pz = zippo; // pz ����ָ��һ����������intֵ������

	printf("pz = %p,pz+1=%p\n", pz, pz + 1); // 1

	printf("pz[0]=%p,pz[0]+1=%p\n", pz[0], pz[0] + 1);// 2

	printf("*pz=%p,*pz+1=%p\n", *pz, *pz + 1); // 3

	printf("pz[0][0]=%d\n", pz[0][0]); // 4

	printf("*pz[0]= %d\n", *pz[0]); // 5

	printf("**pz=%d\n", **pz); // 6

	printf("pz[2][1]=%d\n", pz[2][1]); // 7

	printf("*(*(pz+2)+1)=%d\n", *(*(zippo + 2) + 1)); // 8


}