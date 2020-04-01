jupyter tutorial can be found at
https://www.youtube.com/watch?v=HW29067qVWk&feature=youtu.be
    
Magic commands:
    1. bash commands
    2. timeit: to time cell execution
    3. debug: to run a cell in debug mode


# Linking R kernel to jupyter notebook

For CentOS 7:
	1. yum install openssl-devel
	2. sudo yum install R
	3. cd /usr/bin
For all systems:
	open R
	install.packages("devtools")
	devtools::install_github("IRkernel/IRkernel")
	IRkernel::installspec()

In order, they (1) install the devtools package which gets you the install_github() function, (2) install the IR Kernel from github, and (3) tell Jupyter where to find the IR Kernel.
