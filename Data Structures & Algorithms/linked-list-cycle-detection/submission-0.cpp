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
    bool hasCycle(ListNode* head) {
        if (head == NULL) return false;
        ListNode *p1 = head, *p2 = head->next;
        while (p1 != NULL && p2 != NULL) {
            if (p1 != NULL) p1 = p1->next;
            if (p2 != NULL) p2 = p2->next;
            if (p2 != NULL) p2 = p2->next; // move p2 twice
            if (p1 == p2) return true;
        }
        return false;
    }
};
