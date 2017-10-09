// Block Chain should maintain only limited block nodes to satisfy the functions
// You should not have all the blocks added to the block chain in memory 
// as it would cause a memory overflow.

import java.util.*;

public class BlockChain {
    public static final int CUT_OFF_AGE = 10;

    /**
     * create an empty block chain with just a genesis block. Assume {@code genesisBlock} is a valid
     * block
     */
    private Map<ByteArrayWrapper, Block> tree = new HashMap<ByteArrayWrapper, Block>();// hash Integer->block
    private Map<ByteArrayWrapper, Integer> heights = new HashMap<ByteArrayWrapper, Integer>();// hash Integer->height
    private Map<ByteArrayWrapper, UTXOPool> utxoPools = new HashMap<ByteArrayWrapper, UTXOPool>();// hash Integer->utxoPool
    private Block maxHeightBlock;
    private TransactionPool transactionPool = new TransactionPool();

    public BlockChain(Block genesisBlock) {
        UTXOPool utxoPool = new UTXOPool();
        addCoinbaseToUTXOPool(genesisBlock, utxoPool);

        ByteArrayWrapper hash = new ByteArrayWrapper(genesisBlock.getHash());
        tree.put(hash, genesisBlock);
        heights.put(hash, 1);
        utxoPools.put(hash, utxoPool);

        maxHeightBlock = genesisBlock;
    }

    /** Get the maximum height block */
    public Block getMaxHeightBlock() {
        return maxHeightBlock;
    }

    /** Get the UTXOPool for mining a new block on top of max height block */
    public UTXOPool getMaxHeightUTXOPool() {
        UTXOPool pool = utxoPools.get(new ByteArrayWrapper(maxHeightBlock.getHash()));
        return new UTXOPool(pool);
    }

    /** Get the transaction pool to mine a new block */
    public TransactionPool getTransactionPool() {
        return transactionPool;
    }

    /**
     * Add {@code block} to the block chain if it is valid. For validity, all transactions should be
     * valid and block should be at {@code height > (maxHeight - CUT_OFF_AGE)}.
     * 
     * <p>
     * For example, you can try creating a new block over the genesis block (block height 2) if the
     * block chain height is {@code <=
     * CUT_OFF_AGE + 1}. As soon as {@code height > CUT_OFF_AGE + 1}, you cannot create a new block
     * at height 2.
     * 
     * @return true if block is successfully added
     */
    public boolean addBlock(Block block) {
        if(block == null || block.getPrevBlockHash()==null) return false;

        ByteArrayWrapper prevHash = new ByteArrayWrapper(block.getPrevBlockHash());
        if(!tree.containsKey(prevHash)) return false;

        int prevHeight = heights.get(prevHash);
        ByteArrayWrapper maxHash = new ByteArrayWrapper(maxHeightBlock.getHash());
        int maxHeight = heights.get(maxHash);

        int height = prevHeight + 1;

        if(height <= maxHeight - CUT_OFF_AGE) return false;

        UTXOPool pool = utxoPools.get(prevHash);
        TxHandler handler = new TxHandler(new UTXOPool(pool));
        Transaction[] txs = block.getTransactions().toArray(new Transaction[0]);
        Transaction[] validTxs = handler.handleTxs(txs);
        if (validTxs.length != txs.length) {
            return false;
        }
        addCoinbaseToUTXOPool(block, handler.getUTXOPool());

        ByteArrayWrapper currentHash = new ByteArrayWrapper(block.getHash());
        tree.put(currentHash, block);
        heights.put(currentHash, height);
        utxoPools.put(currentHash, handler.getUTXOPool());

        if(height > maxHeight) {
            maxHeightBlock = block;
        }
        return true;
    }

    private void addCoinbaseToUTXOPool(Block block, UTXOPool utxoPool) {
        Transaction coinbase = block.getCoinbase();
        for (int i = 0; i < coinbase.numOutputs(); i++) {
            Transaction.Output out = coinbase.getOutput(i);
            UTXO utxo = new UTXO(coinbase.getHash(), i);
            utxoPool.addUTXO(utxo, out);
        }
    }
    /** Add a transaction to the transaction pool */
    public void addTransaction(Transaction tx) {
        transactionPool.addTransaction(tx);
    }
}