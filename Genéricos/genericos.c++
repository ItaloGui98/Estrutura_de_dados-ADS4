
#include <iostream>
using namespace std;

// PILHA
template <class T, class U>
class Pilha {
    T valores[10];
    U outros[10];
    int topo;

public:
    Pilha() {
        topo = -1;
    }

    void inserir(T valor, U outro) {
        if (topo < 9) {
            topo++;
            valores[topo] = valor;
            outros[topo] = outro;
        }
    }

    void remover() {
        if (topo >= 0) {
            topo--;
        }
    }

    void mostrar() {
        cout << "\nPilha:\n";

        for (int i = topo; i >= 0; i--) {
            cout << valores[i] << " - " << outros[i] << endl;
        }
    }
};

// FILA
template <class T, class U>
class Fila {
    T valores[10];
    U outros[10];
    int inicio, fim;

public:
    Fila() {
        inicio = 0;
        fim = -1;
    }

    void inserir(T valor, U outro) {
        if (fim < 9) {
            fim++;
            valores[fim] = valor;
            outros[fim] = outro;
        }
    }

    void remover() {
        if (inicio <= fim) {
            inicio++;
        }
    }

    void mostrar() {
        cout << "\nFila:\n";

        for (int i = inicio; i <= fim; i++) {
            cout << valores[i] << " - " << outros[i] << endl;
        }
    }
};

// LISTA
template <class T, class U>
class Lista {
    T valores[10];
    U outros[10];
    int quantidade;

public:
    Lista() {
        quantidade = 0;
    }

    void inserir(T valor, U outro) {
        if (quantidade < 10) {
            valores[quantidade] = valor;
            outros[quantidade] = outro;
            quantidade++;
        }
    }

    void remover() {
        if (quantidade > 0) {
            quantidade--;
        }
    }

    void mostrar() {
        cout << "\nLista:\n";

        for (int i = 0; i < quantidade; i++) {
            cout << valores[i] << " - " << outros[i] << endl;
        }
    }
};

int main() {

    Pilha<int, string> p;
    Fila<int, string> f;
    Lista<int, string> l;

    p.inserir(1, "Ana");
    p.inserir(2, "Joao");
    p.mostrar();
    p.remover();
    p.mostrar();

    f.inserir(1, "Ana");
    f.inserir(2, "Joao");
    f.mostrar();
    f.remover();
    f.mostrar();

    l.inserir(1, "Ana");
    l.inserir(2, "Joao");
    l.mostrar();
    l.remover();
    l.mostrar();

    return 0;
}