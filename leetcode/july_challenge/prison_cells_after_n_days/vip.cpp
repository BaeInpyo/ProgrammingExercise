class Solution {
public:
    int encode(vector<int>& cells) {
        int ret = 0;
        for (int cell : cells) {
            ret <<= 1;
            ret += cell;
        }
        return ret;
    }
    
    vector<int> decode(int num) {
        vector<int> result(8, 0);
        int index = 8;
        while (num > 0) {
            result[--index] = num % 2;
            num >>= 1;
        }
        return result;
    }
    
    vector<int> get_next(vector<int> &cells) {
        vector<int> next(8, 0);
        next[0] = 0;
        for (int i = 1; i < 7; ++i) {
            if (cells[i-1] == cells[i+1]) next[i] = 1;
            else next[i] = 0;
        }
        next[7] = 0;
        return next;
    }
    
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        vector<int> next(256, -1);
        vector<int> nth(256, -1);
        int day = 0;
        int curr_state = encode(cells);
        int prev_state;
        vector<int> next_cells = cells;
        while (nth[curr_state] == -1) {
            next_cells = get_next(next_cells);
            nth[curr_state] = day++;
            prev_state = curr_state;
            curr_state = encode(next_cells);
            next[prev_state] = curr_state;
        }
        
        int start = nth[curr_state];
        int end = nth[prev_state];
        if (N <= end) {
            prev_state = encode(cells);
        } else if (N > end) {
            if (start == 0) N += 1;
            N %= (end - start + 1);
            if (N == 0) {
                return decode(prev_state);
            }
        }
        
        int result = prev_state;
        while (--N >= 0) {
            result = next[result];
        }
        return decode(result);
    }
};
