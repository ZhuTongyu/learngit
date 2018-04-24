#include<stdio.h>
#include<stdlib.h>
// { -1,-1,1,1,1 }; sum=1
int pivotIndex(int* nums, int numsSize) 
{
	int i = 0;
	int sum = 0;
	int left = 0;
	//int count = 0;
	if (numsSize == 1)
		return 0;
	else{
		for (i = 0; i < numsSize; i++) {
			sum += nums[i];
		}
		for (i = 0; i < numsSize; i++) {
			//left += nums[i];
			
			if ((left * 2 + nums[i]) == sum) {
				return i;
			}
			left += nums[i];
			//count++;
		}
	}
	return -1;

}

int main()
{
	int a[] = { -1,-1,1,1,1 };
	//int a[] = { 1,2,3};
	int n = 5;
	int result;
	result = pivotIndex(a, n);
	printf("%d\n", result);
	return 0;
}