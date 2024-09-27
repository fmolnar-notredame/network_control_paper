# Global network control from local information - Supplementary Information
by Aleksandar Haber, Ferenc Molnar, and Adilson E. Motter

## Abstract

In the classical control of network systems, the control actions on a node are determined as a
function of the states of all nodes in the network. Motivated by applications where the global state
cannot be determined in real time due to limitations in the collection, communication, and processing
of data, here we introduce a control approach in which the control actions can be computed as a
function of the states of nodes within a limited state information neighborhood. The trade-off
between the control performance and the size of this neighborhood is primarily determined by
the condition number of the controllability Gramian. Our theoretical results are supported by
simulations on regular and random networks and are further illustrated by an application to the
control of power-grid synchronization. We demonstrate that for well-conditioned Gramians, there
is no significant loss of control performance as the size of the state information neighborhood is
reduced, allowing efficient control of large networks using only local information.

## Contents of this Repository

### [Adjacency]
Network adjacency information for the RGG and Iceland networks in edge-list format. 
In the files each line indicates an edge, identified by the two node labels.

### [Figures_Iceland]
State Information Neighborhood (SIN) Plots for the Iceland network. 

Each file is labelled by the central node of the SIN.

Network parameters:
- Number of nodes = 224
- Number of edges = 238

SIN parameters:
- f = 2
- q = 2

### [Figures_RGG]
State Information Neighborhood (SIN) Plots for the Random Geometric Graph (RGG) network. 

Each file is labelled by the central node of the SIN.

Network parameters:
- Number of nodes = 702
- Number of edges = 3390

SIN parameters:
- f = 5
- q = 3

### [Script]
Utilities to generate this github repository.

