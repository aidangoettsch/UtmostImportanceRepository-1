#include <stdio.h>

int fib(int x) {
  int a = 0;
  int b = 1;
  
  for (int i = 1; i <= x; i++) {
    int temp = a;
    a = a + b;
    b = temp;
  }
  
  return a;
} 

int main() {
  printf("%d", fib(1000));
}
