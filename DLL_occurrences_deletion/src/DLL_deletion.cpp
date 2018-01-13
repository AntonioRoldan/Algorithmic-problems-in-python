#include <iostream>
#include <vector>
#include <map>

//Nodes and lists use public data members for convenience
//This may make some software engineers froth at the mouth

class Node
{
public:
    int value; //This could really be any type
    Node* next;
    Node* prev;
    Node(int val) {
        std::cout << "Node constructor!" << std::endl;
        this->value = val;
        this->next = (Node*)0;
        this->prev = (Node*)0;
    }
    ~Node() {
        std::cout << "Node destructor" << std::endl;
        std::cout << "I had the value " << this->value << std::endl;
    }
};
class List
{

public:
    Node* head;
    Node* tail;

    List() {
        std::cout << "List Constructor!" << std::endl;
        this->head = 0;
        this->tail = 0;
    }
    ~List() {
        std::cout << "List destructor!" << std::endl;
        std::cout << "Todo: properly delete nodes..." << std::endl;
    }
    void insert(Node* n, Node* x) {
        if (n != 0) {
            x->next = n->next;
            n->next = x;
            x->prev = n;
            if (x->next != 0)
                x->next->prev = x;
        }
        if (this->head == 0) {
            this->head = x;
            this->tail = x;
            x->prev = 0;
            x->next = 0;
        }
        else if (this->tail == n) {
            this->tail = x;
        }
    }

    Node* find_node(int data){
        Node* cur = this->head;
        while(cur != 0){
            if (cur->value == data){
                return cur;
            } else{
                cur = cur->next;
            }
        }
    }

    void deletion(int data){
        Node* n = find_node(data);
        if (n->prev != 0){
            n->prev->next = n->next;
        } else{
            this->head = n->next;
        }
        if(n->next != 0){
            n->next->prev = n->prev;
        } else{
            this->tail = n->prev;
        }
    }

    void delete_occurences(){
        std::pair<int, int> occurrencesp;
        std::map<int, int> occurrences;
        Node*i = this->head;
        Node* cur;
        int value;
        while(i != 0){
            cur = i;
            value = cur->value;
            if(occurrences.find(value) != occurrences.end()){ //If element is already in the dictionary
                occurrences[value] += 1; //We increase its amount of occurrences by one
            } else{
                occurrences[value] = 1; //Else we just set it to one
            }
            i = i->next; //We keep on iterating through the list
        }
        for(std::map<int, int>::iterator it = occurrences.begin(); it != occurrences.end(); it++){
            if(it->second > 1){
                for(int i = 0; i < it->second; i++){
                    deletion(it->first);
                }
            }
        }
    }

    void display() {
        Node* i = this->head;
        std::cout << "List: ";
        while (i != 0) {
            std::cout << i->value << ",";
            i = i->next;
        }
        std::cout << std::endl;
    }
};

int main(int argc, char *argv[])
{
    List* l = new List();
    l->insert(0, new Node(4));
    l->insert(l->head, new Node(4));
    l->insert(l->head, new Node(6));
    l->insert(l->head, new Node(8));
    l->insert(l->head, new Node(8));
    l->display();
    l->deletion(6);
    l->display();
    l->delete_occurences();
    l->display();
    delete l;
    return 0;
}
