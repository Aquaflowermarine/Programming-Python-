#include <iostream>
using namespace std;
int main(){
    int num;
    cout<<"알고 싶은 단수를 입력하세요 : ";
    cin>>num;
    for(int i = 1; i >=9; i++){
        cout << num <<" * "<<i<<" = "<<num*i<<endl;
    }
    return 0;
}