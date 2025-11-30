#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k; cin >> n >> k;
  int* v = (int*) malloc(n * sizeof(int));
  
  for (int i = 0; i < n; i++){
    cin >> v[i];
  }

  int minimun = v[k-1];

  int count = 0;
  for (int j = 0; j < n; j++){
    if( v[j] >= minimun && v[j] > 0) {
      count++;
    }
  }

  cout << count;

  return 0;
}
