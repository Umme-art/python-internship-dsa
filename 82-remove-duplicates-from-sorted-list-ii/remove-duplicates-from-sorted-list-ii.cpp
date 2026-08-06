/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

        ListNode *prev = new ListNode(INT_MIN);
        prev->next = head;
        ListNode *ans = prev;
        while(head != nullptr){
            if(head->next == nullptr || head->val != head->next->val){
                prev->next = head;
                prev = prev->next;
                head = head->next;
            }else{
                while(head->next != nullptr && head->val == head->next->val)
                head = head->next;

                prev->next = head->next;
                head = head->next;
            }
        }
        return ans->next;
    }
};
 