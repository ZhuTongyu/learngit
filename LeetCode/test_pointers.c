#include<stdio.h>
int main(void)
{
	int zippo[4][2] = { {2,4},{6,8},{1,3},{5,7} };
	printf("zippo= %p, zippo+1 = %p\n", zippo, zippo + 1);  // 1

	printf("zippo[0]=%p,zippo[0]+1=%p\n", zippo[0], zippo[0] + 1); // 2
		
	printf("*zippo= %p, *zippo+1 = %p\n", *zippo, *zippo + 1);  // 3

	printf("zippo[0][0]=%d\n", zippo[0][0]); // 4

	printf(" *zippo[0]=%d\n", *zippo[0]); // 5

	printf("  **zippo=%d\n", **zippo); // 6

	printf("zippo[2][1]=%d\n", zippo[2][1]); // 7

	printf("*(*(zippo+2)+1)=%d\n", *(*(zippo + 2) + 1));  // 8 || zippo = &zippo[0]
	// zippo = &zippo[0]; zippo+2=&zippo[2]; *(zippo+2)=zippo[2]=&zippo[2][0];
	// *(zippo+2)+1 = &zippo[2][1] ;    *(*(zippo+2)+1)==zippo[2][1]

	return 0;

}