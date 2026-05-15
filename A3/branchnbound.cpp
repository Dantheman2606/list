#include <iostream>
#include <vector>
using namespace std;

class NQueensBnB {

    int N;

    vector<vector<int>> board;

    vector<int> cols;
    vector<int> diag1;
    vector<int> diag2;

public:

    NQueensBnB(int n) {

        N = n;

        board.resize(N, vector<int>(N, 0));

        cols.resize(N, 0);

        diag1.resize(2 * N - 1, 0);

        diag2.resize(2 * N - 1, 0);
    }

    bool solve(int row) {

        // All queens placed
        if (row == N)
            return true;

        for (int col = 0; col < N; col++) {

            int d1 = row - col + N - 1;
            int d2 = row + col;

            // Check if safe
            if (!cols[col] &&
                !diag1[d1] &&
                !diag2[d2]) {

                // Place queen
                board[row][col] = 1;

                cols[col] = 1;
                diag1[d1] = 1;
                diag2[d2] = 1;

                // Recur
                if (solve(row + 1))
                    return true;

                // Backtrack
                board[row][col] = 0;

                cols[col] = 0;
                diag1[d1] = 0;
                diag2[d2] = 0;
            }
        }

        return false;
    }

    void printBoard() {

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {

                if (board[i][j] == 1)
                    cout << "Q ";
                else
                    cout << ". ";
            }

            cout << endl;
        }
    }
};

int main() {

    int n;

    cout << "Enter value of N: ";
    cin >> n;

    NQueensBnB obj(n);

    if (obj.solve(0)) {

        cout << "\nSolution Exists:\n";

        obj.printBoard();
    }
    else {

        cout << "No Solution Exists";
    }

    return 0;
}