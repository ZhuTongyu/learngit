#include<stdio.h>
#define ROW 3
#define COL 4
// ！！！声明！！！此类函数参量的方法
// void somefunction(int (* pt)[4]);
// void somefunction(int pt[][4]); 当且仅当pt是函数的形式参量时，与上一行等价

void sum_rows(int ar[][COL], int rows);
//void sum_rows(int ar[][cols], int rows);
//void sum_cols(int[][cols], int); // can ignore name
//void sum2d(int(*ar)[cols], int rows); // these three Statement Method are equivalent

int main(void)
{
	int junk[ROW][COL] = {
		{2,4,6,8},
		{3,5,7,9},
		{12,10,8,6}
	};
	sum_rows(junk, ROW);

	return 0;
}
void sum_rows(int ar[][COL], int rows)
{
	int r;
	int c;
	int tot;
	for (r = 0; r < rows; r++)
	{
		tot = 0;
		for (c = 0; c < COL; c++)
			tot += ar[r][c];
		printf("row %d: sum = %d\n", r, tot);
	}


}

