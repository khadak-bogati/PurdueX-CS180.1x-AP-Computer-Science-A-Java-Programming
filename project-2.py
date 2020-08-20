CS	180	HS	– Topic	2
Project 2: Associative	Property
In	this	Java	programming	assignment,	you	will	practice	using	primitive	data	types	in	order	to	perform	simple	arithmetic	
applying	the	associative	property.
I. Design	a	class	called	Associative in	a	file	called	Associative.java.	This	class	will	hold	the	main	method,	and	the	class	
methods	that	we	will	write	in	this	assignment.
II. Write	an	empty public	static	void	main(String[]	args) method.	This	method	should	appear	inside	the	curly	braces	of	
the	Associative	class.
III. Create	three	class	variables,	all	integers.	
IV. Write	a	class	constructor,	that	assigns	values	from	three	parameters	passed	to	the	constructor	to	the	three	class	
variables	that	you	created	for	your	Associative	class.
V. Write	two class	methods (firstTwo,	lastTwo). The	method	firstTwo should	combine	the	three	class	variables by	
grouping	the	sum	of	the	first	two	class	variables,	and	then	multiplying	that	result	by	the	third	class	variable and	
returning	the	result.	The	method	lastTwo should	combine	the	three	class	variables	by	grouping	the	product	of	
the	last	two	class	variables,	and	then	adding	the	result	to	the	first	class	variable and	returning	the	result.	If	you	
call	your	variables	x,y, and	z	for	example,	the	calculations	should	appear	as	below.
firstTwo:	 (x	+	y)	*	z
lastTwo: x	+	(y	*	z)
VI. Complete	the	definition	for	main.	Your	program	should	create	a	new	Scanner object, prompt	the	user	to	type	in	
three	integers,	and	then	store	three	integer	values	from	standard	input.	The	main method	should	then	create	a	
new	Associative object,	and	print	out	two	lines	like	that	display	the	results	of	calling	your	firstTwo and	lastTwo
methods.	For	example,	if	the	user	enters	1,	2,	and	3	as	inputs:
“Grouping	the	first	two	terms,	(1	+	2)	* 3	=	9”
“Grouping	the	last	two	terms,	1	+	(2	* 3)	=	7”
VII. Submit	your	Associative.java file	on	Blackboard.



import java.util.Scanner;
public class Associative {
  public int x;
  public int y;
  public int z;
  int firstTwo(){
    return (x + y) * z;
  }
  int lastTwo(){
    return x * (y+z);
  }
  
  public Associative(int x, int y, int z){
    this.x = x;
    this.y = y;
    this.z = z;
  }
  public static void main(String[] args) { 
    Scanner s = new Scanner(System.in);
    int x = s.nextInt();
    int y = s.nextInt();
    int z = s.nextInt();
    int firstTwo = (x + y) *3;
    int lastTwo = x +(2 + 3);
      
    Associative asc = new Associative(x, y, z);
    int a = asc.firstTwo();
    int b =asc.lastTwo();
  }
}
    

