public class Solution {
    public boolean isPalindrome(String s) {
        // int head = 0, tail = s.length()-1;
        // if(s.isEmpty()){
        //     return true;
        // }
        // while(head < tail){
        //     Character headC = s.charAt(head);
        //     Character tailC = s.charAt(tail);
        //     if(!Character.isLetterOrDigit(headC)){
        //         head++;
        //     }else if(!Character.isLetterOrDigit(tailC)){
        //         tail--;
        //     }else{
        //         if(Character.toLowerCase(headC) != Character.toLowerCase(tailC)){
        //             return false;
        //         }else{
        //             head++;
        //             tail--;
        //         }
        //     }
        // }
        // return true;



        // faster version
        int head = 0, tail = s.length()-1;
        int sLength = s.length();
        if(s.isEmpty()){
            return true;
        }
        while(head < tail){
            while(!Character.isLetterOrDigit(s.charAt(head))){
                head++;
                if(head == sLength){
                    return true;
                }
            }
            while(tail > 0 && !Character.isLetterOrDigit(s.charAt(tail))){
                tail--;
                if(tail == -1){
                    return true;
                }
            }
            if(Character.toLowerCase(s.charAt(head)) != Character.toLowerCase(s.charAt(tail))){
                return false;
            }else{
                head++;
                tail--;
            }
        }
        return true;
    }
}