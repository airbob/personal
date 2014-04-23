C# wpf notes
======

### how to change button name

```c#
<Button Content="New name of button"   />
```

### button linked functions
```c#
<Button Click="button1_Click" />
//in MainWindow.xaml.cs
private void button1_Click(object sender, RoutedEventArgs e)
        {
            dataBox.Text = "hi shan completed";
        }
```

### how to add debug messages
```c#
using System.Diagnostics;
// then add debug message when needed
Debug.WriteLine("init the main window");
```
### how to do linear/least square regression?
[ref](http://www.codeproject.com/Articles/63170/Least-Squares-Regression-for-Quadratic-Curve-Fitti)

### how to draw chart in wpf?
by default there is no chart component in toolbox, I found a few chart library can be used.
The most common one is [WPF ToolKit](https://wpf.codeplex.com/releases/view/40535)
1. install the tool kit first
2. Add reference
3. Add following code in head of xaml file:
```c#
xmlns:DV="clr-namespace:System.Windows.Controls.DataVisualization;assembly=System.Windows.Controls.DataVisualization.Toolkit"
        xmlns:DVC="clr-namespace:System.Windows.Controls.DataVisualization.Charting;assembly=System.Windows.Controls.DataVisualization.Toolkit"
```
4. Add the chart inside of GRID
```c#
<DVC:Chart Canvas.Top="80" Canvas.Left="10" Name="mcChart"
           Width="400" Height="250"
           Background="LightSteelBlue">
            <DVC:Chart.Series>
                <DVC:ScatterSeries Title="Dots" Name="scatter"
            IndependentValueBinding="{Binding Path=Key}"
            DependentValueBinding="{Binding Path=Value}">
                </DVC:ScatterSeries>

            </DVC:Chart.Series>
        </DVC:Chart>
```
5. Add the data binding functions in .xaml.cs file
```c#
using System.Windows.Controls.DataVisualization.Charting;

namespace WpfApplication2
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            LoadScatterChartData();  //test case 1
            LoadScatterChartData2(); //test case 2
        }
        private void LoadScatterChartData()
        {

            ((ScatterSeries)mcChart.Series[0]).ItemsSource =
                new KeyValuePair<DateTime, int>[]{
            new KeyValuePair<DateTime, int>(DateTime.Now, 100),
            new KeyValuePair<DateTime, int>(DateTime.Now.AddMonths(1), 130),
            new KeyValuePair<DateTime, int>(DateTime.Now.AddMonths(2), 150),
            new KeyValuePair<DateTime, int>(DateTime.Now.AddMonths(3), 125)
            };

        }
        private void LoadScatterChartData2()
        {
            List<KeyValuePair<int, int>> plot = new List<KeyValuePair<int, int>>();
            plot.Add(new KeyValuePair<int, int>(12, 1));
            plot.Add(new KeyValuePair<int, int>(24, 2));
            plot.Add(new KeyValuePair<int, int>(36, 3));
            plot.Add(new KeyValuePair<int, int>(48, 4));
            scatter.ItemsSource = plot;
        }
    }
}
```

[reference](http://www.c-sharpcorner.com/uploadfile/mahesh/scatter-chart-in-wpf/)

### how to add global varialbes
```c#
        public MainWindow()
        {
            InitializeComponent();
            int local1 = 2;
            local1 = Global.global1;
            Debug.WriteLine("local variable 1 is " + local1);
        }
        public class Global
        {
            public static int global1 = 3;
            public static int global2 = 4;
        }
```

### how to exit current application programmingly
```c#
Application.Current.Shutdown();
```


### win 7(home premium) can not install visual studio 2013 
a few reasons:  <br>
1. install [win 7 SP1](http://www.microsoft.com/en-us/download/details.aspx?id=5842) <br>
2. [which SP1 to choose?](http://social.technet.microsoft.com/Forums/windows/en-US/0c260197-950a-4dd7-b277-3ed033242b7a/what-files-to-download-for-w7-sp1?forum=w7itprogeneral)<br>

### reference visifire:
1. add *.dll files in binaries folder <br>
2. in *.cs file add 
```c#
using Visifire.Charts;
using Visifire.Commons;
```
3. in *.xaml file
```c#
xmlns:vc="clr-namespace:Visifire.Charts;assembly=WPFVisifire.Charts"
```

### comparison of chart libraries in wpf:
[ref](http://stackoverflow.com/a/16180699/874585)

### wpf controls

**Grid** Arranges controls in rows and columns and a **StackPanel** arranges controls in a single row either vertically or horizontally

### how to bind slider and label?
```c#
<Grid x:Name="MyChartGrid2"  Margin="5,5,5,5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
<Slider Name="slider1" HorizontalAlignment="Left" Margin="50,10,0,0" VerticalAlignment="Top" Width="500" SmallChange="1" IsSnapToTickEnabled="True" Maximum="100" Value="49" ValueChanged="Slider_ValueChanged" />
<Label Name="label1" Content="{Binding ElementName=slider1, Path=Value}"   HorizontalAlignment="Left" Margin="589,10,0,0" VerticalAlignment="Top"/>
</Grid>

        private void Slider_ValueChanged(object sender,
        RoutedPropertyChangedEventArgs<double> e)
        {
            // ... Get Slider reference.
            var slider = sender as Slider;
            int value = (int)slider.Value;
            this.Title = "Value: " + value.ToString("0.0") + "/" + slider.Maximum;
        }
```

### how to use progress bar
[ref1](http://www.codeproject.com/Articles/38555/WPF-ProgressBar) <br>
[ref2](http://www.wpf-tutorial.com/misc-controls/the-progressbar-control/)

### set progress bar hidden

```c#
ProgressBar1.Visibility = Visibility.Hidden;
```

### how to implement a "select foder dialog"

1. add reference of System.Windows.Forms (located at  C:\Program Files (x86)\Reference Assemblies\Microsoft\Framework\.NETFramework\v4.0\....) <br>
2. using System.Windows.Forms; <br>
3. add following code inside the methods:<br>
```c#
var dialog = new System.Windows.Forms.FolderBrowserDialog();
System.Windows.Forms.DialogResult result = dialog.ShowDialog();
var folder = dialog.SelectedPath;
Debug.WriteLine(folder);
var subFolders = System.IO.Directory.GetDirectories(folder);
Debug.WriteLine(subFolders[0]);
```

## Visifire

### how to format Y axis to 0.0001 digits?
```c#
Axis axisY = new Axis();
axisY.ValueFormatString = "#,0.0000#";
```

### how to change marker size?
```c#
DataPoint dataPoint = new DataPoint();
dataPoint.XValue = val1;
dataPoint.YValue = val2;
dataPoint.MarkerScale = 0.1;
```

### how to change marker style?
```c#
DataSeries dataSeries = new DataSeries();
dataSeries.MarkerType = MarkerTypes.Square;
```

### how to change dataSeries display name:
```c#
 dataSeries.LegendText = "series name";
```
