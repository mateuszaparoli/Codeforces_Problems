#include <bits/stdc++.h>

using namespace std;

int main(){
  int n, m; cin >> m >> n;

  int mul = n * m;
  if (!(mul%2)) {
    cout << mul/2;
  } else {
    cout << (mul-1)/2;
  }
  return 0;
}
