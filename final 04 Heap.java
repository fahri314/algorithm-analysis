//The ADT Heap
//Interface used for implementation of maxheap

 public interface MaxHeapinterface {
  public void add(Comparable newEntry);
  public Comparable removeMax();
  public Comparable getMax();
  public boolean isEmpty();
  public int getSize();
  public void clear();
 } 

// end MaxHeapinterface
