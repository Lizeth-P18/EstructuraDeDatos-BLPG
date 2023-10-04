#include<iostream>
using namespace std;
const int NUM = 8;
int main()
{
	int nums[NUM];
	int total = 0;
	for (int i = 0; i < NUM; i++)
	{
		cout << "Por favor introdusca el numero: ";
		cin >> nums[i];
		total += nums[i];
	}
	cout << "El total del numero es:" << total << endl;
	return 0;
}