#include <iostream>
#include <iomanip>
using namespace std;

char * Xor(char * in, int inSize, char * key, int keySize, char * out){
	for(int i=0; i<inSize; i++) {
		out[i] = in[i] ^ key[i % keySize];
	}
	return out;
}


void f2() {
    // char tab1[7] = "\x64\x0c\x0a\x02\x08\x18"; // "/ISIMA"
    // char tmp[10];
    // cout << Xor(tab1, 6, "KEY", 3, tmp) << endl;
    // cout << hex << 78 << quoted(Xor(tmp, 6, "KEY", 3, tmp)) << endl; // Faudrait reussir a afficher de l'hexa...

    char tab1[7] = "/ISIMA";
    char tmp[10];
    cout << hex << Xor(tab1, 6, "KEY", 3, tmp) << endl;
    cout << endl;
    cout << quoted(Xor(tab1, 6, "KEY", 3, tmp)) << endl;
    cout << endl;
    cout << hex << quoted(Xor(tab1, 6, "KEY", 3, tmp)) << endl;
}


void f1() {
    char tab1[24] = "\x12\x14\x07\x10\x07\x13\x1e\x66\x16\x14\x07\x12\x0f\x17\x13\x03\x15\x66\x0f\x15\x0f\x0b\x07"; // fAp7fV?^_hv.FA
    char tab2[24] = "\x61\x67\x74\x63\x74\x60\x6d\x15\x65\x67\x74\x61\x7c\x64\x60\x70\x66\x15\x7c\x66\x7c\x78\x74"; // TRAVAUX PRATIQUES ISIMA
    char tab3[24] = "\x12\x67\x07\x63\x07\x60\x1e\x15\x16\x67\x07\x61\x0f\x64\x13\x70\x15\x15\x0f\x66\x0f\x78\x07"; // TRAVAUX PRATIQUES ISIMA
    char tab4[24] = "\x0e\x08\x73\x09\x07\x60\x02\x7a\x62\x0d\x07\x61\x13\x0b\x67\x1a\x15\x15\x13\x09\x7b\x12\x07"; // TRAVAUX PRATIQUES ISIMA

    char tmp[24],tmp1[7];
    cout << Xor(tab1, 23, "F", 1, tmp) << endl;
    cout << Xor(tab2, 23, "5", 1, tmp) << endl;
    cout << Xor(tab3, 23, "F5", 2, tmp) << endl;
    cout << Xor(tab4, 23, "ZZ2_F5", 6, tmp) << endl;
    cout << Xor(tab4, 23, Xor("\x1c\x6f\x74\x6a\x00\x00", 6, "F5", 2, tmp1), 6, tmp) << endl; // ZZ2_F5
}

int main()
{
    f2();
    return 0;
}
