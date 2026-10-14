/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        if(!head) return head;
        Node* curr=head;
        while(curr){
            if(curr->child){
                Node* tailchild=curr->child;

                while(tailchild->next){
                    tailchild=tailchild->next;
                }
                if(curr->next){
                    tailchild->next=curr->next;
                    curr->next->prev=tailchild;
                }
                curr->next=curr->child;
                curr->child->prev=curr;
                curr->child=nullptr;
            }
            curr=curr->next;
        }
        return head;
    }
};