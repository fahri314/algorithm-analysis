template <class vType,int size>
class graphType{
public:        
    bool isEmpty();
    void createGraph();
    void clearGraph(); //Vertices Deallocated
    void printGraph();
    graphType();       //Default Constructor [ gsize=0 and maxSize=size ]
    ~graphType();      //Storage Deallocated
protected:
    int maxSize;       //Max Number of Vertices
    int size;          //Current Number of Vertices
    linkedListGraph<vType> *graph; //Array of Pointers to Create
};                                 //The Adjacaceny List           
