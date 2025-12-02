#include <bits/stdc++.h>

using namespace std;

int main() {

  int ifinal, jfinal;
  int c[5][5];

  for(int i = 0; i < 5; i++){
    for (int j = 0; j < 5; j++){
        cin >> c[i][j];
        if (c[i][j] == 1){
          ifinal = i;
          jfinal = j;
          break;
        }
    }
  }

  int x = abs(ifinal - 2);
  int y = abs(jfinal - 2);

  cout << x + y;

  return 0;
}
