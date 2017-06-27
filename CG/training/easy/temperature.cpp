#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
    int result = 5526;
    int n;
    cin >> n;
    
    vector<int> temps;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        temps.push_back(t);
    }
    
    if(n == 0) {
        result = 0;
    } else {
        for(int i = 0; i < temps.size(); i++) {
            int t = temps[i];
            if(abs(t) < abs(result)) {
                result = t;
            } else if (abs(t) == abs(result)) {
                result = max(t, result);
            }
        }
    }
    
    cout << result << endl;
    
    return 0;
}