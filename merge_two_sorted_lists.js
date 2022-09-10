/**

* Definition for singly-linked list.

* function ListNode(val, next) {

*     this.val = (val===undefined ? 0 : val)

*     this.next = (next===undefined ? null : next)

* }

*/

/**

* @param {ListNode} list1

* @param {ListNode} list2

* @return {ListNode}

*/

var mergeTwoLists = function(list1, list2) {

   

    

    

        fake_head = new ListNode();

        current= fake_head;

       

        first= list1;

        second=list2;

       

        

        while(first!==null && second!==null)

        {

            if(first.val<=second.val)

                {

                    current.next = first;

                    first = first.next;

                    current = current.next;

                }else

                    {

                       

                        current.next =second;

                    second = second.next;

                    current = current.next;

 

                       

                    }

            

        }

   

    while(first!==null)

        {

            current.next  = first;

            first = first.next;

            current= current.next;

        }

 

   

        while(second!==null)

        {

            current.next = second;

            second = second.next;

            current= current.next;

        }

 

 

    return fake_head.next;

   

    

};