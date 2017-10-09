import java.util.ArrayList;
import java.util.Set;
import java.util.*;

/* CompliantNode refers to a node that follows the rules (not malicious)*/
public class CompliantNode implements Node {

    private final double p_graph;
    private final double p_malicious;
    private final double p_txDistribution;
    private final int numRounds;

    private boolean[] followees;
    private int numFollowees;

    public CompliantNode(double p_graph, double p_malicious, double p_txDistribution, int numRounds) {
        this.p_graph = p_graph;
        this.p_malicious = p_malicious;
        this.p_txDistribution = p_txDistribution;
        this.numRounds = numRounds;
    }

    public void setFollowees(boolean[] followees) {
        this.followees = followees;
        numFollowees = 0;
        for(boolean followee : followees) {
            if(followee) numFollowees++;
        }
    }

    Map<Transaction, Integer> map = new HashMap<>();
    private int countRound = 0;

    public void setPendingTransaction(Set<Transaction> pendingTransactions) {
        map.clear();
        countRound = 0;
        for(Transaction transaction : pendingTransactions) {
            map.put(transaction, 1);
        }
    }

    public Set<Transaction> sendToFollowers() {
        Set<Transaction> set = new HashSet<>();
        for(Map.Entry<Transaction, Integer> kv : map.entrySet()) {
            if(kv.getValue() > numFollowees * p_txDistribution * (1-p_malicious) * countRound) {
                set.add(kv.getKey());
            }
        }
        return set;
    }

    public void receiveFromFollowees(Set<Candidate> candidates) {
        for(Candidate candidate : candidates ) {
            if(map.containsKey(candidate.tx) && followees[candidate.sender]) {
                map.put(candidate.tx, map.get(candidate.tx) + 1);
            }
            else {
                map.put(candidate.tx, 1);
            }
        }
        countRound++;
    }
}
