
class Student {
    String name;
    int Rollno;
    int percentage;

    public Student(String name,int Rollno,int percentage){
        this.name=name;
        this.Rollno=Rollno;
        this.percentage=percentage;
    }

    public void setpercent(int Rollno,int newp){
        this.percentage=newp;
    }

    public static void main(String[] args){
        Student s1=new Student("Rajeev",101,96);
    }

    
}
