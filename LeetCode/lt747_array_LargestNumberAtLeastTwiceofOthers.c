#include<stdio.h>
#include<stdlib.h>

int dominantIndex(int* nums, int numsSize) {
	int i = 0;
	int max= INT_MIN, sedmax= INT_MIN,maxid;
	if (numsSize == 1) {
		return 0;
	}
	for (i = 0; i < numsSize; i++) {
		if (max < nums[i]) {
			sedmax = max;
			max = nums[i];
			maxid = i;	
		}
		else if(sedmax < nums[i]){
			sedmax = nums[i];
			
		}
	}
	if (sedmax * 2 <= max) {
		return maxid;
	}
	else {
		return -1;
	}

}

int main()
{
	int a[4] = { 1,0 };
	int output = 0;
	output = dominantIndex(a, 2);

	printf("%d\n", output);

	return 0;



}