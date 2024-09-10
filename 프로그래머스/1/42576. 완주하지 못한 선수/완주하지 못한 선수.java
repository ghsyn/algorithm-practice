import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        int tmp = 0;

        Map<Integer, String> hMap = new HashMap<>();
        for (String i : participant) {
            hMap.put(i.hashCode(), i);
            tmp += i.hashCode();
        }

        for (String i : completion) {
            tmp -= i.hashCode();
        }

        return hMap.get(tmp);
    }
}