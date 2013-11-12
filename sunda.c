#include <stdio.h>

#define N 1000000

int mas[N];

int main()
{
	int t = 0;
	int i = 0;
	int mas[N];
	
	for (i = 0; i < N; ++i)
	{
		//t += mas[i];
		mas[i] = 0;
	};

	printf("%d\n", t);

}