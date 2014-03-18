## Eclipse

## Command line java compilation

```
javac start/HelloWorldSwing.java
java start.HelloWorldSwing
```


## Learning notes

- [how to compile a simple java file in eclipse](http://www.javaprogrammingforums.com/java-jdk-ide-tutorials/253-beginners-eclipse-tutorial-how-run-first-java-application-eclipse.html)

I also learned a few tutorials about unit test in java, here is a good [reference](http://eclipsetutorial.sourceforge.net/totalbeginner.html)


## java swing

Since the project will need java swing, I think I better take a look at it earlier, so here are two pieces of simple code snippet to generate a frame:

```java
import javax.swing.SwingUtilities;
import javax.swing.JFrame;

public class SwingPaintDemo1 {
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
    
    private static void createAndShowGUI() {
        System.out.println("Created GUI on EDT? "+
                SwingUtilities.isEventDispatchThread());
        JFrame f = new JFrame("Swing Paint Demo");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(250,250);
        f.setVisible(true);
    }
}
```


```java
package eclipsePackage;
import javax.swing.*; 
public class TutorialClass {
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("HelloWorldSwing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setExtendedState(frame.MAXIMIZED_BOTH);

        //Add the ubiquitous "Hello World" label.
        JLabel label = new JLabel("Hello World");
        frame.getContentPane().add(label);

        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
	}
}
```






