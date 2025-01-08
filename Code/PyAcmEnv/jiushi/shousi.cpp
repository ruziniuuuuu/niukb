#include <bits/stdc++.h>
using namespace std;

std::string  encode(std::string  s, int n) {
  //fill your code here
  vector<string> a(n, "");
  int len = s.length();

  int d = 1;
  for (int i = 0, j = 0; i < len; i++) {
    if (j == 0) d = 1;
    if (j == n - 1) d = -1;
    a[j] += s[i];
    j += d;
  }

  string encoded_s = "";
  
  for (int i = 0; i < n; i++) {
    encoded_s += a[i];
  }
    
  return encoded_s;
}

std::string  decode(std::string  s, int n) {
  //fill your code here
  vector<string> a(n, "");
  int len = s.length();

  string decoded_s("0", len);

  int cycle = 2 * n - 2;
  int j = 0;
  for (int i = 0; i < len; i ++) {
    int k = i / cycle;
    int m = i % cycle;
    if (k == 0) {
      // first track
      decoded_s[m] = s[i];
    } else
    if (k == n) {
      // last track
      decoded_s[k * cycle + m] = s[i];
    } else {
      // middle tracks
      if (m < n) {
        // first middle
        decoded_s[k * cycle + m] = s[i];
      } else {
        // second middle
        decoded_s[(k + 1) * cycle - (cycle - m)] = s[i];
      }
    }
  }
    
  return decoded_s;
}
