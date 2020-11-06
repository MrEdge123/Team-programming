from judgeModule.judge import submitCode

c_code = '''
#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\\n", a+b);
    return 0;
}
'''

cpp_code = '''
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
'''

python_code = '''
s = input().split()
print(int(s[0]) + int(s[1]))
'''

# submitCode("mredge", 0, c_code, "C")
# submitCode("mredge", 0, cpp_code, "C++")
submitCode("mredge", 0, python_code, "Python3")
