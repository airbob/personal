## [KIF framework notes](https://github.com/kif-framework/KIF)

### where to set accessory labels, etc
it is in inspector instead of attribute 

### tester object
The tester object is a special shortcut to an instance of the KIFUITestActor class.

### simulate tap
```objective-c
    [tester tapViewWithAccessibilityLabel:@"Settings"];
```

### how to set uiswitch
```objective-c
    [tester setOn:YES forSwitchWithAccessibilityLabel:@"Debug Mode"];
```

### assert uislider value
```objective-c
    UISlider *slider = (UISlider *)[tester waitForViewWithAccessibilityLabel:@"Work Time Slider"];
    STAssertEqualsWithAccuracy([slider value], 15.0f, 0.1, @"Work time slider was not set!");
```

### how to simulate text input
```objective-c
    [tester enterText:@"Set up a test" intoViewWithAccessibilityLabel:@"Task Name"];
    [tester tapViewWithAccessibilityLabel:@"done"];
```

### how to simulate tap table view 
1st need to set tableview clickable
in tableview controller viewDidLoad add

```
[self.tableView setAccessibilityLabel:@"History List"];
[self.tableView setIsAccessibilityElement:YES];
```

```objective-c
    [tester tapRowInTableViewWithAccessibilityLabel:@"Presets List"
                                        atIndexPath:[NSIndexPath indexPathForRow:index inSection:0]];
```

### how to simulate uistepper and tap actions
```objective-c
    UIStepper *repsStepper = (UIStepper*)[tester waitForViewWithAccessibilityLabel:@"Reps Stepper"];
    CGPoint stepperCenter = [repsStepper.window convertPoint:repsStepper.center
                                                    fromView:repsStepper.superview];
    
    CGPoint minusButton = stepperCenter;
    minusButton.x -= CGRectGetWidth(repsStepper.frame) / 4;
    
    CGPoint plusButton = stepperCenter;
    plusButton.x += CGRectGetWidth(repsStepper.frame) / 4;
    [tester tapScreenAtPoint:minusButton];
```
### how to simulate tableview swipe
1st need to set setAccessibilityLabel in cellForRowAtIndexPath 

```
#ifdef DEBUG
  [cell setAccessibilityLabel:[NSString stringWithFormat:@"Section %ld Row %ld", (long)indexPath.section, (long)indexPath.row]];
#endif
```

then 

```objective-c
    UITableView *tableView = (UITableView *)[tester waitForViewWithAccessibilityLabel:@"History List"];
    NSInteger originalHistoryCount = [tableView numberOfRowsInSection:0];
    STAssertTrue(originalHistoryCount > 0, @"There should be at least 1 history item!");
    [tester swipeViewWithAccessibilityLabel:@"Section 0 Row 0" inDirection:KIFSwipeDirectionLeft];
    [tester tapViewWithAccessibilityLabel:@"Delete"];
```

### how to run only one test
click the square icon before the test name

### how to set DEBUG flag:
Build Settings -> preprocessings -> DEBUG=1

### KIF set up procedure
install cocoapods
pod init
edit Podfile to include KIF
pod install
click *.xcworkspace to start
new test files (subclass of KIFTestCase)

### wati for 1 seconds
```objective-c
[tester waitForTimeInterval:1];
```

## KIF articles
http://www.raywenderlich.com/61419/ios-ui-testing-with-kif
http://www.preeminent.org/steve/iOSTutorials/XCTest/

### cocoa pods recommends using utf-8 in termial
run ```export LANG=en_US.UTF-8``` before ```pod init``` or ```pod install```

## KIF issues
https://github.com/kif-framework/KIF/issues/310
http://stackoverflow.com/questions/18888059/cannot-find-executable-for-cfbundle-certuiframework-axbundle/18889514#18889514
http://stackoverflow.com/questions/18036381/xcode-5-error-certuiframework-axbundle
