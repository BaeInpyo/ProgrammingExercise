class Solution {
public:
    bool is_valid(int x, int y, int height, int width) {
        return (x >= 0 && x < height && y >= 0 && y < width);
    }
    
    int islandPerimeter(vector<vector<int>>& grid) {
        int perimeter = 0;
        int height = grid.size();
        int width = grid[0].size();
        vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                if (!grid[i][j]) continue;
                
                for (auto dir : directions) {
                    int x = i + dir.first;
                    int y = j + dir.second;
                    if (!is_valid(x, y, height, width) || !grid[x][y]) {
                        ++perimeter;
                    }
                }
            }
        }
        return perimeter;
    }
};
