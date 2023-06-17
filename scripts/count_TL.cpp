#include<iostream>
#include<fstream>
#include<string>

using namespace std;

"""
학습시킬 때, 신호등 색의 비율을 맞추기 위한 코드입니다.
신호등 색깔 인식 (R, O, G, LR, LO, LG)의 개수를 추출합니다.
"""

int main(int argc, char** argv) {
	ifstream FILE;
	
	char tmp;
	int ret[6] = { 0 };
	int src = stoi(argv[1]);
	int dst = stoi(argv[2]);
	int i = 0;
	int total = 0;
	while (1) {
		string file_name;
		file_name = "./2022_incheon_" + string(argv[3]) + "/labels/";
		if (stoi(argv[4])==1)	file_name += "2022_camera_4_";
		file_name += to_string(src);
		file_name += ".txt";
		tmp = NULL;
		FILE.open(file_name);
		FILE.get(tmp);
		if (tmp!=NULL){
			int tmp_num = tmp - 48;
			ret[tmp_num]++;
			total++;
		}
		FILE.close();
		if (src == dst) {
			break;
		}
		src++;
		if (i<1) cout << "path :" << file_name << endl;
		i++;
	}

	cout << "R  :" << ret[0] << endl;
	cout << "O  :" << ret[1] << endl;
	cout << "G  :" << ret[2] << endl;
	cout << "LR :" << ret[3] << endl;
	cout << "LO :" << ret[4] << endl;
	cout << "LG :" << ret[5] << endl;
	cout << "total :" << total << endl;


	return 0;
}
