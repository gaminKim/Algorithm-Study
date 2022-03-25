import java.util.*;

class Solution {
    public int getTime(String time) {
        String[] s = time.split(":");
        return Integer.parseInt(s[0]) * 60 + Integer.parseInt(s[1]);
    }
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};
        Map<String, Integer> in = new TreeMap<>();
        Map<String, Integer> totalTime = new TreeMap<>();

        for (String s : records) {
            String[] arr = s.split(" ");
            if (arr[2].equals("IN")) {
                in.put(arr[1], getTime(arr[0]));
            } else {
                int time = getTime(arr[0]) - in.get(arr[1]);
                totalTime.merge(arr[1], time, Integer::sum);
                in.remove(arr[1]);
            }
        }
        for (String key : in.keySet()) {
            int inTime = in.get(key);
            int outTime = getTime("23:59");

            int time = outTime - inTime;
            totalTime.merge(key, time, Integer::sum);
        }

        answer = new int[totalTime.size()];
        int i = 0;
        for (String key : totalTime.keySet()) {
            int time = totalTime.get(key);
            int value = fees[1];
            if (time > fees[0]) {
                value += fees[3] * (int) Math.ceil((time - fees[0]) / (double) fees[2]);
            }
            answer[i] = value;
            i++;
        }
        return answer;
    }
}