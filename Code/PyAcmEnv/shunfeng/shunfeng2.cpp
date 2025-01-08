// 对于一个3*3的矩阵，小明可以在每一个格子中填上0到3之间的任何一个数。
// 给数6个约束。
// 前三个数a_1, a_2, a_3代表每一行异或和为a_1, 第二行异或和为a_2, 第三行异或和为a_3。
// 后三个数a_4, a_5, a_6代表每一列异或和a_4, 第二列异或和a_5, 第三列异或和a_6。
// 求有多少种填法使得以上约束至少满足k个。

// 输入描述：
// 一行给出6个数a_i(0 <= a_i <= 7)。
// 第二行给出一个数k(1 <= k <= 6)

// 输出描述：
// 输出一行一个数代表答案。

// 样例输入：
// 3 2 1 0 1 1 
// 6

// 样例输出：
// 256

#include <iostream>
#include <vector>
using namespace std;

int count_all = 0;

bool check(vector<vector<int>>& matrix, vector<int>& rowSum, vector<int>& colSum)
{
    int count = 0;
    // row constraint
    for (int i = 0; i < 3; i ++) {
        int sum = 0;
        for (int j = 0; j < 3; j ++) {
            sum ^= matrix[i][j];
        }
        if (sum == rowSum[i]) count++;
    }
    // col constraint
    for (int i = 0; i < 3; i ++) {
        int sum = 0;
        for (int j = 0; j < 3; j ++) {
            sum ^= matrix[j][i];
        }
        if (sum == colSum[i]) count++;
    }
    return count;
}

void solve(vector<vector<int>>& matrix, vector<int>& rowSum, vector<int>& colSum, int k, int row, int col)
{
    if (row == 3) {
        if (check(matrix, rowSum, colSum) >= k) {
            count_all++;
        }
        return;
    }
    if (col == 3) {
        solve(matrix, rowSum, colSum, k, row, 0);
        return;
    }
    for (int num = 0; num < 4; num++) {
        matrix[row][col] = num;
        solve(matrix, rowSum, colSum, k, row, col + 1);
        matrix[row][col] = 0;
    }
}

int main() {
    vector<int> rowSum(3), colSum(3);
    cin >> rowSum[0] >> rowSum[1] >> rowSum[2] >> colSum[0] >> colSum[1] >> colSum[2];
    int k;
    cin >> k;

    vector<vector<int>> matrix(3, vector<int>(3, 0));
    solve(matrix, rowSum, colSum, k, 0, 0);
    cout << count_all << endl;
    return 0;
}