Project 1: All	About	Me Rubric
I. Completion	Tasks (1	pt	each,	unless	specified)
a. AboutMe	Class	header
b. main	method	prototype
c. main	method	body
i. created	AboutMe	object
ii. printed	statement,	using	AboutMe	method	calls (3 pts)
d. class	methods
i. method	prototypes (3pts)
e. submitted	as	specified
II. Correctness (
a. AboutMe	compiles
b. Each	method	runs	as	expected	(3pts)
c. Program	successfully	prints	output (“My	name	is	Phil,	and	I	attend	Purdue	University.	I	am	36 years	
old.”)
TOTAL:	10 +	5	=	15 pts



/**
 * Project 1 -- About me
 * This program inputs the my name my age and my school name
 
 *
 * @author Khadka Bogati
 *
 * @recitation 03 (Andy Scharlott)
 *
 * @date Augest  19, 2020
 *
 */
public class AboutMe {
    
  
  public static void main(String[] args) {  
    String name = myName();
    String school = mySchool();
    int age = myAge();
    String output = "My name is " + name + " and I attend " + school + " I am " + age+ " years old";
    System.out.print(output);
  }  
  public static String myName(){
    return "Phil";
  }
  public static String mySchool(){
    return "Purdue University";
  }
  public static int myAge(){
    return 36;
  }
}
