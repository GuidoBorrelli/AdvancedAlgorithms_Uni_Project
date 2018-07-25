# Project Advanced Algorithms 2017/2018

This is the the folder for the project of the AAPP course attended at Politecnico di Milano.

# Project specifications
Implementation and comparison of performance to find strongly connected components within a graph
* Tarjan algorithm
* Nuutila algorithm
* Pearce algorithm

# Project implementation
#### To start the program
* Check global variable `TEST` set to False
* Run main.py
* Optionally set `SIZE_BENCHMARK` to another value
#### To test correctness of algorithms
* Check global variable `TEST` set to True
* Optionally set global variable `TEST_NODE_SIZE` to a valid number 
* Optionally set global variable `TEST_EDGE_PROBABILITY` to a valid number (0,1) 
* If either `TEST_NODE_SIZE` or `TEST_EDGE_PROBABILITY` are set to 0, a valid random value is automatically generated
* If `TEST_NODE_SIZE` either given or generated is lower than 50 a graph showing SCCs is showed
# Project documentation
#### main.py
* This file contains the main: it performs either a check of SCCs in randomly generated graphs or a test of correctness of algorithms
* Check of SCCs works in such a way
	* A test set is generated for several categories of graphs. Each of these categories is performed with different number of nodes contained in `dimension_list`, and density: sparse, normal, dense
 	* A set of graphs for the benchmark of each category is created and each graph performance recorded
 	* After this phase, the file related to plot performance results is called
 	* My initial idea was to quantify the size of graphs of each benchmark in an adaptive fashion to maximize samples when computation allowed it, but I haven't find a nice fashion and fixed the value to a global constant value in head of file
* Test of correctness of algorithms works in such a way
	* Global variable `TEST` in main.py is manually set to True
	* Eventually global variables `TEST_NODE_SIZE` and `TEST_EDGE_PROBABILITY` are set to valid number, as specified below for wrt implentation
	* Main method detects test environment is required and call function within file test.py
#### test.py
* Function is called with eventually parametrised values of test, otherwise values are randomly generated
* After a graph is generated, SCCs are retrieved for each algorithm manually implemented and by a builtin function offered by networkx
* Results are then compared with the assumed true builtin function in DEBUG mode
* Results are validated through verifying that each pair of node is effectively in the same component or not as expected by its property
* If the generated graph is lower or equal of 40 nodes size, then the graph is printed and not single SCCs are coloured for the sake of clarity
#### stack.py
* This file has been created to create a support class Stack due to reproduce the stack behaviour, and develope desired functions
#### performance.py
* This file is related to what concern managing of performance dictionary records and creation of significance measures
* extract_statistics function deal with extraction of statistics value
* plot_graph function deal with the plotting settings of matplotlib
* Initial idea was to plot an errorbar: that means visualizing together mean and standard deviation. Due to higher standard deviation, bigger than mean, the graphic became not really readable. High standard deviation in some categories is due to variability of graph generation that is very effective when graph is small.
* For such reasons a plot for both mean and variance is saved within the graph folder
#### alg1.py
* Implementation of Tarjan algorithm
* Commented lines explain some choices of implementation
* In particular, when a component is removed from stack and assigned to a component, its root reference is "updated" in order to let test algorithm correctness
#### alg2.py
* Implementation of Nuutila algorithm 2 (so called in paper)
* Commented lines explain some choices of implementation
* In particular, a small function at end of the algorithm has been added to collect within root array all root "updated" references in order to let test algorithm correctness
#### alg3.py
* Implementation of Pearce algorithm PEA_FIND_SSC2 (so called in paper)
#### graph folder
* Within this folder performance records plot are saved for both mean and variance for each category of graph: sparse, normal, dense
* Within each image, algorithms are compared and presented with different colors

## Student
* Guido Borrelli - 874451
