#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int factorial(int n)
{
  //5! = 5 * 4 * 3 * 2 * 1
  int sum = 1;
  for(int i = 1; i <= n; i++)
  {
    sum *= i;
  }

  return sum;
}

int main(int argc, char * argv[])
{
  int x = (int)'D'-(int)'A';

  printf("%d",x);

  return 0;
}
