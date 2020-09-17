package src.main.java;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Hash42576 {

    private static String setSolution(String[] participants, String[] completions) {
        String failed = "";
        if(participants.length > 1 && participants.length <= 100000) {
            if (completions.length == participants.length - 1) {
                for (String participant : participants) {
                    List<String> passed = Arrays.stream(completions).filter(x -> x.equals(participant)).collect(Collectors.toList());

                    if (passed.size() == 0) {
                        failed = participant;
                    }else{
                        long sameNameParticipate = Arrays.stream(participants).filter(x -> x.equals(participant)).count();
                        if(sameNameParticipate > passed.size()){
                            failed = participant;
                        }
                    }
                }

            }
        }
        return failed;
    }

    public static void main(String[] args){
        String[] participants = {"mislav", "stanko", "mislav", "ana"};
        String[] completions = {"stanko", "ana", "mislav"};
        String k = setSolution(participants,completions);
        System.out.println(k);
    }
}
