#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <time.h>
#define SIZE 53 //Length of the lines divided by four(number of line in section)
using namespace std;
class Queplet
{
public:
	std::string one;
	std::string two;
	std::string three;
	std::string four;
};

int main()
{
	//Init srand
	srand ( time(NULL) );
	Queplet queplet[SIZE];
	std::string line;
	std::fstream myFile;

	myFile.open("data.txt");

	//Assing values from the line
	int i = 0;
	string linebuffer;
	while (getline(myFile, line)){
		queplet[i].one = line;
		getline(myFile, line);
		queplet[i].two = line;
		getline(myFile, line);
		queplet[i].three = line;
		getline(myFile, line);
		queplet[i].four = line;
		i++;
	}
		//Print to terminal and to file
		ofstream output;
		output.open ("FileOne.txt");
		for(int i = 0; i< 4; i ++)
		{
			int num1 = rand() % SIZE;

			int num2 = rand() % SIZE;
			
			output << queplet[num1].one << endl;
			output << queplet[num2].two << endl;
			output << queplet[num1].three << endl;
			output << queplet[num2].four << endl;
			output << endl;

			
		}	
		output.close();
		

	return 0;
}
