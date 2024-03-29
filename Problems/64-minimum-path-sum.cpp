// https://leetcode.com/problems/minimum-path-sum

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int dist[m][n];
        dist[0][0] = grid[0][0];
        for (int i = 1; i != n; i++){
            dist[0][i] = dist[0][i-1] + grid[0][i];
        }
        for (int j = 1; j != m; j++){
            dist[j][0] = dist[j-1][0] + grid[j][0];
        }
        
        for (int i = 1; i != m; i++){
            for (int j = 1; j != n; j++){
                dist[i][j] = min(dist[i-1][j], dist[i][j-1]) + grid[i][j];
            }
        }
        
        return dist[m-1][n-1];
    }
};